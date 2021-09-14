# Brainwave-Analyzer
## Introduction
A simple parser in Python to visualize the brainwave data collected from [NeuroSky Mindwave Mobile EEG Headset](http://neurosky.com/biosensors/eeg-sensor/biosensors/). This was originally developed as part of trying to explore whether it was possible to quantify the calmness induced by different music stimuli through brainwaves - Delta, Theta, Alpha, Beta and Gamma. The visualizer and spectogram plotter may be useful in other domains as well.

Brainwave spectral power logs from NeuroSky Mindwave SDK are exported to a file first and then analyzed through the parser provided here. An example spectral power log, parser, and final plot are provided.

# Usage
```
python brainview.py <bwave-power-log>
```
# Plot
![Spectrogram](myplot.png)
