from modules import crypto
import cv2 as cv
import os

# filename = './images/lena_cor.jpg'
# assert os.path.isfile(filename)

lena = cv.imread('./images/lena_cor.jpg')
lena_pgm = cv.imread('./images/lena.pgm', -1)

# cv.imshow("image", lena)
# cv.imshow("image 2", lena_pgm)
# cv.waitKey()
# print(lena[0][0])

