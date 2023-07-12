import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#Inside the while loop we define the HSV ranges (low_red, high_red)
#we create the mask and we show only the object with the red color
    
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    
    red = cv2.bitwise_and(frame, frame, mask=red_mask)
    
    konturlar = cv2.findContours(red_mask.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)[-2]

    if(len(konturlar) > 0):
        #en geniş alana sahip kontur
        engeniskontur = max(konturlar,key=cv2.contourArea)
        #En büyük konturun capı ve merkez pixel koordinatları
        ((x,y),radius) = cv2.minEnclosingCircle(engeniskontur)

        if radius > 5:
            #cember cizdirme
            cv2.circle(red,(int(x), int(y)), int(radius),(0, 255, 255), 2)

   
    cv2.imshow("Red", red)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
