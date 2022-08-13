# Gerekli kütüphaneler
import cv2
import time
import os
import datetime


# Birden fazla kamera kullanılabilir. Ben id si 1 olan kamerayı kullandım.
# Kameranın id si 0 olan kamerayı kullanmak istiyorsanız, 0 yapın.
CAMERAID = 1

# Dosyanın hangi konuma kaydedileceğini belirtir.
PATH = ''

# Dosyanın isimlendirme şeklidir. Bence dokunmayın
NAMING = '%Y-%m-%d--%H-%M-%S'

# Dosyanın uzantısıdır. '.png' olarak değiştirebilirsiniz.
EXTENSION = '.jpg'

# Kaç saniyede bir çekileceğini belirtir.
INTERVAL = 5


# Fotoğraf çekip kaydetme fonksiyonu
def capture_image() -> None:
    cap = cv2.VideoCapture(CAMERAID)
    ret, frame = cap.read()

    # Kare yakalandıktan sonra kameranın hemen kapatılmasını sağlar.
    cap.release()

    if ret and frame is not None:
        image_name = datetime.datetime.today().strftime(NAMING) + EXTENSION
        cv2.imwrite(os.path.join(PATH, image_name), frame)


# Fotoğraf çekip kaydettikten sonra INTERVAL saniye bekleyen döngü
while True:
    capture_image()
    time.sleep(INTERVAL)
