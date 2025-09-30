def soru6():
    print("Soru:")
    print("Kullanıcıdan iki sayı ve bir işlem türü (+, -, *, /) iste.")
    print("Girilen işleme göre sonucu ekrana yazdır.")
    print("")

    sayi1 = int(input("1. sayıyı girin: "))
    sayi2 = int(input("2. sayıyı girin: "))
    islem = input("İşlem türünü girin (+, -, *, /): ")

    if islem == "+":
        print(f"{sayi1} + {sayi2} = {sayi1 + sayi2}")
    elif islem == "-":
        print(f"{sayi1} - {sayi2} = {sayi1 - sayi2}")
    elif islem == "*":
        print(f"{sayi1} * {sayi2} = {sayi1 * sayi2}")
    elif islem == "/":
        print(f"{sayi1} / {sayi2} = {sayi1 / sayi2}")
    else:
        print("Hatalı işlem türü belirttiniz +, -, *, / işlemlerinden birini belirtmeniz gerekiyor.")