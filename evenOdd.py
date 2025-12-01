def read_int(prompt):
    while True:
        x = input(prompt).strip()
        try:
            if "." in s or "," in x:
                raise ValueError
            return int(x)
        except ValueError:
            print("Gecersiz islem, lutfen tam sayi girin.")


def main():
    n = read_int("tam sayi giriniz: ")
    if n % 2 == 0:
        print(f"Girilen sayi cift: {n}")
    else:
        print(f"Girilen sayi tek: {n}")


if __name__ == "__main__":
    main()
