def soru3():
    print("Soru:")
    print("Bir dikdörtgenin kısa ve uzun kenarını kullanıcıdan iste.")
    print("Alanını ve çevresini hesaplayıp ekrana yazdır.")
    print("")

    sayi1 = int(input("Uzun kenarın uzunluğunu girin: "))
    sayi2 = int(input("Kısa kenarın uzunluğunu girin: "))

    kisakenar = 0
    uzunkenar = 0

    if sayi1 == 0 or sayi2 == 0:
        print("Kenar uzunlukları 0 olamaz.")
        return False
    elif sayi1 > sayi2:
        uzunkenar = sayi1
        kisakenar = sayi2
    else:
        uzunkenar = sayi2
        kisakenar = sayi1

    print(f"Uzun Kenar: {uzunkenar} | Kısa Kenar: {kisakenar}")
    print(f"Alan: {uzunkenar * kisakenar} | Çevre: {(kisakenar * 2) + (uzunkenar * 2)}")
    return True