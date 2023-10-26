import socket
import cv2

# Fungsi untuk mengambil gambar dari webcam dan mengirim datanya melalui socket
def capture_and_send(sock):
    cap = cv2.VideoCapture(0)  # Mengakses kamera utama

    while True:
        ret, frame = cap.read()  # Membaca satu frame

        # Mengubah gambar menjadi bentuk byte
        data = cv2.imencode('.jpg', frame)[1].tobytes()

        # Mengirim data gambar melalui socket
        sock.sendall(data)

        # Mengatur kondisi untuk menghentikan loop
        key = cv2.waitKey(1)
        if key == ord('q'):  # Tekan 'q' untuk keluar dari loop
            break

    cap.release()
    cv2.destroyAllWindows()

# Buat koneksi socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Ganti alamat IP dan port dengan informasi yang diberikan oleh ngrok
    ngrok_address = '6.tcp.ngrok.io'  # Ganti dengan alamat ngrok yang sesuai
    ngrok_port = 13005  # Ganti dengan port ngrok yang sesuai

    # Melakukan koneksi dengan alamat ngrok yang disediakan
    sock.connect((ngrok_address, ngrok_port))
    capture_and_send(sock)
except ConnectionRefusedError:
    print("Koneksi ditolak. Pastikan server telah dijalankan.")
except Exception as e:
    print(f"Terjadi kesalahan: {e}")
finally:
    sock.close()
