import matplotlib.pyplot as plt
# %matplotlib inline
import numpy as np
import cv2

img1 = cv2.imread("sze.jpg")
img1 = img1[:,:,::-1]
plt.imshow(img1)
plt.show()

kernel2 = np.ones((5, 5), np.float32) / 25
print(kernel2)

img2 = img1[:, 150:450, :] # kivágás a kettőspont operátorral
kernel3 = np.ones((6, 6),np.float32) / 36
kernel4 = np.ones((12, 12),np.float32) / 144
img3 = cv2.filter2D(img2, -1, kernel3)
img4 = cv2.filter2D(img2, -1, kernel4)

plt.subplot(131),plt.imshow(img2),plt.title('Eredeti')
plt.subplot(132),plt.imshow(img3),plt.title('6  x 6')
plt.subplot(133),plt.imshow(img4),plt.title('12 x 12')
plt.show()


kernel5 = np.ones((3, 3),np.float32) * - 1
kernel5[1][1] = 8
kernel5 = np.ones((3, 3),np.float32) * - 1
kernel5[1][1] = 8
# kernel5 = kernel5 / 2
kernel6 = np.matrix('0 1 0; 1 -4 1; 0 1 0')

img5 = cv2.filter2D(img2, -1, kernel5)
img6 = cv2.filter2D(img2, -1, kernel6)


plt.subplot(131),plt.imshow(img2),plt.title('Eredeti')
plt.subplot(132),plt.imshow(img5),plt.title('K5')
plt.subplot(133),plt.imshow(img6),plt.title('K6')
plt.show()

#
#kernel5 = np.ones((3, 3),np.float32) * - 1
#kernel5[1][1] = 8
#kernel5 = kernel5 * 4
#r11 = cv2.imread("road01.png")
#r11 = r11[:,:,::-1]
#r12 = cv2.filter2D(r11, -1, kernel5)
#plt.imshow(r11)
#plt.show()
#plt.imshow(r12)
#plt.show()
## print(kernel5)
#
#
#
#kernel5 = np.ones((3, 3),np.float32) * - 1
#kernel5[1][1] = 8
#kernel5 = kernel5 * 4
#r21 = cv2.imread("road02.png")
#r21 = r21[:,:,::-1]
#r22 = cv2.filter2D(r21, -1, kernel5)
#plt.imshow(r21)
#plt.show()
#plt.imshow(r22)
#plt.show()
## print(kernel5)
#kernel5 = np.ones((3, 3),np.float32) * - 1
#kernel5[1][1] = 8
#kernel5 = kernel5 * 4
#r21 = cv2.imread("road02.png")
#r21 = r21[:,:,::-1]
#r22 = cv2.filter2D(r21, -1, kernel5)
#plt.imshow(r21)
#plt.show()
#plt.imshow(r22)
#plt.show()
## print(kernel5)
