def read_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Gecersiz Girdi Lutfen Tekrar Giriniz!")


def main():
    x = read_number("Ilk degeri girin: ")
    y = read_number("ikinci degeri girin: ")

    if x > y:
        print(f"Buyuk olan sayi: {x}")
    elif b > a:
        print(f"Buyuk olan sayi: {y}")
    else:
        print(f"Iki sayi esit: {x}")


if __name__ == "__main__":
    main()
