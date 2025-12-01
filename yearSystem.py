def read_year(prompt):
    while True:
        x = input(prompt).strip()
        if x == "":
            print("Hata! Lutfen gecerli bir yil giriniz.")
            continue
        if not (x.lstrip('-').isdigit()):
            print("Hata! Lutfen tam sayi biciminde gecerli bir yil giriniz.")
            continue
        try:
            year = int(x)
            return year
        except ValueError:
            print("Hatalı islem, Lutfen tekrar deneyiniz.")


def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def main():
    print('Artik Yil Kontrolu')
    year = read_year('Yil giriniz (ör. 2012): ')

    if is_leap_year(year):
        print(f"{year} Bu Yil Artik Yildir.")
    else:
        print(f"{year} Bu Yil Artik Yil Degildir.")


if __name__ == '__main__':
    main()
