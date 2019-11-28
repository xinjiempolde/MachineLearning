from scipy import signal
import numpy as np
import cv2

conv2 = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
im = cv2.imread('animal2.jpg')
print(im.shape)
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
gray = cv2.filter2D(gray, -1, conv2)
cv2.imshow('g', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
