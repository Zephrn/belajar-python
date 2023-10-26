print("Latihan Praktikum Menggunakan Operator Bitwise OR, AND, XOR dan NOT")
print("\n")

a = 75
b = 82

print(f"nilai biner dari a yaitu {a} adalah:\t {format(a, '08b')}")
print(f"nilai biner dari a yaitu {b} adalah:\t {format(a, '08b')}")
print("\n")
# bitwise OR
bitwise_or = a | b
print(f"nilai a OR b : {bitwise_or}")
print(f"nilai biner dari a OR b {bitwise_or} adalah:\t {format(bitwise_or, '08b')}")
print("\n")
# bitwise AND
bitwise_and = b & b
print(f"nilai a AND b : {bitwise_and}")
print(f"nilai biner dari a AND b {bitwise_and} adalah:\t {format(bitwise_and, '08b')}")
print("\n")
# bitwise XOR
bitwise_xor =  bitwise_or ^ bitwise_and
print(f"nilai a XOR b : {bitwise_xor}")
print(f"nilai biner dari a XOR b {bitwise_xor} adalah:\t {format(bitwise_xor, '08b')}")
# bitwise not
print("\n")
bitwise_nota = (~b - bitwise_xor)
bitwise_notb = ~b
binta = bin(bitwise_nota)
bintb = bin(bitwise_notb)
print(f"nilai ~a : {bitwise_nota} dan nilai ~b : {bitwise_notb}")
print(f"nilai biner dari ~a adalah : {format(bitwise_nota, '08b')} \nnilai biner dari ~b adalah : {format(bitwise_notb, '08b')}")

# menggunakan Input
print("\n")
print("-"*20, "dengan input", "-"*20)
print("\n")
a = int(input("masukan inputan a : "))
b = int(input("masukan inputan b : "))
print("\n")
print(f"nilai biner dari a yaitu {a} adalah:\t {format(a, '08b')}")
print(f"nilai biner dari a yaitu {b} adalah:\t {format(a, '08b')}")
print("\n")
# bitwise OR
bitwise_or = a | b
print(f"nilai a OR b : {bitwise_or}")
print(f"nilai biner dari a OR b {bitwise_or} adalah:\t {format(bitwise_or, '08b')}")
print("\n")
# bitwise AND
bitwise_and = b & b
print(f"nilai a AND b : {bitwise_and}")
print(f"nilai biner dari a AND b {bitwise_and} adalah:\t {format(bitwise_and, '08b')}")
print("\n")
# bitwise XOR
bitwise_xor = bitwise_or ^ bitwise_and
print(f"nilai a XOR b : {bitwise_xor}")
print(f"nilai biner dari a XOR b {bitwise_xor} adalah:\t {format(bitwise_xor, '08b')}")
# bitwise not
print("\n")
bitwise_nota = a = (~b - bitwise_xor)
bitwise_notb = ~b
print(f"nilai ~a : {bitwise_nota} dan nilai ~b : {bitwise_notb}")
print(f"nilai biner dari ~a adalah : {format(bitwise_nota, '08b')} \nnilai biner dari ~b adalah : {format(bitwise_notb, '08b')}")