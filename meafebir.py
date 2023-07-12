import cv2             #kütüphaneleri kur
import numpy as np
 
Known_distance = 22    # kameradan objeye(yüz) bilinen uzaklık (cm)  = measured_distance
Known_width = 3        # gerçek hayatta yüzün genişliği (cm)         = real_width
width_frame=0

GREEN = (0, 255, 0) 
RED = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
  
fonts = cv2.FONT_HERSHEY_COMPLEX         # font belirleme
 
def Focal_Length_Finder(measured_distance, real_width, width):            # odak uzunluğu bulan fonk.

    focal_length = (width * measured_distance) / real_width
    return focal_length
   
def Distance_finder(Focal_Length, real_face_width, width_frame):          # mesafeyi hesaplayan fonk.
  
    distance = (real_face_width * Focal_Length)/width_frame
    return distance
       
#DOMATES REFERANS FOTO
#domatesin referans fotosundaki kapladığı px genişliği FOTO ÜZERİNDEN DOMATES TESPİT EDİLECEK.
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
        width= radius*2
        #print(width)  #DOMATES GENİŞLİĞİ
   
cv2.imshow("Red", red)
  
Focal_length_found = Focal_Length_Finder(Known_distance, Known_width, width)  # face width in reference(pixe) REFERANS FOTOSU İÇİN  ODAK UZUNLUĞU
  
print(Focal_length_found)   #odak uzunluğu yazdır        #GEREK YOK
  
cap = cv2.VideoCapture(0)              # video başlat    #GEREK YOK!!!!!
   
while True:
  
    # kameradan frame okuma
    _, frame = cap.read()
  
    # calling face_data function to find
    # the width of face(pixels) in the frame
    

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#Inside the while loop we define the HSV ranges (low_red, high_red)
#we create the mask and we show only the object with the red color
    
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    
    red = cv2.bitwise_and(frame, frame, mask=red_mask)
    
    konturlar = cv2.findContours(red_mask.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)[-2]

    if(len(konturlar) > 4):
        #en geniş alana sahip kontur
        engeniskontur = max(konturlar,key=cv2.contourArea)
        #En büyük konturun capı ve merkez pixel koordinatları
        ((x,y),radius) = cv2.minEnclosingCircle(engeniskontur)

        if radius > 4:
            #cember cizdirme
            cv2.circle(red,(int(x), int(y)), int(radius),(0, 255, 255), 2)
            width_frame=radius*2

    cv2.imshow("Red", red)

    
  
    # check if the face is zero then not 
    # find the distance
    if width_frame != 0:      #yapılacakkkkkkk!!!!!!!!!!!!!!!!!!!!!!!!1 
        
        # mesafe fonk çağırılır 
        Distance = Distance_finder(Focal_length_found, Known_width, width_frame) #mesafe fonk.
  
        # draw line as background of text
        cv2.line(frame, (30, 30), (230, 30), RED, 32) 
        cv2.line(frame, (30, 30), (230, 30), BLACK, 28)
  
        # ekrana  uzaklık yazdır
        cv2.putText(frame, f"Distance: {round(Distance,2)} CM", (30, 35),fonts, 0.6, GREEN, 2)
  
    # frame göster
    cv2.imshow("frame", frame)
  
    # q basarsak programdan çık
    if cv2.waitKey(1) == ord("q"):
        break
  
cap.release()

cv2.destroyAllWindows()