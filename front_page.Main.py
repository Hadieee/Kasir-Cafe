import os
import time
import Setting_Akun
import Setting_Menu
import Kasir_cafe

def front_page(tampilan): 
    print(f"""
            
=WELCOME to Tasty Coffe,DUDE..=
       ______________
      |____|cafe|____|
      |\============/|
      ||\  ^    ^  /||
    <<|||\________/|||>>
      ||||\______/||||
      ||||||||||||||||
      ||||||||||||||||  
      [___|_|__|_|___]
      |||| |||||| ||||
       ||   ||||   ||
        |    ||     |
              |
|         1.masuk          |
|         2.keluar         |
                                                         
 {'=='}login dan tampilan awal{'=='}
    
    """)
    return tampilan

def inpil3():   # pilihan 3 setting menu dan akun
    print("[1] setting akun\n[2] setting menu")
    try:
        pilkunmen = int(input("masukkan pilihan(1/2): "))
    except:
        print("harus berupa angka!")
    else:
        if pilkunmen == 1:
            Setting_Akun.loop()
        elif pilkunmen == 2:
            Setting_Menu.set_menu()
        else:
            print("masukan salah")

def menuu():    # pilihan 2 kasir
    Kasir_cafe.menu()

main_menu = ("""
  MAIN MENU

[1] List Menu
[2] Kasir
[3] Setting
[4] Keluar
""")

i = 4

# untuk pilihan 1
os.system('cls')
while i >= 1 :
    os.system('cls')
    front_page(tampilan='')
    pilog = input("masukkan pilihan (1/2)? ")

    # untuk pilihan 1.1
    if pilog == '1':
        u = 3
        while u>=1:
            login = input("username : ")
            if login in Setting_Akun.users:
                passw = input("password : ")
                if passw == Setting_Akun.users[login]:
                    print("akun anda terdaftar dan anda sudah masuk")
                    e=3
                    while e>=1:
                        try:
                            print(main_menu)
                            pil1 = int(input("pilihan anda(1/2/3/4) ? "))
                        except:
                            print("\nmohon masukkan angka!\n")
                        else:
                            if pil1 == 1:
                                Setting_Menu.tampilan_menu()
                                lanjut=input("tekan 'ENTER' untuk kembali ke 'MAIN MENU'")
                                e = True
                            elif pil1 == 2:
                                menuu()
                            elif pil1 == 3:
                                inpil3()
                            elif pil1 == 4:
                                i = False
                                print("anda telah keluar")
                                exit(i)
                            else:
                                e-=1
                                print("inputan salah, mohon pilih sesuai angka")
                else:
                    print("lah!!!!")
            else:
                u-=1
                print(f"data tidak valid, percobaan tersisa {u}")
                time.sleep(2)
        

    # untuk pilihan 1.2
    elif pilog == '2':
        print("semoga harimu menyenangkan")
        exit()

    # untuk kesalahan masukan data
    else:
        print("pilihan yang anda masukkan salah")        
        time.sleep(2)
