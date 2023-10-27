import socket
import cv2
import numpy as np
import geocoder

def capture_and_send(sock):
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        # Mengubah gambar menjadi bentuk byte
        data = cv2.imencode('.jpg', frame)[1].tobytes()

        # Mendapatkan lokasi
        g = geocoder.ip('me')
        location = g.latlng

        # Mengonversi lokasi menjadi string
        location_str = f"{location[0]}, {location[1]}"

        # Mengirim data gambar dan lokasi melalui socket
        message = location_str.encode() + b' ' + data
        sock.sendall(message)

        # Mengatur kondisi untuk menghentikan loop
        key = cv2.waitKey(1)
        if key == ord('q'):  
            break

    cap.release()
    cv2.destroyAllWindows()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect(('192.168.1.3', 4444))
    capture_and_send(sock)
except ConnectionRefusedError:
    print("Koneksi ditolak. Pastikan server telah dijalankan.")
except Exception as e:
    print(f"Terjadi kesalahan: {e}")
finally:
    sock.close()
