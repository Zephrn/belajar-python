# # fungsi kosong 

def fungs():
    """
    menampilkan def kosong
    """
    print("print fungsi")

fungs()
print("")



# fungsi parameter dan optional

def huhu(kota, suhu = 37, satuan = "celcius"):
    print(f"di {kota} suhunya {suhu} {satuan}")
    """
    menampilkan suhu di suatu kota
    """

huhu("singkawang", 30)
huhu("singkawang", 87, "fahrenhait")
huhu("pontianak", )
print("")



# fungsi local dan global dan dic string

laptop, prosesor = "lenovo", "amd"

def lp(gp = "rtx"):
    """
    fungsi ini untuk melihat macam macam prosesor 
    yang digunakan pada laptop 
    """
    prosesor = "intel"
    print(laptop, prosesor,"graphic card", gp)



print("pemanggilan langsung : ",laptop, prosesor)

print("pemanggilan def ", end="")
lp()
print("")
# parameter loop 

def loop(nama):
    nama = ['fadil', 'hafiz', 'rosi', 'koko']
    for i in nama:
        print(f"teman saya {i}")

loop(nama="")