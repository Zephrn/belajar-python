from fractions import Fraction
# bilangan prima
print("bilangan prima")
inputan = int(input("masukan angka : "))
i = 2
while (i < inputan):
    j = 2
    while(j <= (i/j)):
        if not (i % j): break
        j = j + 1
    if (j > i/j) : print(i, "adalah bilangan prima")
    i = i + 1
print("yeah program berhasil")

print("")
# bilangan genap
print("bilangan genap")
inputan = int(input("masukan angka : "))
i = 2
while (i < inputan):
    j = 2
    while(j <= (i/j)):
        if not (i % j): break
        j = j + 1
    if (i % 2 == 0) : print(i, "adalah bilangan genap")
    i = i + 1
print("yeah program berhasil")

print("")
print("bilangan cacah")
# bilangan cacah
inputan = int(input("Masukkan angka: "))
i = 0
while i < inputan:
    print(f"{i} adalah bilangan cacah")
    i = i + 1
print("Program berhasil")

print("")
print("bilangan real")
# bilangan real
inputan = int(input("Masukkan angka: "))
i = 1
while i < inputan:
    print(f"{i} adalah bilangan real")
    i = i + 1
print("Program berhasil")

print("")
print("bilangan negatif")
# bilangan negatif 
inputan = int(input("Masukkan angka: "))
i = -inputan
while i < inputan:
    if (i == 0): break
    print(f"{i} adalah bilangan negatif")
    i = i + 1
print("Program berhasil")
print("")
# Bilangan Rasional
print("bilangan rasional")
inputan = int(input("Masukkan angka: "))
i = 1
while i < inputan:
    rational_number = Fraction(i, i+1)
    print(f"{rational_number} adalah bilangan rasional")
    i = i + 1
print("Program berhasil")

print("")
print("bilangan irasional")
# Bilangan Irrasional
prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23]
for prime in prime_numbers:
    irrational_number = prime ** 0.5
    print(f"{irrational_number} adalah bilangan irasional")

