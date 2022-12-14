import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("image/20180816-Au_Si(111)-12min Au-RT, table float,Lock-in off,--34_2.jpg", 0)

dft = cv.dft(np.float32(img), flags = cv.DFT_COMPLEX_OUTPUT) 
dft_shift = np.fft.fftshift(dft) 
magnitude_spectrum = 20*np.log(cv.magnitude(dft_shift[:,:,0],dft_shift[:,:,1])) 

fshift = dft_shift
fshift_mask_mag = 20 * np.log(cv.magnitude(fshift[:, :, 0], fshift[:, :, 1]))
f_ishift = np.fft.ifftshift(fshift) 
img_back = cv.idft(f_ishift)
img_back = cv.magnitude(img_back[:, :, 0], img_back[:, :, 1])

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('FFT Image'), plt.xticks([]), plt.yticks([])
plt.show()