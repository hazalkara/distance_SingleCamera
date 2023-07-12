import cv2             #kütüphaneleri kur
  
Known_distance = 50  # kameradan objeye(yüz) bilinen uzaklık (cm)
  
Known_width = 14.3     # gerçek hayatta yüzün genişliği (cm)
 
GREEN = (0, 255, 0)
RED = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
  
fonts = cv2.FONT_HERSHEY_COMPLEX   # font belirleme
  
face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")       # yüz tesipt
  
def Focal_Length_Finder(measured_distance, real_width, width_in_rf_image):         # odak uzunluğu bulan fonksiyon

    focal_length = (width_in_rf_image * measured_distance) / real_width
    return focal_length
   
def Distance_finder(Focal_Length, real_face_width, face_width_in_frame):           # mesafeyi hesaplayan fonk.
  
    distance = (real_face_width * Focal_Length)/face_width_in_frame
    return distance

def face_data(image):
    face_width = 0  # yüz genişliği 0 yapıldı
  
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)          # görüntü gri ölçeklemeye çevirdik
  
    faces = face_detector.detectMultiScale(gray_image, 1.3, 5)    # yüzü tespit etme
  
    for (x, y, h, w) in faces:                # koordinatları al  x, y , genişlik and yükseklik
        
        cv2.rectangle(image, (x, y), (x+w, y+h), GREEN, 2)     # yüzün kenarını çiz yeşil ile
        face_width = w             # yüz genişliği pixel cinsenden hesapla
        
    return face_width             # yüz genişliğini pixel cinsinden döndür
  
  
ref_image = cv2.imread("Ref_image.png")         # ref fotoyu oku
  
ref_image_face_width = face_data(ref_image)     # referance_imageden yüz genişliği(pixel)  bul

Focal_length_found = Focal_Length_Finder(       # odak uzunluğu bulan fonk çağır "Focal_Length_Finder"

    Known_distance, Known_width, ref_image_face_width)  # face width in reference(pixel)
  
print(Focal_length_found)   #odak uzunluğu yazdır
  
cv2.imshow("ref_image", ref_image)     # ref im göster
cap = cv2.VideoCapture(0)              # video başlat 
  
while True:
  
    # kameradan frame okuma
    _, frame = cap.read()
  
    # calling face_data function to find
    # the width of face(pixels) in the frame
    face_width_in_frame = face_data(frame)
  
    # check if the face is zero then not 
    # find the distance
    if face_width_in_frame != 0:
        
        # mesafe fonk çağırılır 
        Distance = Distance_finder(
            Focal_length_found, Known_width, face_width_in_frame)
  
        # draw line as background of text
        cv2.line(frame, (30, 30), (230, 30), RED, 32)
        cv2.line(frame, (30, 30), (230, 30), BLACK, 28)
  
        # ekrana  uzaklık yazdır
        cv2.putText(
            frame, f"Distance: {round(Distance,2)} CM", (30, 35), 
          fonts, 0.6, GREEN, 2)
  
    # frame göster
    cv2.imshow("frame", frame)
  
    # q basarsak programdan çık
    if cv2.waitKey(1) == ord("q"):
        break
  
cap.release()

cv2.destroyAllWindows()
