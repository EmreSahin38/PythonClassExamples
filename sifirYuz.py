print("1 ile 100 arasindaki asal sayilar:")

for sayi in range(2, 101):
    is_asal = True
    for i in range(2, int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            is_asal = False
            break
            
    if is_asal:
        print(sayi, end=" ")
print()