import numpy as np
import matplotlib.pyplot as plt

import scipy
from scipy import signal

#----------------------------------------------------------------
plt.ion()
plt.figure(figsize=(10, 8))
for i in range(0, 200, 1):
    f = 20 # Hz
    t = np.linspace(0, 0.5, 200)
    x1 = np.sin(2 * np.pi * f * t)

    s_rate = 35 + i # Hz. Here the sampling frequency is less than the requirement of sampling theorem

    T = 1 / s_rate
    n = np.arange(0, 0.5 / T)
    nT = n * T
    x2 = np.sin(2 * np.pi * f * nT) # Since for sampling t = nT.

    freq = np.fft.fftfreq(nT.size)
    freq = np.fft.fftshift(freq)
    x2fft = np.fft.fft(x2)
    
    
    plt.suptitle("Sampling a Sine Wave of Fmax=20Hz with fs=35Hz", fontsize=20)

    plt.subplot(2, 2, 1)
    plt.plot(t, x1, linewidth=3, label='SineWave of frequency 20 Hz')
    plt.xlabel('time.', fontsize=15)
    plt.ylabel('Amplitude', fontsize=15)
    plt.legend(fontsize=10, loc='upper right')

    # plt.subplot(2, 2, 2)
    # plt.plot(nT, x2, 'ro', label=f'fs= {s_rate} Hz')
    # plt.xlabel('time.', fontsize=15)
    # plt.ylabel('Amplitude', fontsize=15)
    # plt.legend(fontsize=10, loc='upper right')

    plt.subplot(2, 2, 2)
    plt.plot(freq, x2fft, label=f'fs= {s_rate} Hz')
    plt.xlabel('time.', fontsize=15)
    plt.ylabel('Amplitude', fontsize=15)
    plt.legend(fontsize=10, loc='upper right')

    plt.subplot(2, 2, 3)
    plt.stem(nT, x2, 'm', label=f'fs= {s_rate} Hz')
    plt.xlabel('time.', fontsize=15)
    plt.ylabel('Amplitude', fontsize=15)
    plt.legend(fontsize=10, loc='upper right')

    plt.subplot(2, 2, 4)
    plt.plot(nT, x2, 'g-', label='Reconstructed Sine Wave')
    plt.xlabel('time.', fontsize=15)
    plt.ylabel('Amplitude', fontsize=15)
    plt.legend(fontsize=10, loc='upper right')

    plt.tight_layout()
    plt.show(block= False)
    plt.pause(0.005)
    plt.clf()  
