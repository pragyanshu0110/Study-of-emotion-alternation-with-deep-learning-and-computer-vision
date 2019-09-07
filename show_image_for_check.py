'''open a image via image viewer '''

import cv2
import time

img=cv2.imread('test_image.jpeg')
cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
cv2.imshow("window", img)
cv2.waitKey(30000)   # image will colose after 20 seconds

