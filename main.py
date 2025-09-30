import os
from soru_1_degiskenatama import soru1
from soru_2_veritiplerivedonusturme import soru2
from soru_3_aritmetikislemler import soru3
from soru_4_kosulyapisi import soru4
from soru_5_karsilastirma import soru5
from soru_6_basithesapmakinesi import soru6
from soru_7_dongukullanimi import soru7

while True:
    print("1 ) Değişken Atama")
    print("2 ) Veri Tipleri ve Dönüştürme")
    print("3 ) Aritmetik İşlemler")
    print("4 ) Koşul Yapısı (if-else)")
    print("5 ) Karşılaştırma")
    print("6 ) Basit Hesap Makinesi")
    print("7 ) Döngü Kullanımı")
    islem = input("Soruyu Seçin: ")

    if islem == "1":
        os.system('cls')
        soru1()
    elif islem == "2":
        os.system('cls')
        soru2()
    elif islem == "3":
        os.system('cls')
        soru3basari = False
        while not soru3basari:
            soru3basari = soru3()
    elif islem == "4":
        os.system('cls')
        soru4()
    elif islem == "5":
        os.system('cls')
        soru5()
    elif islem == "6":
        os.system('cls')
        soru6()
    elif islem == "7":
        os.system('cls')
        soru7()
    else:
        os.system('cls')
        print("Böyle bir işlem bulunmuyor, lütfen listeden seçim yapın.")

    print("")
    print("")