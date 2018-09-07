import serial
import time
import matplotlib.pyplot as plt

emptyLine = 0
ser = serial.Serial('/dev/tty.usbmodem14121', 115200) #establishing connection

fig, ax = plt.subplots()
plt.xlim(0,1)
plt.ylim(-25, 25)

tstart = time.time()
num_plots = 0
while time.time()-tstart < 1:
    val = ser.readline()
    try: #if the reading is good do the following
        s1 = float(val)
        #s2 = float(val[1])
        ax.plot((time.time()-tstart), s1, 'ro')
        #ax.plot((time.time()-tstart), s2, 'bo')
        plt.pause(0.001)
        num_plots += 1
    except: #otherwise there was an empty line
        emptyLine += 1
    
print (num_plots)
print (emptyLine)
plt.show()