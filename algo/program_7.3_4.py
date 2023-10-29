# enskripsi program serang kota itu besok dengan 2 langkah enskripsi 
abjad = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
abjad = [letter.lower() for letter in abjad]

key = 2
kalimat = "serang kota itu besok"

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

kalimat_hasilenkripsi = enkripsi(kalimat, key)
kalimat_hasildekripsi = dekripsi(kalimat_hasilenkripsi, key)

print("\nHasil enkripsi:", kalimat_hasilenkripsi)
print("Masukkan berapa langkah:", key)
print("Hasil dekripsi:", kalimat_hasildekripsi)


print("\n" + "="*40 + "\n")

# enskripsi berupa inputan
abjad = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
abjad = [letter.lower() for letter in abjad]

key = int(input("Masukkan berapa langkah: "))
kalimat = input("Kalimat yang ingin dienkripsi: ")

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
# fungsi enskripsi
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

kalimat_hasilenkripsi = enkripsi(kalimat, key)
kalimat_hasildekripsi = dekripsi(kalimat_hasilenkripsi, key)

print("\nHasil enkripsi:", kalimat_hasilenkripsi)
print("Masukkan berapa langkah:", key)
print("Hasil dekripsi:", kalimat_hasildekripsi)
print("\n" + "="*40 + "\n")


