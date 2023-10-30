import cv2
import mediapipe as mp

# Inisialisasi modul wajah dari Mediapipe
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# Buka kamera
cap = cv2.VideoCapture(1)

# Membaca kamera dan mendeteksi wajah
with mp_face_detection.FaceDetection(
    min_detection_confidence=0.5) as face_detection:

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Kamera tidak ditemukan")
            break

        # Ubah warna gambar ke BGR
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Deteksi wajah
        results = face_detection.process(image_rgb)

        # Gambar kotak deteksi wajah
        if results.detections:
            for detection in results.detections:
                mp_drawing.draw_detection(image, detection)

        cv2.imshow('Face Detection', image)
        if cv2.waitKey(5) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
