import cv2
import pickle
import numpy as np
import os

# Ganti indeks perangkat sesuai dengan kamera eksternal yang terhubung (DroidCam Source 3)
video = cv2.VideoCapture(1)  # Jika tidak berhasil, coba ganti ke 3 atau indeks yang sesuai
deteksi_wajah = cv2.CascadeClassifier('face ai project/data/wajah.xml')
data_wajah = []
i = 0

name = input("Masukan nama mu: ")

while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    muka = deteksi_wajah.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in muka:
        crop = frame[y:y + h, x:x + w, :]
        resize = cv2.resize(crop, (50, 50))
        if len(data_wajah) <= 100 and i % 10 == 0:
            data_wajah.append(resize)
        i = i + 1
        cv2.putText(frame, str(len(data_wajah)), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 225))
        cv2.rectangle(frame, (x, y), (x + w, y + h), (50, 50, 255), 1)
    cv2.imshow("Frame", frame)
    k = cv2.waitKey(1)
    if k == ord('q') or len(data_wajah) == 100:
        break
video.release()
cv2.destroyAllWindows()

data_wajah = np.asarray(data_wajah)
data_wajah = data_wajah.reshape(100, -1)

if 'names.pkl' not in os.listdir('face ai project/data'):
    names = [name] * 100
    with open('face ai project/data/nama.pkl', 'wb') as f:
        pickle.dump(names, f)
else:
    with open('face ai project/data/nama.pkl', 'rb') as f:
        names = pickle.load(f)
    names = names + [names] * 100
    with open('face ai project/data/nama.pkl', 'wb') as f:
        pickle.dump(names, f)

if 'wajah_names.pkl' not in os.listdir('face ai project/data'):
    with open('face ai project/data/wajah_nama.pkl', 'wb') as f:
        pickle.dump(data_wajah, f)
else:
    with open('face ai project/data/wajah_nama.pkl', 'rb') as f:
        muka = pickle.load(f)
    muka = np.append(muka, data_wajah, axis=0)
    with open('face ai project/data/wajah_nama.pkl', 'wb') as f:
        pickle.dump(muka, f)
