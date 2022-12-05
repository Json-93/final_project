# Final Project
## Discrete Fourier Series
*&nbsp; A Fourier series is a summation of harmonically related sinusoidal functions, also known as components or harmonics. The result of the summation is a periodic function whose functional form is determined by the choices of cycle length (or period), the number of components, and their amplitudes and phase parameters.*

$$f(t)=a_{0} + \sum_{n=1}^{\infty}a_{n} \cos{\frac{n \pi t}{l}} + b_{n} \sin{\frac{n \pi t}{l}}$$

*&nbsp; In general, we usually use complex form to calculate the DFT of input siganl.*

$$f[n] = \sum_{k= \langle N \rangle} c_{k} e^{j k 2 \pi f n}$$

$$c_{k} = \frac{1}{N}\sum_{n = \langle N \rangle} f[n] e^{-j k 2 \pi f n}$$
