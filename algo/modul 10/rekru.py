def AngkaTampil(i):
    print(f"perulangan ke {i}")
AngkaTampil(1)
AngkaTampil(2)
AngkaTampil(3)
print("")

def AngkaTampil(batas, i = 1):
    print(f"perulangan ke {i}")
AngkaTampil(3)
AngkaTampil(3,2)
AngkaTampil(3,3)

print("")
def bata(batas, i=1):
    print(f"perulangan ke {i}")
    if (i < batas):
        bata(batas, i + 1 )
        print(f"perulangan ke {i}")

bata(10)

print()

# gambaran rekrusif
i = 1
batas = 5
if i < batas:
    idua = i + 1
    if idua < batas:
        itiga = idua + 1
        if itiga < batas:
            iempat = itiga + 1
            if iempat < batas:
                ilima = iempat + 1
                if ilima < batas:
                    ienam = ilima + 1
                # dan seterusnya
                    print(ienam)
                print(ilima)
            print(iempat)
        print(itiga)
    print(idua)
print(i)

# rekrusif ke kanan
print("")
def bata(batas, i=1):
    prefix = '--' * (i-1)
    print(f"{prefix}sebelum rekrusif {(i)}")
    if (i < batas):
        bata(batas, i + 1 )
    print(f"{prefix}setelah rekrusif {(i)}")

bata(10)

# rekrusif ke kiri
print("")
def bata(batas, i=1):
    prefix = '--' * (batas - i)
    print(f"{prefix}sebelum rekrusif ({i})")
    if (i < batas):
        bata(batas, i + 1)
    print(f"{prefix}setelah rekrusif ({i})")

bata(10)


