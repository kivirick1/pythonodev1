def soru5():
    print("Soru:")
    print("Kullanıcıdan yaşını al.")
    print("18 ve üzerindeyse “Reşitsiniz” yazdır, değilse “Reşit değilsiniz” yazdır.")
    print("")

    yas = int(input("Yaşınızı girin: "))

    if yas >= 18:
        print("Reşitsiniz.")
    else:
        print("Reşit değilsiniz.")