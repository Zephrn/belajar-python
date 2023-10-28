# from Crypto.Cipher import AES
# from Crypto.Random import get_random_bytes
# from Crypto.Util.Padding import pad, unpad

# # Fungsi untuk mengenkripsi string
# def encrypt_string_to_AES(plain_text, key):
#     cipher = AES.new(key, AES.MODE_CBC)
#     cipher_text = cipher.encrypt(pad(plain_text.encode(), AES.block_size))
#     return cipher.iv + cipher_text

# # Fungsi untuk mendekripsi string
# def decrypt_string_from_AES(cipher_text, key):
#     iv = cipher_text[:AES.block_size]
#     cipher = AES.new(key, AES.MODE_CBC, iv)
#     decrypted_text = unpad(cipher.decrypt(cipher_text[AES.block_size:]), AES.block_size)
#     return decrypted_text.decode()

# # Contoh pemanggilan fungsi
# key = get_random_bytes(16)  # Kunci acak 16 byte (untuk keperluan demonstrasi)
# plain_text = input()  # Ganti dengan string yang ingin Anda enkripsi
# cipher_text = encrypt_string_to_AES(plain_text, key)
# print(f"Cipher Text: {cipher_text}")
# decrypted_text = decrypt_string_from_AES(cipher_text, key)
# print(f"Decrypted Text: {decrypted_text}")
