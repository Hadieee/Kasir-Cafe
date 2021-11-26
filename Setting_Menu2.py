import os
from tabulate import tabulate 

menu=['french fries','burger','hotdog','greentea','thaitea','capucino','chocolate milk','strawberry milk']
harga=[12000,15000,17000,12000,12000,16000,17000,17000]


package = {
'Menu': menu,
'Harga(Rp)':harga,
}

def tampilan_menu():
    print(tabulate(package,headers='keys', tablefmt='fancy_grid'))

def tambah():
    i = 1
    for x,y in zip(menu,harga):
        print(str(i),x,": Rp",y)
        i += 1
#------> memilih menu  
i = 3
def set_menu():
    while i >= 3 :
        #input pengguna
        print(f"\n{20*'='}SETTING MENU{20*'='}")
        print("[1]tambah menu\n[2]hapus menu\n[3]ubah menu\n[4]tampilkan menu\n[5]keluar")
        try:
            pilihan=int(input('masukkan pilihan data(1/2/3/4/5) : '))
        except:
            print("pilih dengan angka yang tertera!")
            input("tekan 'ENTER' untuk lanjut")
            os.system('cls')
        else:
            if pilihan == 1:    # tambah menu
                # a = int(input("Pilih letak data yang ingin ditambahkan : "))
                menu_baru = input("Masukkan menu yang ingin ditambahkan : ")
                while True:
                    try:
                        harga_baru= int(input("Masukkan harga : "))
                        menu.append(menu_baru)
                        harga.append(harga_baru)
                        tampilan_menu()
                        break
                    except:
                        print("mohon masukkan angka!")



            elif pilihan == 2:  # hapus menu       
                tambah()
                b=int(input('hapus indeks ke-'))
                menu.remove(menu[b])
                harga.remove(harga[b])
                print("menu terhapus")

            elif pilihan == 3:  # ubah menu
                while(True):
                    try:
                        tambah()
                        a=int(input('pilih nomor menu yang mau diubah : '))
                        b=input("Masukkan nama menu: ")
                        c=int(input('masukkan harga : '))
                    except:
                        print("terjadi kesalahan inputan")
                        print("mohon inputkan data dengan benar")
                    else:
                        menu[a-1]=b
                        harga[a-1]=c
                        print("data telah diubah")
                        break

            elif pilihan == 4:  # tampilan menu
                os.system('cls')
                print(tabulate(package,headers='keys', tablefmt='fancy_grid'))
                lanjut = input("tekan 'ENTER untuk lanjut")

            elif pilihan == 5:  # keluar
                os.system('cls')
                break
            else:
                break