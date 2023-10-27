import socket
import time

def connection():
    while True:
        time.sleep(15)
        try:
                s.connect(('172.17.0.1', 4444))
                s.close()
                break
        except:
             connection()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection()