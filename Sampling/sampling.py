import numpy as np
from numpy import pi, sin, cos, log10
from numpy.fft import fft
import matplotlib.pyplot as plt

# Parameters:
N = 64              # Must be a power of two
T = 1               # Set sampling rate to 1
A = 1               # Sinusoidal amplitude
phi = 0             # Sinusoidal phase
f = 0.25            # Frequency (cycles/sample)
n = np.arange(N)    # Discrete time axis
x = A*(sin(pi*n*f*T+phi) + 1/2*sin(2*pi*n*f*T+phi) + 1/3*sin(3*pi*n*f*T+phi) ) # Sampled sinusoid
X = fft(x)          # Spectrum

plt.figure(figsize=(10,10))

# Plot time data:
plt.subplot(3,1,1)
plt.plot(n,x,'o')        
ni = np.arange(0,N,0.1)   # Interpolated time axis
plt.plot(ni,A*(sin(pi*ni*f*T+phi) + 1/2*sin(2*pi*ni*f*T+phi) + 1/3*sin(3*pi*ni*f*T+phi) ),'red') 
plt.xlim(0,N)
plt.title('sin(pi*f*T) + 1/2sin(2*pi*f*T) + 1/3sin(3*pi*f*T)   f = 0.25')
plt.xlabel('Time (samples)') 
plt.ylabel('Amplitude')
plt.text(-.11*64,1,'a)')


# Plot spectral magnitude:
magX = abs(X)
fn = np.arange(0, 1, 1/N)  # Normalized frequency axis
plt.subplot(3,1,2)
plt.stem(fn,magX,'-ok', use_line_collection=True)
plt.grid()
plt.xlim(0,1)
plt.xlabel('Normalized Frequency (f/2 f 3f/2))') 
plt.ylabel('Magnitude (Linear)')
plt.text(-.11,30,'b)')

# Same thing on a dB scale:
spec = 20*log10(magX) # Spectral magnitude in dB
plt.subplot(3,1,3)
plt.plot(fn,spec,'--ok')
plt.grid()
plt.xlim(0,1)
plt.ylim(-350, 50)
#plt.axis([0 1 -350 50])
plt.xlabel('Normalized Frequency (f/2 f 3f/2))') 
plt.ylabel('Magnitude (dB)')
plt.text(-.11,0,'c)')

plt.show()
