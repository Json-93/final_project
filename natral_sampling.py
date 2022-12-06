import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

N = 1024
t = np.linspace(-1, 1, N)

# def rect(x):
#     return np.where(np.abs(x)<=0.5, 1, -1)

x1 = np.sin(2*np.pi*1*t)
x2 = 0.5 * (signal.square(50*np.pi*1*t) + 1)

y1 = x1*x2

plt.subplot(411), plt.plot(t, x1, 'blue')
plt.grid(True)
plt.subplot(412), plt.plot(t, x2, 'blue')
plt.grid(True)
plt.subplot(413), plt.plot(t, y1, 'blue')
plt.grid(True)


n = np.arange(-1, 1, 1/N)
y1_fft = np.abs(np.fft.fft(np.sin(2*np.pi*1*n) * 0.5 * (signal.square(50*np.pi*1*n) + 1)))
plt.subplot(414), plt.plot(n, y1_fft, 'blue')
plt.show()
