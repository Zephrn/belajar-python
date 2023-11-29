import datetime
import os
import getpass

# Membersihkan transaksi sebelumnya
if __name__ == "__main__":
    sistem_operasi = os.name

    match sistem_operasi:
        case "posix":os.system("clear")
        case "nt":os.system("cls")

# Login user
def login(name,password):
    sukses = False
    file = open('databaselogin.txt', 'r')
    for i in file:
        a,b = i.split(",")
        b = b.strip()
        if(a==name and b==password):
            sukses = True
            break
    file.close()
    if(sukses):
        print('\nLogin berhasil, Selamat Datang',name)
        user()
    else:
        print('\33[91mLogin gagal, silahkan coba lagi atau registrasi akun anda terlebih dahulu...\33[0m')
    begin()

# Register user baru
def register(name,password):
    file = open('databaselogin.txt','a')
    file.write(name+','+password+'\n')

# Akses login
def access(option):
    global name
    if(option == 'login'):
        waktu = datetime.datetime.now()
        print(waktu.strftime('%d/%m/%Y %H:%M:%S'))
        name = input('\nMasukkan username : ')
        password = getpass.getpass('Masukkan password : ')
        login(name,password)
    else:
        print('Masukkan username dan password anda yang baru')
        name = input('Masukkan username : ')
        password = input('Masukkan password : ')
        register(name,password)
        print('Registrasi berhasil, silahkan login...')
        begin()

# Pilihan apakah user ingin login atau registrasi
def begin():
    global option
    print('\n--- Selamat Datang ---\n')
    print("Ketik 'login' jika anda sudah memiliki akun")
    print("Ketik 'reg' jika anda belum memiliki akun\n")
    option = input('Silahkan masukkan (login/reg) : ')
    if(option!='login' and option!='reg' and option!='Reg' and option!='REG'):
        print('\33[91mPeriksa kembali input anda...\33[0m')
        begin()


def user():
    print("teman yang ingin di chat")


begin()
access(option)