import os
import time
import datetime

#Daftar list2 yang ada
Menu     = ['French Fries', ' Burger', 'Hotdog', 'Greentea', 'Thaitea', 'Cappucino', 'Milk Chocolate', 'Milk Strawberry']
Harga    = [12000, 15000, 17000, 12000, 12000, 16000, 17000, 17000]

#Variabel hari
hari = str(datetime.datetime.now().strftime("%A"))

#fungsi untuk jam
def waktu():
    Jam     = time.localtime()
    hour    = Jam.tm_hour
    minutes = Jam.tm_min
    return ('{}:{}'.format(hour, minutes))

#fungsi untuk metode pembayaran
def bayar(hari, listnama, jumlahpesan, harga, diskonpesan, diskonhari, diskonbayar, totalharga):
    try:
        Bayar = int(input("Mau bayar Tunai atau E-money ? (1 atau 2) : "))
        if Bayar == '1' :
            print("--------------------------")
            print("Tasty Coffe")
            print("Hari :", hari)
            print("--------------------------")
            print("Menu         :", listnama)
            print("Jumlah Pesan :", jumlahpesan)
            print("Harga        :", harga)
            print("Diskon       :", diskonpesan)
            print("--------------------------")
            print("Jumlah Bayar :", totalharga)
            print("------------------------------------------------")
            print("Anda mendapatkan diskon pemesanan sebesar 10 % ")

        elif Bayar == '2':
            diskonbayar = int(diskonhari - diskonpesan)
            print("--------------------------")
            print("Tasty Coffe")
            print("Hari :", hari)
            print("--------------------------")
            print("Menu         :", listnama)
            print("Jumlah Pesan :", jumlahpesan)
            print("Harga        :", harga)
            print("Diskon       :", diskonpesan + diskonbayar + diskonhari)
            print("--------------------------")
            print("Jumlah Bayar :", totalharga - diskonpesan - diskonbayar - diskonhari)
            print("------------------------------------------------")
            print("Anda mendapatkan diskon pemesanan,E-money serta Weekend sebesar 10 % + 10 % + 5 %")

    except ValueError:
        print("Metode pembayaran salah, silahkan coba kembali")

#def hari()

#fungsi untuk resi pemesanan setelah memilih menu
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

