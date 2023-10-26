# program (1): perhitungan sederhana
BilanganPertama = 15
BilanganKedua = 8
BilanganKetiga = 100
RumusPengjumlahan = BilanganPertama + BilanganKedua + BilanganKetiga
RumusPengurangan = BilanganPertama - BilanganKedua - BilanganKetiga
RumusPerkalian = BilanganPertama * BilanganKedua * BilanganKetiga
RumusPembagian = BilanganPertama / BilanganKedua / BilanganKetiga

print("Penjumlahan = ", BilanganPertama,  '+', BilanganKedua, '+', BilanganKetiga, '=', RumusPengjumlahan)
print("Penjumlahan = ", BilanganPertama,  '+', BilanganKedua, '+', BilanganKetiga, '=', RumusPengjumlahan)
print("Pengurangan = ", BilanganPertama,  '-', BilanganKedua, '-', BilanganKetiga, '=',    RumusPengurangan)
print("Perkalian = ", BilanganPertama,  'x', BilanganKedua, 'x', BilanganKetiga, '=',    RumusPerkalian)
print("Pembagian = ", BilanganPertama,  '/', BilanganKedua, '/', BilanganKetiga, '=',    RumusPembagian)

print("-"*20, "dengan input", "-"*20)
# dengan input
bil_pertama = int(input("Bilangan Pertama = "))
bil_kedua = int(input("Bilangan kedua = "))
bil_ketiga = int(input("Bilangan ketiga = "))
Rumus_Pengjumlahan = bil_pertama + bil_kedua + bil_ketiga
Rumus_Pengurangan = bil_pertama - bil_kedua - bil_ketiga
Rumus_Perkalian = bil_pertama * bil_kedua * bil_ketiga
Rumus_Pembagian = bil_pertama / bil_kedua / bil_ketiga

print("Penjumlahan = ", bil_pertama,  '+', bil_kedua, '+', bil_ketiga, '=', Rumus_Pengjumlahan)
print("Pengurangan = ", bil_pertama,  '-', bil_kedua, '-', bil_ketiga, '=',    Rumus_Pengurangan)
print("Perkalian = ", bil_pertama,  'x', bil_kedua, 'x', bil_ketiga, '=',    Rumus_Perkalian)
print("Pembagian = ", bil_pertama,  '/', bil_kedua, '/', bil_ketiga, '=', Rumus_Pembagian)