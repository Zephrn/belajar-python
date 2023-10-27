import hashlib
import random
import rahasia

abjad = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
abjad = [letter.lower() for letter in abjad]

kunci = random.randint(1, 100)
key = kunci
kalimat = "nxh pvagn xnzh >//<"

if key == rahasia.KB:
    print("Kamu telah menemukan deskripsi nya!")

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

def enkripsi(kalimat, key):
    hasil_enkripsi = ""
    for karakter in kalimat:
        if karakter in abjad:
            index_lama = abjad.index(karakter)
            index_baru = (index_lama + key) % len(abjad)
            abjad_baru = abjad[index_baru]
            hasil_enkripsi = hasil_enkripsi + abjad_baru
        else:
            hasil_enkripsi = hasil_enkripsi + karakter
    return hasil_enkripsi

def dekripsi(kalimat, key):
    hasil_dekripsi = ""
    for karakter in kalimat:
        if karakter in abjad:
            index_lama = abjad.index(karakter)
            index_baru = (index_lama - key) % len(abjad)
            abjad_baru = abjad[index_baru]
            hasil_dekripsi = hasil_dekripsi + abjad_baru
        else:
            hasil_dekripsi = hasil_dekripsi + karakter
    return hasil_dekripsi

if key == 13:
    kalimat_hasilenkripsi = enkripsi(kalimat, key)
    kalimat_hasildekripsi = dekripsi(kalimat_hasilenkripsi, key)
    encrypt_string = encrypt_string_to_md5(kalimat_hasilenkripsi)
    print("\nHasil enkripsi:", kalimat_hasilenkripsi)
    print("Masukkan berapa langkah:", key)
    print(f"Hasil dekripsi md5 dari ({kalimat_hasildekripsi}) adalah ({encrypt_string})")

    print("\n" + "="*40 + "\n")

else:
    print("kunci blom sama haha")
    print("kunci random yang benar adalah: ", kunci)
