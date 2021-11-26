import os
import time
import datetime
import Setting_Menu
#Daftar list2 yang ada
Menu     = ['French Fries', ' Burger', 'Hotdog', 'Greentea', 'Thaitea', 'Cappucino', 'Milk Chocolate', 'Milk Strawberry']
Harga    = [12000, 15000, 17000, 12000, 12000, 16000, 17000, 17000]

#Variabel hari
hari = str(datetime.datetime.now().strftime("%A"))

#Variabel2 yang ada
counter     = 0
totalharga  = 0
diskonhari  = 0
diskonbayar = 0
diskonpesan = 0

#fungsi untuk jam
def waktu():
    Jam     = time.localtime()
    hour    = Jam.tm_hour
    minutes = Jam.tm_min
    return ('{}:{}'.format(hour, minutes))

#fungsi untuk metode pembayaran
def metodebayar(hari, diskonpesan, diskonbayar, diskonhari):
    while True:
        try:
            pembayaran = int(input("Mau bayar Tunai atau E-money ? (1 untuk Tunai, 2 untuk E-money) : "))
            if hari == 'Saturday' or hari == 'Sunday':
                if pembayaran == 1 :
                    print("--------------------------")
                    print("Tasty Coffe")
                    print("Hari :", hari)
                    print("--------------------------")
                    print("Jumlah Bayar :", diskonpesan - diskonhari)
                    print("------------------------------------------------")
                    print("Anda mendapatkan diskon Pemesanan serta Weekend sebesar 10 % + 5 %")
                    Bayar     = int(input("Masukkan uang yang diterima : "))
                    kembalian = Bayar - (diskonpesan - diskonhari)
                    if kembalian > 0:
                        print("Kembalian anda sebesar : Rp.", kembalian)
                        print("Terimakasih telah datang ke cafe kami :) Silahkan datang kembali")
                        time.sleep(2)
                        os.system('cls')
                        

                    elif kembalian == 0:
                        print("Uang anda pas")
                        print("Terimakasih telah datang ke cafe kami :) Silahkan datang kembali")
                        time.sleep(2)
                        os.system('cls')
                        break

                    else:
                        print("Uang anda kurang")
                        time.sleep(2)

                elif pembayaran == 2:
                    print("--------------------------")
                    print("Tasty Coffe")
                    print("Hari :", hari)
                    print("--------------------------")
                    print("Jumlah Bayar :", diskonbayar - (diskonbayar * 10/100)) - diskonhari
                    print("------------------------------------------------")
                    print("Anda mendapatkan diskon pemesanan,E-money serta Weekend sebesar 10 % + 10 % + 5 %")
                    Bayar     = int(input("Masukkan uang yang diterima : "))
                    kembalian = Bayar - (diskonbayar - (diskonbayar * 10/100) - diskonhari)
                    if kembalian > 0:
                        print("Kembalian anda sebesar : Rp.", kembalian)
                        print("Terimakasih telah datang ke cafe kami :) Silahkan datang kembali")
                        time.sleep(2)
                        os.system('cls')

                    elif kembalian == 0:
                        print("Uang anda pas")
                        print("Terimakasih telah datang ke cafe kami :) Silahkan datang kembali")
                        time.sleep(2)
                        os.system('cls')
                        break

                    else:
                        print("Uang anda kurang")
                        continue

                else:
                    print("Metode pembayaran salah, silahkan coba kembali")
                    continue

            else:
                if pembayaran == 1 :
                    print("--------------------------")
                    print("Tasty Coffe")
                    print("Hari :", hari)
                    print("--------------------------")
                    print("Jumlah Bayar :", diskonpesan)
                    print("------------------------------------------------")
                    print("Anda mendapatkan diskon pemesanan sebesar 10 % ")
                    Bayar     = int(input("Masukkan uang yang diterima : "))
                    kembalian = Bayar - diskonpesan
                    if kembalian > 0:
                        print("Kembalian anda sebesar : Rp.", kembalian)
                        print("Terimakasih telah datang ke cafe kami :) Silahkan datang kembali")
                        time.sleep(2)
                        os.system('cls')

                    elif kembalian == 0:
                        print("Uang anda pas")
                        print("Terimakasih telah datang ke cafe kami :) Silahkan datang kembali")
                        time.sleep(2)
                        os.system('cls')
                        break

                    else:
                        print("Uang anda kurang")

                elif pembayaran == 2:
                    print("--------------------------")
                    print("Tasty Coffe")
                    print("Hari :", hari)
                    print("--------------------------")
                    print("Jumlah Bayar :", diskonbayar - (diskonbayar * 10/100))
                    print("------------------------------------------------")
                    print("Anda mendapatkan diskon pemesanan,E-money sebesar 10 % + 10 %")
                    Bayar     = int(input("Masukkan uang yang diterima : "))
                    kembalian = Bayar - (diskonbayar - (diskonbayar * 10/100))
                    if kembalian > 0:
                        print("Kembalian anda sebesar : Rp.", kembalian)
                        print("Terimakasih telah datang ke cafe kami :) Silahkan datang kembali")
                        time.sleep(2)
                        os.system('cls')
                        break

                    elif kembalian == 0:
                        print("Uang anda pas")
                        print("Terimakasih telah datang ke cafe kami :) Silahkan datang kembali")
                        time.sleep(2)
                        os.system('cls')
                        break

                    else:
                        print("Uang anda kurang")
                        continue

                else:
                    print("Metode pembayaran salah, silahkan coba kembali")
                    continue

        except ValueError:
            print("Metode pembayaran salah, silahkan coba kembali")


