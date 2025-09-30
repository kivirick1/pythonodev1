def soru4():
    print("Soru:")
    print("Kullanıcıdan bir sayı al.")
    print("Eğer sayı çift ise “Çift sayı” yazdır, tek ise “Tek sayı” yazdır.")
    print("")

    sayi = int(input("Bir sayı girin: "))

    if sayi % 2 == 0:
        print("Girilen sayı çift.")
    else:
        print("Girilen sayı tek.")