import cv2
import numpy as np
import matplotlib.pyplot as plt
# Feature Matching (homography) Brute Force

img1 = cv2.imread('opencv-feature-matching-template.jpg',1)
img2 = cv2.imread('opencv-feature-matching-image.jpg',1)

orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True )

matches = bf.match (des1, des2)
matches = sorted(matches, key= lambda x:x.distance)

img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:13], None , flags=2)
# you can test with change the matches cont
plt.imshow(img3)
plt.show()
