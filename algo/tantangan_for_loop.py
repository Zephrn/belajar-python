print("perulangan dengan for")
angka = [7,0,1,5,3,8,9,2,1,4,6]
# loop biasa
for i in angka:
    print("nilai", i)

print("")
# loop genap
print("perulangan angka genap")
gnp = [genap for genap in angka if genap %2 == 0]

for i in gnp:
    print(f"angka genap : {i}")

print("")

# loop ganjil
print("perulangan agnka ganjil")
gjl = [ganjil for ganjil in angka if ganjil %2 != 0]

for i in gjl:
    print(f"angka ganjil : {i}")

print("")
# kecuali 1 2 3 
print("print angka kecuali 1 2 3")
angka.sort()
for i in angka:
    if i in [1,2,3]:
        continue
    print(i)
