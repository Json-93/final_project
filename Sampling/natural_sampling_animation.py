import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

plt.ion()
for fs in range(1, 100, 1):
    N = 512
    t = np.linspace(-1, 1, N)

    x1 = np.sin(2*np.pi*1*t)
    x2 = 0.5 * (signal.square(fs*np.pi*t) + 1)

    y1 = x1*x2

    plt.subplot(221), plt.plot(t, x1, 'blue')
    plt.xlabel('time')
    plt.title('sin wave')
    plt.grid(True)

    plt.subplot(222), plt.plot(t, x2, 'blue')
    plt.grid(True)
    plt.xlabel('time')
    plt.title('square wave')

    plt.subplot(223), plt.plot(t, y1, 'blue')
    plt.ylim(-1.1, 1.1)
    plt.grid(True)
    plt.xlabel('time')
    plt.title('natral sampling')

    n = np.arange(-1, 1, 1/N)
    y1_fft = np.abs(np.fft.fft(np.sin(2*np.pi*1*n) * 0.5 * (signal.square(fs*np.pi*n) + 1)))
    plt.subplot(224), plt.plot(n, y1_fft, 'blue')
    plt.xlabel('frequence')
    plt.title('freq of natral sampling')
    
    plt.show()
    plt.pause(0.5)
    plt.clf()
