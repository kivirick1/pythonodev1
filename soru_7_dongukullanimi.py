def soru7():
    print("Soru:")
    print("Kullanıcıdan bir sayı al.")
    print("1’den bu sayıya kadar olan tüm sayıların toplamını hesaplayıp ekrana yazdır (örnek: 5 girerse 1+2+3+4+5 = 15).")
    print("")

    sayi = int(input("Bir sayı girin: "))
    islem = ""
    toplam = 0
    for s in range(1, sayi+1):
        toplam += s
        if s != sayi:
            islem += f"{s} + "
        else:
            islem += f"{s} = {toplam}"
    print(islem)