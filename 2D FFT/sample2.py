import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("image/20180816-Au_Si(111)-12min Au-RT, table float,Lock-in off,--34_2.jpg", 0)

dft = cv.dft(np.float32(img), flags = cv.DFT_COMPLEX_OUTPUT) 
dft_shift = np.fft.fftshift(dft) 
magnitude_spectrum = 20*np.log(cv.magnitude(dft_shift[:,:,0],dft_shift[:,:,1])) 

# ------------------------------------------------------------------------------------------
crop = img[106:406, 106:406]

crop_dft = cv.dft(np.float32(crop), flags = cv.DFT_COMPLEX_OUTPUT) 
crop_dft_shift = np.fft.fftshift(crop_dft) 
crop_magnitude_spectrum = 20*np.log(cv.magnitude(crop_dft_shift[:,:,0], crop_dft_shift[:,:,1])) 


# ------------------------------------------------------------------------------------------
rows, cols = img.shape
crow, ccol = int(rows / 2), int(cols / 2)

mask = np.zeros((rows, cols, 2), np.uint8)
r1 = 220
r2 = 50
center = [crow, ccol]
x, y = np.ogrid[:rows, :cols]
# mask_area1 = (x - center[0]) ** 2 + (y - center[1]) ** 2 >= r1*r1
mask_area2 = (x - center[0]) ** 2 + (y - center[1]) ** 2 <= r2*r2
# mask[mask_area1] = 1
mask[mask_area2] = 1

# apply mask and inverse DFT
crop_mask_fshift = dft_shift * mask
crop_mask_magnitude = 20 * np.log(cv.magnitude(crop_mask_fshift[:, :, 0], crop_mask_fshift[:, :, 1]))
crop_mask_f_ishift = np.fft.ifftshift(crop_mask_fshift) # 將移動到中心的資料先移動回左上角，這樣才會是正確的
img_back = cv.idft(crop_mask_f_ishift)
img_back = cv.magnitude(img_back[:, :, 0], img_back[:, :, 1]) # 資料還是複數，扔需用 cv.magnitude()顯示出振福



# ------------------------------------------------------------------------------------------
plt.subplot(3,2,1), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])

plt.subplot(3,2,2), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('FFT Image'), plt.xticks([]), plt.yticks([])

plt.subplot(3,2,3), plt.imshow(crop, cmap='gray')
plt.title('FFT'), plt.xticks([]), plt.yticks([])

plt.subplot(3,2,4), plt.imshow(crop_magnitude_spectrum, cmap='gray')
plt.title('Inverse FFT'), plt.xticks([]), plt.yticks([])

plt.subplot(3,2,5), plt.imshow(crop_mask_magnitude, cmap='gray')
plt.title('crop + mask on freq domain'), plt.xticks([]), plt.yticks([])

plt.subplot(3,2,6), plt.imshow(img_back, cmap='gray')
plt.title('crop + mask inverse fft'), plt.xticks([]), plt.yticks([])

plt.show()