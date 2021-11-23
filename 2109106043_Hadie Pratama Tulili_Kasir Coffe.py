import os
import time
import datetime

#Daftar list2 yang ada
Menu     = ['French Fries', ' Burger', 'Hotdog', 'Greentea', 'Thaitea', 'Cappucino', 'Milk Chocolate', 'Milk Strawberry']
Harga    = [12000, 15000, 17000, 12000, 12000, 16000, 17000, 17000]
Weekdays = ['Senin','Selasa','Rabu','Kamis','Jumat']
Weekend  = ['Sabtu','Minggu']


def waktu():
    Jam     = time.localtime()
    hour    = Jam.tm_hour
    minutes = Jam.tm_min
    return ('{}:{}'.format(hour, minutes))

hari1 = str(datetime.datetime.now().strftime("%A"))



#Fungsi untuk menu
def Pesann():
    coba = 'y'
    while coba == "y": 
        os.system('cls')
        print(waktu(), 'WITA' )
        print(hari1)
        print("""
        ==============================
        
                Tasty Coffe
                List Menu 
        ==============================
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
        
        1. Mendapat Diskon setiap Pembelian 3 Minuman sebesar 10%
        2. Mendapat Diskon setiap Pembelian 4 Makanan sebesar 10%
        3. Mendapat Diskon setiap pembayaran melalui E-money sebesar 10%
        4. Mendapat Diskon saat weekend sebesar 5%
        ==================================================================
        """)
        ulang    = 'a'
        while ulang == 'a':      
            pesan = str(input("masukkan list abjad menu : "))
            counter = 0

            if pesan == 'a' or 'A':
                balik    = 'b'
                while balik == 'b':
                    try:
                        jumlahpesan1 = int(input("masukkan jumlah pesanan : "))
                        listnama1    = Menu[0]
                        harga1       = (Harga[0] * jumlahpesan1)

                        if jumlahpesan1 >= 3 :
                            if hari1 == 'Saturday' or 'Sunday':
                                diskon1     = int(harga1 * 10/100)
                                diskon1_1   = int(diskon1 - (harga1 * 5/100))
                                totalharga1 = int(harga1 - diskon1 - diskon1_1)
                                print("--------------------------")
                                print("Tasty Coffe")
                                print("Hari :",hari1)
                                print("--------------------------")
                                print("Menu         :", listnama1)
                                print("Jumlah Pesan :", jumlahpesan1)
                                print("Harga        :", harga1)
                                print("Diskon       :", diskon1 + diskon1_1)
                                print("--------------------------")
                                print("Jumlah Bayar :", totalharga1)
                                print("--------------------------")
                                print("Anda mendapatkan diskon pemesanan dan weekend sebesar 10 % + 5 % ")
                                counter = counter + totalharga1
                                Bayar = input("Mau bayar Tunai atau E-money ? (1 atau 2) : ")
                                oke  = 'c'
                                while oke == 'c':
                                    if Bayar == '1' :
                                        print("--------------------------")
                                        print("Tasty Coffe")
                                        print("Hari :", hari1)
                                        print("--------------------------")
                                        print("Menu :",listnama1)
                                        print("Jumlah Pesan :", jumlahpesan1)
                                        print("Harga :", harga1)
                                        print("Diskon :", diskon1)
                                        print("--------------------------")
                                        print("Jumlah Bayar :", totalharga1)
                                        print("------------------------------------------------")
                                        print("Anda mendapatkan diskon pemesanan sebesar 10 % ")
                                    
                                    elif Bayar == '2':
                                        diskon1_1_1 = int(diskon1_1 - diskon1)
                                        print("--------------------------")
                                        print("Tasty Coffe")
                                        print("Hari :", hari1)
                                        print("--------------------------")
                                        print("Menu :",listnama1)
                                        print("Jumlah Pesan :", jumlahpesan1)
                                        print("Harga :", harga1)
                                        print("Diskon :", diskon1 + diskon1_1 + diskon1_1_1)
                                        print("--------------------------")
                                        print("Jumlah Bayar :", totalharga1 - diskon1_1_1)
                                        print("------------------------------------------------")
                                        print("Anda mendapatkan diskon pemesanan,E-money serta Weekend sebesar 10 % + 10 % + 5 %")


                                    elif hari1 == 'Monday' or 'Tuesday' :
                                        print("Metode pembayaran salah, silahkan pilih kembali")
                                        oke = 'c'

                            else:
                                diskon1     = int(harga1 * 10/100)
                                totalharga1 = int(harga1 - diskon1)
                                print("--------------------------")
                                print("Tasty Coffe")
                                print("Hari :",hari1)
                                print("--------------------------")
                                print("Menu         :", listnama1)
                                print("Jumlah Pesan :", jumlahpesan1)
                                print("Harga        :", harga1)
                                print("Diskon       :", diskon1)
                                print("--------------------------")
                                print("Jumlah Bayar :", totalharga1)
                                print("--------------------------")
                                print("Anda mendapatkan diskon pemesanan sebesar 10 % ")

                        
                        elif jumlahpesan1 < 2:
                            if hari == 'Saturday' or 'Sunday ':
                                diskon1     = int(harga1 * 5/100)
                                totalharga1 = int(harga1 - diskon1)
                                print("--------------------------")
                                print("Tasty Coffe")
                                print("Hari :",hari1)
                                print("--------------------------")
                                print("Menu         :", listnama1)
                                print("Jumlah Pesan :", jumlahpesan1)
                                print("Harga        :", harga1)
                                print("Diskon       :", diskon1)
                                print("--------------------------")
                                print("Jumlah Bayar :", totalharga1)
                                print("--------------------------")
                                print("Anda mendapatkan diskon weekend sebesar 5 % ")
                                oke1  = 'c'
                                while oke1 == 'c':
                                    Bayar = input("Mau bayar Tunai atau E-money ? (1 atau 2) : ")
                                    if Bayar == '1' :
                                            print("--------------------------")
                                            print("Tasty Coffe")
                                            print("Hari :", hari1)
                                            print("--------------------------")
                                            print("Menu :",listnama1)
                                            print("Jumlah Pesan :", jumlahpesan1)
                                            print("Harga :", harga1)
                                            print("Diskon :", diskon1)
                                            print("--------------------------")
                                            print("Jumlah Bayar :", totalharga1)
                                            print("------------------------------------------------")
                                            print("Anda mendapatkan diskon weekend sebesar 5 % ")
                                            
                                    
                                    elif Bayar == '2':
                                            print("--------------------------")
                                            print("Tasty Coffe")
                                            print("Hari :", hari1)
                                            print("--------------------------")
                                            print("Menu :",listnama1)
                                            print("Jumlah Pesan :", jumlahpesan1)
                                            print("Harga :", harga1)
                                            print("Diskon :", diskon1 + (harga1 * 10/100))
                                            print("--------------------------")
                                            print("Jumlah Bayar :", totalharga1 - (harga1 * 10/100))
                                            print("------------------------------------------------")
                                            print("Anda mendapatkan diskon Weekend dan E-money sebesar 5 % + 10 %")


                                    else:
                                        print("Metode pembayaran salah, silahkan pilih kembali")
                                        oke1 = 'c'

                            else:
                                totalharga1 = int(harga1)
                                print("--------------------------")
                                print("Tasty Coffe")
                                print("Hari :",hari1)
                                print("--------------------------")
                                print("Menu         :", listnama1)
                                print("Jumlah Pesan :", jumlahpesan1)
                                print("Harga        :", harga1)
                                print("--------------------------")
                                print("Jumlah Bayar :", harga1)
                                print("--------------------------")


                    except ValueError:
                        print("Jumlah pesanan salah, silahkan coba kembali")
                        balik = 'b'


            elif pesan == 'b' or 'B':
                jumlahpesan2 = int(input("masukkan jumlah pesanan ="))
                listnama2    = Menu[1]
                harga2       = (Harga[1] * jumlahpesan2)

                if jumlahpesan2 >= 3 :
                    diskon2     = int(harga2 * 10/100)
                    totalharga2 = int(harga2 - diskon2)
                    print("--------------------------")
                    print("Tasty Coffe")
                    print("Hari :",hari)
                    print("--------------------------")
                    print("Menu         :", listnama2)
                    print("Jumlah Pesan :", jumlahpesan2)
                    print("Harga        :", harga2)
                    print("Diskon       :", diskon2)
                    print("--------------------------")
                    print("Jumlah Bayar :", totalharga2)
                    print("--------------------------")

                else:
                    totalharga2 = int(harga2)
                    diskon2     = int(harga2 * 10/100)
                    print("--------------------------")
                    print("Tasty Coffe")
                    print("Hari :",hari)
                    print("--------------------------")
                    print("Menu         :", listnama2)
                    print("Jumlah Pesan :", jumlahpesan2)
                    print("Harga        :", harga2)
                    print("Diskon       :", diskon2)
                    print("--------------------------")
                    print("Jumlah Bayar :", totalharga2)
                    print("--------------------------")

            elif pesan == 'c' or 'C':
                jumlahpesan3 = int(input("masukkan jumlah pesanan ="))
                hari = str(input("Hari apa sekarang ? = "))
                listnama3   = Menu[2]
                harga3       = int(Harga[2] * jumlahpesan3)
                if jumlahpesan3 >= 3 :
                    diskon3     = int(harga3 * 10/100)
                    totalharga3 = int(harga3 - diskon3)
                    print("--------------------------")
                    print("Tasty Coffe")
                    print("Hari :",hari)
                    print("--------------------------")
                    print("Menu         :", listnama3)
                    print("Jumlah Pesan :", jumlahpesan3)
                    print("Harga        :", harga3)
                    print("Diskon       :", diskon3)
                    print("--------------------------")
                    print("Jumlah Bayar :", totalharga3)
                    print("--------------------------")

                else :
                    totalharga3 = int(harga3)
                    print("--------------------------")
                    print("Tasty Coffe")
                    print("Hari :",hari)
                    print("--------------------------")
                    print("Menu         :", listnama3)
                    print("Jumlah Pesan :", jumlahpesan3)
                    print("Harga        :", harga3)
                    print("--------------------------")
                    print("Jumlah Bayar :", totalharga3)
                    print("--------------------------")

            elif pesan == 'd' or 'D':
                jumlahpesan4 = int(input("masukkan jumlah pesanan ="))
                hari = str(input("Hari apa sekarang ? = "))
                listnama4    = Menu[3]
                harga4       = int(Harga[3]*jumlahpesan4)
                if jumlahpesan4 >= 3:
                    diskon4 = int(harga4 * 10/100)
                    totalharga4 = int(harga4 - diskon4)
                    print("--------------------------")
                    print("Tasty Coffe")
                    print("Hari :",hari)
                    print("--------------------------")
                    print("Menu         :", listnama4)
                    print("Jumlah Pesan :", jumlahpesan4)
                    print("Harga        :", harga4)
                    print("Diskon       :", diskon4)
                    print("--------------------------")
                    print("Jumlah Bayar :", totalharga4)
                    print("--------------------------")

                else :
                    diskon4     = int(harga4 * 10/100)
                    totalharga4 = int(harga4)
                    print("--------------------------")
                    print("Tasty Coffe")
                    print("Hari :",hari)
                    print("--------------------------")
                    print("Menu         :", listnama4)
                    print("Jumlah Pesan :", jumlahpesan4)
                    print("Harga        :", harga4)
                    print("Diskon       :", diskon4)
                    print("--------------------------")
                    print("Jumlah Bayar :", totalharga4)
                    print("--------------------------")

            elif pesan == 'e' or 'E':
                jumlahpesan5 = int(input("masukkan jumlah pesanan ="))
                hari = str(input("Hari apa sekarang ? = "))
                listnama5    = Menu[4]
                harga5       = int(Harga[4]*jumlahpesan5)
                if jumlahpesan5 >= 3:
                    diskon5    = int(harga5 * 10/100)
                    totalharga5 = int(harga5 - diskon5)
                    print("--------------------------")
                    print("Tasty Coffe")
                    print("Hari :",hari)
                    print("--------------------------")
                    print("Menu         :", listnama5)
                    print("Jumlah Pesan :", jumlahpesan5)
                    print("Harga        :", harga5)
                    print("Diskon       :", diskon5)
                    print("--------------------------")
                    print("Jumlah Bayar :", totalharga5)
                    print("--------------------------")
                else :
                    totalharga5 = int(harga5)
                    print("--------------------------")
                    print("Tasty Coffe")
                    print("Hari :",hari)
                    print("--------------------------")
                    print("Menu         :", listnama5)
                    print("Jumlah Pesan :", jumlahpesan5)
                    print("Harga        :", harga5)
                    print("Diskon       :", diskon5)
                    print("--------------------------")
                    print("Jumlah Bayar :", totalharga5)
                    print("--------------------------")
            
            elif pesan == 'f' or 'F':
                jumlahpesan6 = int(input("masukkan jumlah pesanan ="))
                hari = str(input("Hari apa sekarang ? = "))
                listnama6    = Menu[5]
                harga6       = int(Harga[5] * jumlahpesan6)
                if jumlahpesan6 >= 4:
                    if hari in Weekdays:
                        diskon6     = int(harga6 * 10/100)
                        totalharga6 = int(harga6 - diskon6)
                        print("--------------------------")
                        print("Tasty Coffe")
                        print("Hari :",hari)
                        print("--------------------------")
                        print("Menu         :", listnama6)
                        print("Jumlah Pesan :", jumlahpesan6)
                        print("Harga        :", harga6)
                        print("Diskon       :", diskon6)
                        print("--------------------------")
                        print("Jumlah Bayar :", totalharga6)
                        print("--------------------------")
                        print("Anda mendapatkan diskon pemesanan sebesar 10% ")

                    elif hari in Weekend:
                        diskon6_2   = int(diskon6 - (harga6*5/100))
                        totalharga6 = int(harga6 - diskon6_2)
                        print("--------------------------")
                        print("Tasty Coffe")
                        print("Hari :",hari)
                        print("--------------------------")
                        print("Menu         :", listnama6)
                        print("Jumlah Pesan :", jumlahpesan6)
                        print("Harga        :", harga6)
                        print("Diskon       :", diskon6)
                        print("--------------------------")
                        print("Jumlah Bayar :", totalharga6)
                        print("--------------------------")
                        print("Anda mendapatkan diskon pemesanan dan weekend sebesar 10% + 5% ")
                else :
                    totalharga6 = int(harga6)
                    print("--------------------------")
                    print("Tasty Coffe")
                    print("Hari :",hari)
                    print("--------------------------")
                    print("Menu         :", listnama6)
                    print("Jumlah Pesan :", jumlahpesan6)
                    print("Harga        :", harga6)
                    print("Diskon       :", diskon6)
                    print("--------------------------")
                    print("Jumlah Bayar :", totalharga6)
                    print("--------------------------")

            elif pesan == 'g' or 'G':
                jumlahpesan7 = int(input("masukkan jumlah pesanan ="))
                hari = str(input("Hari apa sekarang ? = "))
                listnama7    = Menu[6]
                harga7       = int(Harga[6]*jumlahpesan7)
                if jumlahpesan7 >= 4:
                    diskon7    = int(harga7 * 10/100)
                    totalharga7 = int(harga7 - diskon7)
                    print("--------------------------")
                    print("Tasty Coffe")
                    print("Hari :",hari)
                    print("--------------------------")
                    print("Menu         :", listnama7)
                    print("Jumlah Pesan :", jumlahpesan7)
                    print("Harga        :", harga7)
                    print("Diskon       :", diskon7)
                    print("--------------------------")
                    print("Jumlah Bayar :", totalharga7)
                    print("--------------------------")
                else :
                    totalharga7 = int(harga7)
                    print("--------------------------")
                    print("Tasty Coffe")
                    print("Hari :",hari)
                    print("--------------------------")
                    print("Menu         :", listnama7)
                    print("Jumlah Pesan :", jumlahpesan7)
                    print("Harga        :", harga7)
                    print("Diskon       :", diskon7)
                    print("--------------------------")
                    print("Jumlah Bayar :", totalharga7)
                    print("--------------------------")

            elif pesan == 'h' or 'H':
                jumlahpesan8 = int(input("masukkan jumlah pesanan ="))
                hari = str(input("Hari apa sekarang ? = "))
                listnama8    = Menu[7]
                harga8       = int(Harga[7]*jumlahpesan8)
                if jumlahpesan8 >= 4:
                    diskon8     = int(harga8 * 10/100)
                    totalharga8 = int(harga8 - diskon8)
                    print("--------------------------")
                    print("Tasty Coffe")
                    print("Hari :",hari)
                    print("--------------------------")
                    print("Menu         :", listnama8)
                    print("Jumlah Pesan :", jumlahpesan8)
                    print("Harga        :", harga8)
                    print("Diskon       :", diskon8)
                    print("--------------------------")
                    print("Jumlah Bayar :", totalharga8)
                    print("--------------------------")
                else :
                    totalharga8 = int(harga8)
                    print("--------------------------")
                    print("Tasty Coffe")
                    print("Hari :",hari)
                    print("--------------------------")
                    print("Menu         :", listnama8)
                    print("Jumlah Pesan :", jumlahpesan8)
                    print("Harga        :", harga8)
                    print("Diskon       :", diskon8)
                    print("--------------------------")
                    print("Jumlah Bayar :", totalharga8)
                    print("--------------------------")

            else:
                pilihan=input("menu tidak tersedia, silahkan masukkan abjad menu yang tersedia, silahkan ulangi kembali Y/N =")
                if pilihan == ('y'or 'Y') :
                    coba = 'y'

                elif pilihan == ('n' or 'N') :
                    print("======================================\nTerimakasih :) Silahkan datang kembali\n======================================")


        pilihan=input("apakah anda ingin order kembali Y/N =")
        if pilihan == ('y', 'Y') :
            pilihan = 'y'

        elif pilihan == ('n', 'N') :
            print("======================================\nTerimakasih :) Silahkan datang kembali\n======================================")

Pesann()