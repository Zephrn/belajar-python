print("QUIZ MENGHITUNG NILAI MAHASISWA")
nama = str(input("Masukan Nama Anda\t: "))
nim = int(input("Masukan Nim Anda\t: "))
while True:
    try:
        nilai_quiz = float(input("Masukkan Nilai Quiz\t: "))
        if 1 <= nilai_quiz <= 100:
            break
        else:
            print("Nilai harus berada di antara 1 dan 100. Silakan coba lagi.")
    except ValueError:
        print("Input harus berupa angka. Silakan coba lagi.")
while True:
    try:
        nilai_tugas = float(input("Masukkan Nilai tugas\t: "))
        if 1 <= nilai_tugas <= 100:
            break
        else:
            print("Nilai harus berada di antara 1 dan 100. Silakan coba lagi.")
    except ValueError:
        print("Input harus berupa angka. Silakan coba lagi.")
while True:
    try:
        nilai_uts = float(input("Masukkan Nilai uts\t: "))
        if 1 <= nilai_uts <= 100:
            break
        else:
            print("Nilai harus berada di antara 1 dan 100. Silakan coba lagi.")
    except ValueError:
        print("Input harus berupa angka. Silakan coba lagi.")
while True:
    try:
        nilai_uas = float(input("Masukkan Nilai Quiz\t: "))
        if 1 <= nilai_uas <= 100:
            break
        else:
            print("Nilai harus berada di antara 1 dan 100. Silakan coba lagi.")
    except ValueError:
        print("Input harus berupa angka. Silakan coba lagi.")


print("="*50,)
print(" ", "*"*4, "KARTU HASIL STUDI MAHASISWA", " ","*"*4)
print("="*50,)
print("Nama Mahasiswa \t: ", nama)
print("NIM \t\t: ", nim)
print("Mata Kuliah \t: ", "Algoritma Pemograman")
print("Semester/Kelas \t: ", "I/A")
print("SKS \t\t: ", "3 SKS")
print("\n")
nq = nilai_quiz * 0.1 
nt = nilai_tugas * 0.2
nu = nilai_uts * 0.3
na = nilai_uas * 0.4
print("Nilai Quiz\t= ", nilai_quiz, nq)
print("Nilai Tugas\t= ", nilai_tugas, nt)
print("Nilai UTS\t= ", nilai_uts, nu)
print("Nilai UAS\t= ", nilai_uas, na)

# fungsi


nilai_angka = (nilai_quiz * 0.1) + (nilai_tugas * 0.2) + (nilai_uts * 0.3) + (nilai_uas * 0.4)

# fungsi nilai
if nilai_angka >= 80.51 and nilai_angka <= 100:
    grade = "A"
elif nilai_angka >= 65.51 and nilai_angka <= 80.50:
    grade = "B"
elif nilai_angka >= 50.51 and nilai_angka <= 65.50:
    grade = "C"
elif nilai_angka >= 40.41 and nilai_angka <= 50.50:
    grade = "D"
elif nilai_angka >= 0 and nilai_angka <= 40.40:
    grade = "E"

if nilai_angka >= 50.51 and nilai_angka <= 100:
    maka = "lulus"
else:
    maka = "Tidak Lulus"

print("-"*50)
print("Nilai Angka \t: ", nilai_angka)
print("Nilai Huruf \t: ", grade)
print("Kelulusan \t: ", maka)
print("-"*50)
print("\n")
print("="*50,)
print(" ", "*"*4, "Program Studi D3 Teknik Informatika", " ","*"*4)
print("Jurusan Teknik Elektro Politeknik Negeri Pontianak")
print("\n")
print("="*50,)

