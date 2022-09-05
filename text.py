import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img , "sun" , (20 , 300) , cv2.FONT_HERSHEY_COMPLEX , 2 , (0 , 255 , 0) , 3)
cv2.putText(img , "mercury" , (100 , 200) , cv2.FONT_HERSHEY_COMPLEX , 0.5 , (0 , 255 , 0) , 2)
cv2.putText(img , "venus" , (200 , 200) , cv2.FONT_HERSHEY_COMPLEX , 0.5 , (0 , 255 , 0) , 2)
cv2.putText(img , "earth" , (300 , 200) , cv2.FONT_HERSHEY_COMPLEX , 0.5 , (0 , 255 , 0) , 2)
cv2.putText(img , "mars" , (400 , 200) , cv2.FONT_HERSHEY_COMPLEX , 0.5 , (0 , 255 , 0) , 2)
cv2.putText(img , "jupitor" , (500 , 200) , cv2.FONT_HERSHEY_COMPLEX , 0.5 , (0 , 255 , 0) , 2)
cv2.putText(img , "saturn" , (800 , 200) , cv2.FONT_HERSHEY_COMPLEX , 0.5 , (0 , 255 , 0) , 2)
cv2.putText(img , "uranus" , (1000 , 200) , cv2.FONT_HERSHEY_COMPLEX , 0.5 , (0 , 255 , 0) , 2)
cv2.putText(img , "neptune" , (1100 , 200) , cv2.FONT_HERSHEY_COMPLEX , 0.5 , (0 , 255 , 0) , 2)



cv2.imshow("img" , img)



cv2.waitKey(0)