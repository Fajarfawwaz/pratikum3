a = int(input("masukkan bilangan pertama: "))
b = int(input("masukkan bilangan kedua: "))
c = int(input("masukkan bilangan ketiga: "))

if a > b and a > c:
    print(f"angka lebih besar adalah {a}")
elif b > a and b > c:
    print(f"angka lebih besar adalah {b}")
else:
    print(f"angka lebih besar adalah {c}")