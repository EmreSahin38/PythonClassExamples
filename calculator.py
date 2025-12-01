import argparse
import sys


def to_number(c):
    try:
        return int(c)
    except Exception:
        try:
            return float(c)
        except Exception:
            raise argparse.ArgumentTypeError(f"Invalid number: {c}")


def main():
    parser = argparse.ArgumentParser(description='Hesap Makinesi: + - * / islemleri (iki sayi).')
    parser.add_argument('x', nargs='?', type=to_number, help='Ilk Deger')
    parser.add_argument('y', nargs='?', type=to_number, help='Ikinci Deger')
    args = parser.parse_args()

    if args.x is None or args.y is None:
        try:
            x = to_number(input("Ilk degeri girin!: ").strip())
            y = to_number(input("Ikinci Degeri girin!: ").strip())
        except (EOFError, KeyboardInterrupt):
            print('\nIslem iptal edildi!')
            sys.exit(1)
        except Exception as e:
            print('Hatali giris:', e)
            sys.exit(1)
    else:
        x = args.x
        y = args.y

    print('Toplama:', x + y)
    print('Cikarma:', x - y)
    print('Carpma:', x * y)
    if y == 0:
        print('Bolme: Hata (0'a bölünemez)')
    else:
        print('Bolme:', x / y)


if __name__ == '__main__':
    main()
