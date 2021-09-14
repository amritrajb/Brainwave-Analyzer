#!/usr/bin/python

# Brainwave Analyzer
#
# Script for plotting the data from NeuroSky Mindwave Mobile EEG Headset
#  This parser takes brain wave power logs colleted from Mindwave SDK as input and plot the spectral power of waves 
#  and a spectrogram to visualize the brainwaves (Delta, Theta, Alpha, Beta and Gamma)
#
# 

import sys, getopt
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import CheckButtons

def main(argv):

   # read input files
   input_f1  = sys.argv[1]
   print("Reading from " + input_f1)

   i = 0;
   # TODO: Create a dictionary instread of lists
   delta = []
   theta = []
   alpha = []
   beta  = []
   gamma = []
   att   = []
   med   = []
   quality = []
   timestamp = []
   freq = []
   ratings = []

   #
   # Format of the line to be parsed
   # [ 18/ 1/2018 14:05:44:911 ] EEG Bandpower: Delta: 2.0400 Theta: 10.5469 Alpha: 7.4137 Beta: 4.3745 Gamma: 3.2990 ABD 3.0392
   #
   
   # Read file
   with open(input_f1) as f1:
       for line in f1:
           if (line.find("EEG") != -1):
               parts = line.split(']') # separate time stamp and data
               timestamp.append(parts[0])
               parts = parts[1].split(' ')
               #print(parts, timestamp)
               delta.append(float(parts[4]))
               theta.append(float(parts[6]))
               alpha.append(float(parts[8]))
               beta.append(float(parts[10]))
               gamma.append(float(parts[12]))
           if (line.find(" ATT") != -1):
               parts = line.split('=')
               att.append(float(parts[1]))
           if (line.find(" MED") != -1):
               parts = line.split('=')
               med.append(float(parts[1]))
           if (line.find(" PQ") != -1):
               parts = line.split('[')
               parts_right = parts[2].split(']')
               #print(parts_right[0])
               quality.append(float(parts_right[0])/50.0)

   x_size = len(alpha) # limit the size
   quality = quality[0:x_size]
  
   # There are threee plots. 
   #  1. brain wave spectral power 
   #  2. spectrogram of brainwave power
   #  3. Time interval

   # Adjust the plot sizes.
   size = 35
   size_1 = 15 #int(size/2)
   size_2 = 30 #int(size/2) * 2
   size_3 = 35
   ax2 = plt.subplot(size,1,(size_2+3,size_3))
   ax1 = plt.subplot(size,1,(size_1+3,size_2), sharex=ax2)
   ax0 = plt.subplot(size,1,(1,size_1),sharex=ax2)

   # 
   # Configure the Time interval
   # As the experiment was conducted by playing 7 music notes for 30 seconds preceded by 30 seconds of silence
   #   use this as the x-axis timeline. This can be modified based on the data capture
   for x in range(0,450):
       if ( (int(x/30) % 2) == 0):
           freq.append(0)
       else:
           freq.append(1)
   plt.sca(ax2)
   plt.xlabel('Time (min)')
   freq, = ax2.plot(freq,  label='Freq(x)')

   # Configure the spectral power plot
   x = np.arange(0.0,x_size/60, 1.0/60.0)
   q, = ax0.plot(quality, label='Quality')
   a, = ax0.plot(alpha,  label='Alpha')
   b, = ax0.plot(beta,   label='Beta')
   #ax.plot(att,   label='Att')
   #for label in ax.get_yticklabels()[::3]:
   # label.set_visible(False)
   g, = ax0.plot(gamma,  label='Gamma')
   d, = ax0.plot(delta,  label='Delta')
   t, = ax0.plot(theta,  label='Theta')
   plt.sca(ax0)
   plt.ylabel('Spectal Power')

   # Configure the spectogram  
   grid = [delta,theta,alpha,beta,gamma]
   #print(np.size(grid,1))
   grid_plot = ax1.pcolor(grid, cmap='jet')
   x_label = ['0', '1', '2', '3', '4', '5', '6','7','8']
   y_label = ['delta', 'theta', 'alpha', 'beta', 'gamma']
   plt.colorbar(grid_plot, ax=[ax0,ax1,ax2])
   plt.sca(ax1)

   plt.xticks(np.arange(0, x_size, 60),x_label)
   plt.yticks(np.arange(0.5, np.size(grid,0)+1,1), y_label)
   legend = ax0.legend(loc='best', shadow=True, fontsize = 'x-small')

   plt.savefig("myplot.png")
   plt.show()



if __name__ == "__main__":
   main(sys.argv[1:])
