import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

# Input signal configuration
def signal(t, f):
    """
    amp : amplitude
    t : time
    """

    fn = np.cos(2 * np.pi * f * t)

    return fn

f = 20 # Hz
x = np.linspace(-1, 1, 500)
y1 = signal(x, f)

s_rate = 35 # Hz. Here is the sampling rate.
T = 1 / s_rate
n = np.arange(-s_rate, s_rate)
nT = n * T
y2 = signal(nT, f)


# Sampling
# part
dt = 0.005
yf = np.fft.fft(y2)
freq = np.fft.fftfreq(nT.size, d= dt)
freq = np.fft.fftshift(freq)

# display the signal and spectrum
fig, ax = plt.subplots(2)
line0, = ax[0].plot(x, y1, 'red')
line1, = ax[0].plot(nT, y2, '.')
ax[0].set_xlabel('Time')
fig.subplots_adjust(left= 0.25, bottom= 0.25)

line2, = ax[1].plot(freq, yf.imag)
ax[1].set_xlabel('Frequency')
ax[1].set_ylim(-10, 100)
fig.subplots_adjust(left= 0.25, bottom= 0.25)


# Sampling rate slider configuration
axsmaplingrate = fig.add_axes([0.25, 0.1, 0.65, 0.03])
samplingrate_slider = Slider(
    ax = axsmaplingrate,
    label= 'S_rate',
    valmin= 10,
    valmax= 200,
    valinit= s_rate,
)

# update functioon configuration
def update1(val):
    s_rate = val # Hz. Here is the sampling rate.
    T = 1 / s_rate
    n = np.arange(-s_rate, s_rate)
    nT = n * T
    y2 = signal(nT, f)

    line1.set_xdata(nT)
    line1.set_ydata(y2)

    fig.canvas.draw_idle()

samplingrate_slider.on_changed(update1)

def update2(val):
    s_rate = val # Hz. Here is the sampling rate.
    T = 1 / s_rate
    n = np.arange(-s_rate, s_rate)
    nT = n * T
    y2 = signal(nT, f)

    
    yf = np.fft.fft(y2)
    freq = np.fft.fftfreq(nT.size, d= dt)
    freq = np.fft.fftshift(freq)

    line2.set_xdata(freq)
    line2.set_ydata(yf)

    fig.canvas.draw_idle()

samplingrate_slider.on_changed(update2)


# Setup reset function
resetax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, "reset", hovercolor= '0.975')

def reset(event):
    samplingrate_slider.reset()

button.on_clicked(reset)

plt.show()


plt.show()
