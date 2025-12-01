def read_positive_float(prompt):
    while True:
        c = input(prompt).strip()
        try:
            value = float(c)
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("Hatali giris, Lutfen gecerli bir sayi girin.")


def read_nonnegative_int(prompt):
    while True:
        c = input(prompt).strip()
        try:
            if "." in c or "," in c:
                raise ValueError
            value = int(c)
            if value < 0:
                raise ValueError
            return value
        except ValueError:
            print("Hatali giris, Lutfen sifir veya daha buyuk sayi girin.")


def calculate_ticket_price(age, km):
    base_price = km * 2.5
    age_discount = 0.0
    if age <= 12:
        age_discount = 0.50
    elif 12 < age <= 24:
        age_discount = 0.25
    elif age > 65:
        age_discount = 0.30

    price_after_age = base_price * (1 - age_discount)
    long_distance_discount = 0.0
    if km > 100:
        long_distance_discount = 0.20

    final_price = price_after_age * (1 - long_distance_discount)

    return {
        'base_price': base_price,
        'age_discount': age_discount,
        'price_after_age': price_after_age,
        'long_distance_discount': long_distance_discount,
        'final_price': final_price,
    }


def main():
    print("Otobus Bilet Fiyat Hesaplayici")
    age = read_nonnegative_int("Lutfen Yasinizi giriniz (tam sayi): ")
    km = read_positive_float("Lutfen gidilecek mesafeyi kilometre cinsinden giriniz: ")

    result = calculate_ticket_price(age, km)

    print("\nHesaplamanin Sonucu:")
    print(f"- Normal ucret (km * 2.5): {result['base_price']:.2f} TL")
    if result['age_discount'] > 0:
        print(f"- Yas indirim Tutari: {int(result['age_discount']*100)}% => {result['price_after_age']:.2f} TL")
    else:
        print(f"- Yas indirimi: Yok => {result['price_after_age']:.2f} TL")

    if result['long_distance_discount'] > 0:
        print(f"- Uzun mesafe indirimi Tutari: {int(result['long_distance_discount']*100)}% => {result['final_price']:.2f} TL")
    else:
        print(f"- Uzun mesafe indirimi: Yok => {result['final_price']:.2f} TL")

    print(f"\nToplam Tutar: {result['final_price']:.2f} TL")


if __name__ == '__main__':
    main()
