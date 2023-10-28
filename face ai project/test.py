from sklearn.neighbors import KNeighborsClassifier
import cv2
import pickle
import numpy as np
import os
video = cv2.VideoCapture(1)
deteksi_wajah=cv2.CascadeClassifier('face ai project/data/wajah.xml')

with open('face ai project/data/nama.pkl', 'rb') as f:
        LABELS=pickle.load(f)
with open('face ai project/data/wajah_nama.pkl', 'rb') as f:
        MUKA=pickle.load(f)


knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(MUKA, LABELS)



while True:
    ret,frame=video.read()
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    muka=deteksi_wajah.detectMultiScale(gray, 1.3 ,5)
    for(x,y,w,h) in muka:
        crop=frame[y:y+h, x:x+w, :]
        resize=cv2.resize(crop, (50,50)).flatten().reshape(1,-1)
        output=knn.predict(resize)
        cv2.putText(frame, str(output[0]), (x,y-15), cv2.FONT_HERSHEY_COMPLEX, 1, (51,153,255), 1,)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (50,50,255), 1)
    cv2.imshow("Frame",frame)
    k=cv2.waitKey(1)
    if k==ord('q'):
        break
video.release()
cv2.destroyAllWindows()





