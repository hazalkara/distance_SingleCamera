# CSI Kamera ile Mesafe ve Nesne Tespiti

Bu Python uygulaması, kamera görüntüsünden nesnelerin gerçek dünyadaki mesafelerini hesaplamak ve kırmızı nesneleri tespit etmek için kullanılır. Aşağıda, uygulamanın önemli bölümleri ve nasıl kullanılacağı açıklanmıştır.

## Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki Python kütüphanelerine ihtiyacınız vardır:

- OpenCV (`cv2`)
- NumPy

Bu kütüphaneleri yüklemek için şu komutları kullanabilirsiniz:

```bash
pip install opencv-python numpy
```

## Mesafe ve Odak Uzunluğu Hesaplama
Kod, kameradan nesneye olan bilinen mesafeyi (Known_distance) ve nesnenin gerçek dünyadaki genişliğini (Known_width) kullanarak odak uzunluğunu (Focal_Length_Finder) hesaplar.

```bash
Focal_length_found = Focal_Length_Finder(Known_distance, Known_width, width)
```
## Kırmızı Nesne Tespiti
Kod, belirli bir renk aralığına karşılık gelen nesneleri tespit etmek için kamera görüntüsünü kullanır. Bu örnekte, kırmızı renge odaklanılmıştır.
```bash
# Kırmızı rengi belirlemek için HSV aralığı
low_red = np.array([161, 155, 84])
high_red = np.array([179, 255, 255])

red_mask = cv2.inRange(hsv_frame, low_red, high_red)
```
## Gerçek Dünyadaki Mesafe Hesaplama
Kırmızı bir nesne tespit edildiğinde, nesnenin genişliği (width_frame) hesaplanır ve odak uzunluğu kullanılarak nesnenin gerçek dünyadaki mesafesi (Distance) hesaplanır.
```bash
Focal_length_found = Focal_Length_Finder(Known_distance, Known_width, width)
```
## Uygulamayı Çalıştırma
Uygulamayı çalıştırmak için kamera cihazınıza erişim sağladığınızdan emin olun ve 'meafebir.py' dosyasını çalıştırın. Kamera görüntüsü üzerinde kırmızı bir nesne bulunmalıdır. Bu nesne, gerçek dünyadaki mesafesi ekranda görüntülenecektir.
