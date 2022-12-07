# Discrete Fourier Series
*&nbsp; A Fourier series is a summation of harmonically related sinusoidal functions, also known as components or harmonics. The result of the summation is a periodic function whose functional form is determined by the choices of cycle length (or period), the number of components, and their amplitudes and phase parameters.*

$$
f(t)=a_{0} + \sum_{n=1}^{\infty}a_{n} \cos{\frac{n \pi t}{l}} + b_{n} \sin{\frac{n \pi t}{l}} \tag{1}
$$

*&nbsp; In general, we usually use complex form to calculate the DFT of input siganl.*

$$
f[n] = \sum_{k= \langle N \rangle} c_{k} e^{j k 2 \pi f n} \tag{2}
$$

$$
c_{k} = \frac{1}{N}\sum_{n = \langle N \rangle} f[n] e^{-j k 2 \pi f n}
$$



## Sampling Theorem


$$
g_{\delta}(t) = g(t) * \sum_{n = \infty}^{\infty} \delta(t-nT_{s}) = \sum_{n = \infty}^{\infty}g(nT_{s}) \ \delta(t-nT_{s}) \tag{3}
$$

*&nbsp; Using 2 equation below.*

$$
\sum_{m = \infty}^{\infty} g(t-mT_{0}) \rightleftharpoons f_{0} \sum_{n = \infty}^{\infty} G(nf_{0}) \ \delta(f-nf_{0}) \tag{4}
$$

$$
\sum_{m = \infty}^{\infty} \delta(t-mT_{0}) \rightleftharpoons f_{0} \sum_{n = \infty}^{\infty} G(nf_{0}) \ \delta(f-nf_{0}) \tag{5}
$$


*&nbsp; We can get this equation:*

$$
g_{\delta}(t) \rightleftharpoons f_{s} \sum_{m = \infty}^{\infty} G(f-mf_{s}) \tag{6}
$$

*&nbsp; Taking discrete time Fourier transform of both sides of equation.*

$$
G_{\delta}(f) = \sum_{n = \infty}^{\infty} g(nT_{s}) \ exp(-j 2 \pi n f T_{s}) \tag{7}
$$

*&nbsp; Hence, under the follow two conditions:*

1. $G(f) = 0$ for $|f| \geq W$ (band-limited signal)
2. $f_{s} = 2W$ or $T_{s} = \frac{1}{2W}$

*&nbsp; Then,*

$$
G_{\delta}(f) = \sum_{n = \infty}^{\infty} g\Bigl(\frac{n}{2W}\Bigl) \ exp\Bigl(-j 2 \pi \frac{n}{2W} f\Bigl) \tag{9}
$$

$$
G_{\delta}(f) = f_{s}G(f) + f_{s}\sum_{m = \infty \\ m \neq 0}^{\infty} G(f-mf_{s}) \tag{10}
$$

*&nbsp; We find that*

$$
G(f) = \frac{1}{2W}G_{\delta}(f) \ , \ -W < f < W
$$

*&nbsp; Substituting, we may also write*

$$
G(f) = \frac{1}{2W} \sum_{n = \infty}^{\infty} g\Bigl(\frac{n}{2W}\Bigl) \ exp\Bigl(\frac{-j \pi n f}{W} \Bigl) \ , \ -W < f < W \tag{11}
$$


*&nbsp; Therefore, if the sample values of a signal g(t) are specified for all time, then the Fourier transform $G(f)$ of the signal is uniquely determined by using the discrete time Fourier transform. In the other words, the sequence $g(\frac{n}{2W})$ has all the information contained in $g(t)$.*

## Reconstruction the signal of $g(t)$

\begin{align}
g(t) &= \int_{-\infty}^{\infty} G(f) \ exp(j 2 \pi f t) \ df \\
&= \int_{-W}^{W} \frac{1}{2W} \sum_{n = \infty}^{\infty} g\Bigl(\frac{n}{2W}\Bigl) \ exp\Bigl(\frac{-j \pi n f}{W} \Bigl) \tag{12}
\end{align}

*&nbsp; Interchanging the order of summation and integration*

$$
g(t) = \sum_{n = \infty}^{\infty}  \ g\Bigl(\frac{n}{2W}\Bigl) \ \frac{1}{2W} \int_{-W}^{W}exp\Bigr[j 2 \pi f \Bigr(t - \frac{n}{2W} \Bigr)\Bigr] \ df \tag{13}
$$

*&nbsp; Then,*

\begin{align}
g(t) &= \sum_{n = \infty}^{\infty} g\Bigl(\frac{n}{2W}\Bigl) \ \frac{\sin{2 \pi W t}}{2 \pi W t - n \pi} \\
&= \sum_{n = \infty}^{\infty} g\Bigl(\frac{n}{2W}\Bigl) \ sinc(2Wt-n) \ , \ -\infty < t < \infty \tag{14}
\end{align}

*&nbsp; Eq.(14) provides an interpolation formula for reconstructing the original signal from the sequence of sample values $g(\frac{n}{2W})$, with the $sinc(2Wt)$ playing the role of an interpolation function.*

*&nbsp; Eq.(14) can be looked in another way: it represents the convolution (or filtering) of the impulse train $g_{\delta}(t)$ given by Eq.(3) with the impulse response $sinc(2Wt)$.*

*&nbsp; Any impulse response that plays the same roles as $sinc(2Wt)$ is also referred to as a reconstruction filter.*

*&nbsp; The sampling rate of $2W$ samples per second, for a signal bandwidth of $W$ Hz, is called the Nyquist rate; its reciprocal $\frac{1}{2W}$ (measured in seconds) is called __Nyquist interval__.*
