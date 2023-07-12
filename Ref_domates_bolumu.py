import cv2
import numpy as np


ref_imag = cv2.imread("b.jpg")
hsv_frame = cv2.cvtColor(ref_imag, cv2.COLOR_BGR2HSV)
    
low_red = np.array([161, 155, 84])
high_red = np.array([179, 255, 255])
    
red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    
red = cv2.bitwise_and(ref_imag, ref_imag, mask=red_mask)
    
konturlar = cv2.findContours(red_mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
        

if(len(konturlar) > 0):
    #en geniş alana sahip kontur
    engeniskontur = max(konturlar,key=cv2.contourArea)
    #En büyük konturun capı ve merkez pixel koordinatları
    ((x,y),radius) = cv2.minEnclosingCircle(engeniskontur)

    if radius > 0:
        #cember cizdirme
        cv2.circle(red,(int(x), int(y)), int(radius),(0, 255, 255), 2)
        width= radius
        #print(width)  #DOMATES GENİŞLİĞİ


   
cv2.imshow("Red", red)
cv2.waitKey(0) 
  
cv2.destroyAllWindows()