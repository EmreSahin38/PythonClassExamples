def read_number(prompt):
    while True:
        c = input(prompt).strip()
        try:
            if c == "":
                raise ValueError
            try:
                return int(c)
            except ValueError:
                return float(c)
        except ValueError:
            print("Gecersiz deger, lutfen tekrar deneyiniz.")


def read_operation(prompt):
    valid = ['+', '-', '*', '/', '**', '%']
    while True:
        op = input(prompt).strip()
        if op in valid:
            return op
        print(f"Gecersiz islemler, uygun islemler: {', '.join(valid)}")


def calculate(x, y, z):
    try:
        if z == '+':
            return x + y
        if z == '-':
            return x - y
        if z == '*':
            return x * y
        if z == '/':
            if y == 0:
                return '0 hatasi!'
            return x / y
        if z == '**':
            return x ** y
        if z == '%':
            if y == 0:
                return 'Mod alinamaz!'
            return x % y
    except Exception as e:
        return f'Error: {e}'


def main():
    print('Basit Hesap Makinesi')
    x = read_number('c1 = kullanıcı girdisi: ')
    y = read_number('c2 = kullanici girdisi: ')
    z = read_operation('islem (+ - * / ** %): ')

    result = calculate(x, y, z)

    print('\nSonuc:')
    print(f"{x} {z} {y} = {result}")


if __name__ == '__main__':
    main()
