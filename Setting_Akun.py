
users = {}
users['admin'] = 'admin'

def garis():
    print(40*"=")
    print("|-------------Daftar Akun--------------|")
    print(40*"=")
    print("| {0:^4} | {1:^12} | {2:^14} |".format("No", "Nama", "Password")) 
    print(40*"=")

def login():
    print(40*"=")
    count = 0
    while count < 3 :    
        username = input('Masukkan username : ')
        if username in users:
            password = input("Enter password    : ")
            if users[username] == password:
                print(40*"=")
                print(12*"=", 'Berhasil Login', 12*"=")
                print(40*"=")
                ent=input("")
                break
            else:
                print('Gagal Login, Coba Lagi \nKet : Jika Sudah Mencoba 3 Kali Anda Kembali Ke Menu')
                count += 1
        else:
            print("Username Tidak Valid")
    print(40*"=")

def akun_baru():
    print(40*"=")
    username = input("Masukkan Username Baru : ")
    password = input('Masukkan Password Baru : ')
    users[username] = password
    print(40*"=")

def daftar_akun():
    if len(users) <= 0:
        print("========================================")
        print("|------------Tidak Ada Akun------------|")
        print("========================================")
    else:
        no = 0
        garis()
        for data in users.items():
            no += 1
            print(f"| {no:^4} | {data[0]:^12} | {data[1]:^14} |")
            print(40*"=")
            ent=input("tekan 'ENTER' untuk lanjut")          

def hapus_akun():
    print(40*"=")
    username = input("Username Yang Ingin Dihapus     : ")
    if username in users :
        password = input("input Password Untuk Verifikasi : ")
        if users[username] == password:
            users.pop(username)
            print(40*"=")
            print("===========Akun Berhasil Dihapus========")
        else:
            print("Password Salah!")
    else:
        print("Username Akun Tidak Ditemui")
    print(40*"=")

#Program Utama
def loop():
    loop = True
    while loop :
        print(f"""{40*"="}
{10*"="}Portal Setting Akun{10*"="}<
{40*"="}""")
        print("[1] cek akun \n[2] Buat Akun Baru \n[3] Daftar Akun yang tersedia \n[4] Hapus Akun \n[0] Exit")
        try:
            pilihan = int(input("Masukkan Pilihan = "))
        except ValueError:
            print("harus berupa angka!!!")
        else:
            if pilihan == 1:
                login()
                print()
            elif pilihan == 2:
                akun_baru()
                print()
            elif pilihan == 3:
                daftar_akun()
                print()
            elif pilihan == 4:
                hapus_akun()
                print()
            elif pilihan == 0:
                print("Terima Kasih Telah Menggunakan Program Ini")
                lanjut = input()
                loop = False
            else:
                print("Input Salah, Masukkan Dengan Benar")