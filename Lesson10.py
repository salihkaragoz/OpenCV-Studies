import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize = 5)
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0,1, ksize =5)
    edges = cv2.Canny(frame , 100, 200 )
    
    cv2.imshow('origignal', frame)
    cv2.imshow('laplacian' , laplacian)
    cv2.imshow('laacian' , sobelx)
    cv2.imshow('lapl' , sobely)
    cv2.imshow('edgesü' , edges)
    
    
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

    

cv2.destroyAllWindows()
cap.release()
