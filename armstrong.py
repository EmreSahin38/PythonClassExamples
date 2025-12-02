
sayi_str = input("Lutfen bir sayi giriniz: ")

if sayi_str.isdigit():
    basamak_toplami = 0
    for rakam in sayi_str:
        basamak_toplami += int(rakam)
    
    print(f"Girdiginiz sayinin basamaklari toplami: {basamak_toplami}")
    basamak_sayisi = len(sayi_str)
    armstrong_toplami = 0
    
    for rakam in sayi_str:
        armstrong_toplami += int(rakam) ** basamak_sayisi
        
    girilen_sayi = int(sayi_str)
    
    if girilen_sayi == armstrong_toplami:
        print(f"{girilen_sayi} bir Armstrong sayisidir.")
    else:
        print(f"{girilen_sayi} bir Armstrong sayisi DEGILDIR. (Hesaplanan: {armstrong_toplami})")
else:
    print("Lutfen gecerli bir tamsayi giriniz.")