bakiye = 1000

while True:
    print("\n--- ATM MENÜSÜ ---")
    print("1- Bakiye Sorgulama")
    print("2- Para Cekme")
    print("3- Para Yatirma")
    print("4- Cikis")
    
    secim = input("Yapmak istediginiz islemi seciniz (1-4): ")
    
    if secim == '1':
        print(f"Mevcut bakiyeniz: {bakiye} TL")
        
    elif secim == '2':
        miktar = int(input("Cekmek istediginiz tutari giriniz: "))
        if miktar > bakiye:
            print("Yetersiz bakiye! Islem gerceklestirilemedi.")
        else:
            bakiye -= miktar
            print(f"{miktar} TL cektiniz. Yeni bakiyeniz: {bakiye} TL")
            
    elif secim == '3':
        miktar = int(input("Yatirmak istediginiz tutari giriniz: "))
        bakiye += miktar
        print(f"{miktar} TL yatirdiniz. Yeni bakiyeniz: {bakiye} TL")
        
    elif secim == '4':
        print("Cikis yapiliyor. Iyi gunler dileriz!")
        break
        
    else:
        print("Gecersiz islem! Lutfen tekrar deneyiniz.")