import random
import rahasia

abjad = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
abjad = [letter.lower() for letter in abjad]

kunci = random.randint(1, 100)
key = kunci
kalimat = "nxh pvagn xnzh >//<"

if key == rahasia.KB:
    print("Kamu telah menemukan deskripsi nya!")

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

    print("\nHasil enkripsi:", kalimat_hasilenkripsi)
    print("Masukkan berapa langkah:", key)
    print(f"Hasil dekripsi dari ({kalimat_hasildekripsi}) adalah ({kalimat_hasilenkripsi})")

    print("\n" + "="*40 + "\n")

else:
    print("kunci blom sama haha")
    print("kunci random yang benar adalah: ", kunci)
