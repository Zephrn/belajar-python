# from random import randint

# # Buat list option untuk permainan
# Glist = ["Gunting", "Batu", "Kertas"]

# # buat pilihan secara random dengan func randint
# komputer = Glist[randint(0,2)]

# # Set pemain ke False
# pemain = False

# while pemain == False:
#     #Set pemain ke True
#     pemain = input("Gunting, Batu, Kertas ? : ")

#     if pemain == komputer:
#         print("Seri!")
#     elif pemain == "Batu":
#         if komputer == "Kertas":
#             print("Kamu Kalah!", komputer, "membungkus", pemain)
#         else:
#             print("Kamu Menang!", pemain, "menghancurkan", komputer)
#     elif pemain == "Kertas":
#         if komputer == "Gunting":
#             print("Kamu Kalah!", komputer, "memotong", pemain)
#         else:
#             print("Kamu Menang!", pemain, "membungkus", komputer)
#     elif pemain == "Gunting":
#         if komputer == "Batu":
#             print("Kamu Kalah!", komputer, "menghancurkan", pemain)
#         else:
#             print("Kamu Menang!", pemain, "memotong", komputer)
#     else:
#         print("Pilihan yang kamu masukkan salah...")

#     # Set pemain ke False lagi supaya terjadinya looping yang berulang
#     pemain = False
#     komputer = Glist[randint(0,2)]


# suit kelingking jempol telunjuk 

from random import randint

# Buat list option untuk permainan
Glist = ["Jempol", "Telunjuk", "Kelingking"]

# buat pilihan secara random dengan func randint
komputer = Glist[randint(0, 2)]

# Set pemain ke False
pemain = False

while pemain == False:
    #Set pemain ke True
    pemain = input("Jempol, Kelingking, Telunjuk ? : ")

    if pemain == komputer:
        print("Seri!")
    elif pemain == "Jempol":
        if komputer == "Kelingking":
            print("Kamu Kalah!", komputer, "Mengalahkan", pemain)
        else:
            print("Kamu Menang!", pemain, "Mengalahkan", komputer)
    elif pemain == "Telunjuk":
        if komputer == "Jempol":
            print("Kamu Kalah!", komputer, "Mengalahakan", pemain)
        else:
            print("Kamu Menang!", pemain, "Mengalahkan", komputer)
    elif pemain == "Kelingking":
        if komputer == "Telunjuk":
            print("Kamu Kalah!", komputer, "Mnegalahkan", pemain)
        else:
            print("Kamu Menang!", pemain, "Mengalahkan", komputer)
    else:
        print("Pilihan yang kamu masukkan salah...")

    # Set pemain ke False lagi supaya terjadinya looping yang berulang
    pemain = False
    komputer = Glist[randint(0, 2)]