#Fungsi untuk menu
def Pesann(hari):
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
                            A. French Fries    : Rp 12.000
                            B. Burger          : Rp 15.000
                            C. Hotdog          : Rp 17.000
                            D. Greentea        : Rp 12.000
                            E. Thaitea         : Rp 12.000
                            F. Cappucino       : Rp 16.000
                            G. Milk Chocolate  : Rp 17.000
                            H. Milk Strawberry : Rp 17.000
        ==================================================================
                                !!!!Diskon List!!!
        ==================================================================
        
        1. Mendapat Diskon setiap Pembelian 3 Makanan sebesar 10 %
        2. Mendapat Diskon setiap Pembelian 4 Minuman sebesar 10 %
        3. Mendapat Diskon setiap pembayaran melalui E-money sebesar 10 %
        4. Mendapat Diskon saat weekend sebesar 5 %
        ==================================================================
        """)  
        pesan = str(input("masukkan list abjad menu : "))
        counter = 0

        if pesan.casefold() == 'a':
            while True:
                try:
                    jumlahpesan  = int(input("masukkan jumlah pesanan : "))
                    listnama     = Menu[0]
                    harga        = (Harga[0] * jumlahpesan)
                    diskonpesan  = (Harga[0] - (harga * 10/100))
                    totalharga   = harga

                    if jumlahpesan >= 3 :
                        totalharga = (harga - diskonpesan)
                        pesanan(hari, listnama, jumlahpesan, harga, totalharga, diskonpesan)
                        break


                    elif jumlahpesan == 2 or jumlahpesan == 1:
                        pesanan(hari, listnama, jumlahpesan, harga, totalharga, diskonpesan)
                        break

                except ValueError:
                    print("Jumlah pesan yang anda masukkan salah, silahkan coba lagi")
                        

                    counter = counter + totalharga


        elif pesan.casefold() == 'b':
            while True:
                try:
                    jumlahpesan  = int(input("masukkan jumlah pesanan : "))
                    listnama     = Menu[1]
                    harga        = (Harga[1] * jumlahpesan)
                    diskonpesan  = (Harga[1] - (harga * 10/100))
                    totalharga   = harga

                    if jumlahpesan >= 3 :
                        totalharga = (harga - diskonpesan)
                        pesanan(hari, listnama, jumlahpesan, harga, totalharga, diskonpesan)
                        break


                    elif jumlahpesan == 2 or jumlahpesan == 1:
                        pesanan(hari, listnama, jumlahpesan, harga, totalharga, diskonpesan)
                        break

                except ValueError:
                    print("Jumlah pesan yang anda masukkan salah, silahkan coba lagi")
                        

                    counter = counter + totalharga

        elif pesan.casefold() == 'c':
            while True:
                try:
                    jumlahpesan  = int(input("masukkan jumlah pesanan : "))
                    listnama     = Menu[2]
                    harga        = (Harga[2] * jumlahpesan)
                    diskonpesan  = (Harga[2] - (harga * 10/100))
                    totalharga   = harga

                    if jumlahpesan >= 3 :
                        totalharga = (harga - diskonpesan)
                        pesanan(hari, listnama, jumlahpesan, harga, totalharga, diskonpesan)
                        break


                    elif jumlahpesan == 2 or jumlahpesan == 1:
                        pesanan(hari, listnama, jumlahpesan, harga, totalharga, diskonpesan)
                        break

                except ValueError:
                    print("Jumlah pesan yang anda masukkan salah, silahkan coba lagi")
                        

                    counter = counter + totalharga

        elif pesan.casefold() == 'd':
            while True:
                try:
                    jumlahpesan  = int(input("masukkan jumlah pesanan : "))
                    listnama     = Menu[3]
                    harga        = (Harga[3] * jumlahpesan)
                    diskonpesan  = (Harga[3] - (harga * 10/100))
                    totalharga   = harga

                    if jumlahpesan >= 3 :
                        totalharga = (harga - diskonpesan)
                        pesanan(hari, listnama, jumlahpesan, harga, totalharga, diskonpesan)
                        break


                    elif jumlahpesan == 2 or jumlahpesan == 1:
                        pesanan(hari, listnama, jumlahpesan, harga, totalharga, diskonpesan)
                        break

                except ValueError:
                    print("Jumlah pesan yang anda masukkan salah, silahkan coba lagi")
                        

                    counter = counter + totalharga

        elif pesan.casefold() == 'e':
            while True:
                try:
                    jumlahpesan  = int(input("masukkan jumlah pesanan : "))
                    listnama     = Menu[4]
                    harga        = (Harga[4] * jumlahpesan)
                    diskonpesan  = (Harga[4] - (harga * 10/100))
                    totalharga   = harga

                    if jumlahpesan >= 3 :
                        totalharga = (harga - diskonpesan)
                        pesanan(hari, listnama, jumlahpesan, harga, totalharga, diskonpesan)
                        break


                    elif jumlahpesan == 2 or jumlahpesan == 1:
                        pesanan(hari, listnama, jumlahpesan, harga, totalharga, diskonpesan)
                        break

                except ValueError:
                    print("Jumlah pesan yang anda masukkan salah, silahkan coba lagi")
                        

                    counter = counter + totalharga

        elif pesan.casefold() == 'f':
            while True:
                try:
                    jumlahpesan  = int(input("masukkan jumlah pesanan : "))
                    listnama     = Menu[5]
                    harga        = (Harga[5] * jumlahpesan)
                    diskonpesan  = (Harga[5] - (harga * 10/100))
                    totalharga   = harga

                    if jumlahpesan >= 3 :
                        totalharga = (harga - diskonpesan)
                        pesanan(hari, listnama, jumlahpesan, harga, totalharga, diskonpesan)
                        break


                    elif jumlahpesan == 2 or jumlahpesan == 1:
                        pesanan(hari, listnama, jumlahpesan, harga, totalharga, diskonpesan)
                        break

                except ValueError:
                    print("Jumlah pesan yang anda masukkan salah, silahkan coba lagi")
                        

                    counter = counter + totalharga

        elif pesan.casefold() == 'g':
            while True:
                try:
                    jumlahpesan  = int(input("masukkan jumlah pesanan : "))
                    listnama     = Menu[6]
                    harga        = (Harga[6] * jumlahpesan)
                    diskonpesan  = (Harga[6] - (harga * 10/100))
                    totalharga   = harga

                    if jumlahpesan >= 3 :
                        totalharga = (harga - diskonpesan)
                        pesanan(hari, listnama, jumlahpesan, harga, totalharga, diskonpesan)
                        break


                    elif jumlahpesan == 2 or jumlahpesan == 1:
                        pesanan(hari, listnama, jumlahpesan, harga, totalharga, diskonpesan)
                        break

                except ValueError:
                    print("Jumlah pesan yang anda masukkan salah, silahkan coba lagi")
                        

                    counter = counter + totalharga

        elif pesan.casefold() == 'h':
            while True:
                try:
                    jumlahpesan  = int(input("masukkan jumlah pesanan : "))
                    listnama     = Menu[7]
                    harga        = (Harga[7] * jumlahpesan)
                    diskonpesan  = (Harga[7] - (harga * 10/100))
                    totalharga   = harga

                    if jumlahpesan >= 3 :
                        totalharga = (harga - diskonpesan)
                        pesanan(hari, listnama, jumlahpesan, harga, totalharga, diskonpesan)
                        break


                    elif jumlahpesan == 2 or jumlahpesan == 1:
                        pesanan(hari, listnama, jumlahpesan, harga, totalharga, diskonpesan)
                        break

                except ValueError:
                    print("Jumlah pesan yang anda masukkan salah, silahkan coba lagi")
                        

                    counter = counter + totalharga
        else:
            pilihan = input("Menu tidak ditemukan, silahkan masukkan abjad menu yang tersedia, silahkan ulangi kembali (Y/N) : ")
            if pilihan.casefold == 'y':
                continue

            elif pilihan.casefold == 'n':
                os.system('cls')
                print("======================================\nTerimakasih :) Silahkan datang kembali\n======================================")
                exit()


        pilih  = input("apakah anda ingin order kembali ? (Y/N) : ")
        if pilih.casefold == 'y':
            continue

        elif pilih.casefold == 'n':
            print(counter)
            bayar(hari, listnama, jumlahpesan, harga, diskonpesan, diskonhari, diskonbayar, totalharga)

Pesann(hari)