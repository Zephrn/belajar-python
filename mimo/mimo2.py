import mediapipe as mp
import cv2
import pickle
import numpy as np

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# Buka kamera
cap = cv2.VideoCapture(0)

# Load data wajah yang sudah dikenali
with open('known_faces_data.pkl', 'rb') as f:
    known_face_data = pickle.load(f)
    known_face_encodings = known_face_data['encodings']
    known_face_names = known_face_data['names']

# Inisialisasi mediapipe untuk deteksi wajah
with mp_face_detection.FaceDetection(min_detection_confidence=0.5) as face_detection:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Kamera tidak ditemukan")
            break

        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = face_detection.process(image_rgb)

        if results.detections:
            for detection in results.detections:
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, _ = image.shape
                bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                       int(bboxC.width * iw), int(bboxC.height * ih)

                # Mendapatkan encoding wajah
                face_image = image[bbox[1]:bbox[1] + bbox[3], bbox[0]:bbox[0] + bbox[2]]

                # Perbandingan dengan wajah yang dikenal
                known_face_encodings_np = np.array(known_face_encodings)
                face_match = np.linalg.norm(known_face_encodings_np - face_image, axis=1)
                name = known_face_names[np.argmin(face_match)]

                cv2.rectangle(image, (bbox[0], bbox[1]), (bbox[0] + bbox[2], bbox[1] + bbox[3]), (0, 255, 0), 2)
                cv2.putText(image, name, (bbox[0], bbox[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

        cv2.imshow('Face Recognition', image)
        if cv2.waitKey(5) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