#Fungsi untuk memesan menu
def pesann(angka, counter):
    while True:
        try:
            jumlahpesan  = int(input("masukkan jumlah pesanan : "))
            listnama     = Menu[angka]
            harga        = (Harga[angka] * jumlahpesan)
            diskonpesan  = harga * 10/100
            totalharga   = harga

            if jumlahpesan >= 3 :
                totalharga = (harga - diskonpesan)
                pesanan(hari, listnama, jumlahpesan, harga, totalharga, diskonpesan)
                counter += totalharga
                break


            elif jumlahpesan == 2 or jumlahpesan == 1:
                pesanan(hari, listnama, jumlahpesan, harga, totalharga)
                counter += totalharga
                break

            else:
                print("Jumlah pesan yang anda masukkan salah, silahkan coba lagi")

        except ValueError:
            print("Jumlah pesan yang anda masukkan salah, silahkan coba lagi")
                
    return counter

#fungsi untuk resi pemesanan setelah memesan salah satu menu
def pesanan(hari, listnama, jumlahpesan, harga, totalharga, diskonpesan):
    print("--------------------------")
    print("Tasty Coffe")
    print("Hari :",hari)
    print("--------------------------")
    print("Menu         :", listnama)
    print("Jumlah Pesan :", jumlahpesan)
    print("Harga        :", harga)
    if jumlahpesan >= 3:
        print("Diskon       :", diskonpesan)
        print("--------------------------")
        print("Jumlah Bayar :", totalharga)
        print("--------------------------")
    else:
        print("--------------------------")
        print("Jumlah Bayar :", totalharga)
        print("--------------------------")

    time.sleep(1)

#program untuk menu:
def menu(counter, hari, diskonpesan, diskonbayar, diskonhari):
    while True: 
        os.system('cls')
        print(waktu(), 'WITA' )
        print(hari)
        print("""
        ==================================================================
        ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||                    
        |||||||||||||||||||||      Tasty Coffe      |||||||||||||||||||||| 
        |||||||||||||||             List Menu             ||||||||||||||||
        ==================================================================
        """)
        Setting_Menu.tambah()
        print("""
        ==================================================================
                                !!!!Diskon List!!!
        ==================================================================
        
        1. Mendapat Diskon setiap Pembelian 3 Makanan sebesar 10 %
        2. Mendapat Diskon setiap Pembelian 4 Minuman sebesar 10 %
        3. Mendapat Diskon setiap pembayaran melalui E-money sebesar 10 %
        ==================================================================
        """)  
        pesan = str(input("masukkan list nomor menu : "))

        if pesan == '1':
            counter = pesann(0, counter)

        elif pesan == '2':
            counter = pesann(1, counter)  

        elif pesan == '3':
            counter = pesann(2, counter) 

        elif pesan == '4':
            counter = pesann(3, counter) 

        elif pesan == '5':
            counter = pesann(4, counter) 

        elif pesan == '6':
            counter = pesann(5, counter)

        elif pesan == '7':
            counter = pesann(6, counter) 

        elif pesan == '8':
            counter = pesann(7, counter) 
            
        else:
            print("Menu tidak ditemukan, silahkan masukkan abjad menu yang tersedia :) ")
            time.sleep(2)
            continue

        pilih = (input("apakah anda ingin order kembali ? (Y/N) : "))
        if pilih.casefold() == 'y':
            continue

        elif pilih.casefold() == 'n':
            diskonhari   = counter - (counter * 5/100)
            diskonpesan  = counter - (counter * 10/100)
            diskonbayar  = counter - (counter * 10/100)
            metodebayar(hari, diskonpesan, diskonbayar, diskonhari)

        else:
            print("Pilihan anda salah, silahkan coba kembali")
            counter = 0
            time.sleep(2)
            continue