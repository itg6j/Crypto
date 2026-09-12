import cv2
import numpy as np

image1 = cv2.imread('flag.png')
image2 = cv2.imread('lemur.png')
dest_xor = cv2.bitwise_xor(image1, image2, mask=None)
cv2.imshow('Bitwise XOR', dest_xor)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
