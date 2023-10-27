import hashlib

def encrypt_string_to_md5(string):
    # Konversi string ke byte sebelum melakukan enkripsi MD5
    byte_string = string.encode('utf-8')

    # Buat objek hash MD5
    hash_object = hashlib.md5()

    # Perbarui objek hash dengan byte string
    hash_object.update(byte_string)

    # Ambil nilai hex dari hash
    encrypted_string = hash_object.hexdigest()
    
    return encrypted_string

# Contoh pemanggilan fungsi
string = str(input("masukan yang ingin di enskripsi ke md5 : ")) # Ganti dengan string yang ingin Anda enkripsi
encrypted_string = encrypt_string_to_md5(string)
print(f"String Asli: {string}")
print(f"Hasil Enkripsi MD5: {encrypted_string}")
