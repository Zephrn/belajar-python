set_a = {"John", "Amanda", "Kate", "Mike", "Sophia"}
set_b = {"Tom", "Amanda", "Nancy", "Sophia", "John"}
set_c = {"John", "Amanda", "Kate", "Mike", "Sophia"}
set_d = {"Tom", "Amanda", "Nancy", "Sophia", "John"}
set_e = {"Kate", "Mike", "Sophia", "Helen", "Tom"}

# Gabungkan irisan dari semua set
irisan_2a = set()
irisan_2a = irisan_2a.union(set_a.intersection(set_b))
irisan_2a = irisan_2a.union(set_a.intersection(set_c))
irisan_2a = irisan_2a.union(set_a.intersection(set_d))
irisan_2a = irisan_2a.union(set_a.intersection(set_e))

# Tampilkan hasil irisan
print("Hasil irisan_2a:")
for item in irisan_2a:
    print(item)