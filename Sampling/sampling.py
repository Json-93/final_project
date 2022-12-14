import numpy as np
from numpy import pi, cos, log10
from numpy.fft import fft
import matplotlib.pyplot as plt

# Reference : https://ccrma.stanford.edu/~jos/mdft/mdft-python.html


# Parameters:
N = 64              # Must be a power of two
T = 1               # Set sampling rate to 1
A = 1               # Sinusoidal amplitude
phi = 0             # Sinusoidal phase
#f = 0.25            # Frequency (cycles/sample)
n = np.arange(N)    # Discrete time axis
#x = A*cos(2*pi*n*f*T+phi) # Sampled sinusoid
#X = fft(x)          # Spectrum
f = 0.25 + 0.5/N;    # Move frequency up 1/2 bin
x = cos(2*pi*n*f*T); # Signal to analyze
X = fft(x);          # Spectrum

plt.figure(figsize=(10,10))

# Plot time data:
plt.subplot(3,1,1)
plt.plot(n,x,'*k')        
ni = np.arange(0,N,0.1)   # Interpolated time axis
plt.plot(ni,A*cos(2*pi*ni*f*T+phi),'-k') 
plt.xlim(0,64)
plt.title('Sinusoid tuned NEAR 1/4 the Sampling Rate')
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
plt.xlabel('Normalized Frequency (cycles per sample))') 
plt.ylabel('Magnitude (Linear)')
plt.text(-.11,20,'b)')

# Same thing on a dB scale:
spec = 20*log10(magX) # Spectral magnitude in dB
plt.subplot(3,1,3)
plt.plot(fn,spec,'--ok')
plt.grid()
plt.xlim(0,1)
plt.ylim(-10, 30)
plt.xlabel('Normalized Frequency (cycles per sample))') 
plt.ylabel('Magnitude (dB)')
plt.text(-.11,30,'c)')

plt.show()

# Plot the periodic extension of the time-domain signal
plt.figure(figsize=(10,5))
plt.plot(np.concatenate([x,x]),'--ok')
plt.title('Time Waveform Repeated Once')
plt.xlabel('Time (samples)'); plt.ylabel('Amplitude')
plt.show()
