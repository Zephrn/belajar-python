import socket
import numpy as np
import cv2

# Buat koneksi socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('192.168.1.3', 4444))  # Mengikat socket ke alamat dan port tertentu
sock.listen(5)  # Mendengarkan koneksi masuk

print("Menunggu koneksi...")

# Menerima koneksi
conn, addr = sock.accept()
print("Terhubung dengan ", addr)

# Menerima data gambar dari socket
data = b''
while True:
    packet = conn.recv(4096)
    if not packet:
        break
    data += packet

# Menyimpan data gambar sebagai file JPG
with open("received_image.jpg", 'wb') as img_file:
    img_file.write(data)

# Mendekode gambar dan menampilkannya
img = cv2.imread('received_image.jpg')
cv2.imshow('Received Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Menutup koneksi
conn.close()
sock.close()
