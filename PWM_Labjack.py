from labjack import ljm
import time
from scipy import signal
import numpy as np

handle = ljm.openS("T7", "wifi", "ANY") #establishing labjack handle

ljm.eWriteName(handle, "DAC0", 0) #writing voltage of 0 to DAC0 pin
time.sleep(2) #giving voltage time to settle

cps = input('cycles per second: ')
trough_h = input('height of trough: ')
crest_h = input('height of crest: ')
percentON = input('percent of time wave is on: ')
ON = percentON/100
#inputs - eventually self-regulated according to stepper motor's needed speed

t = 0
while t <= t + 1: #infinite loop
      ljm.eWriteName(handle, "DAC0", (crest_h-trough_h)+(crest_h-trough_h)*signal.square(cps*2 * np.pi * t, duty=ON)) 
      #frequency: 1 hz, amplitude: (crest_h - trough_h) volts, on for ONs, off for 0.2s
      time.sleep(1/20) #pause-time
      t += 1/20

ljm.close(handle)

