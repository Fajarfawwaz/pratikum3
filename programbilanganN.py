max=0

while True:   
    N = int(input("masukan angka: "))

    if N == 0:
        print(f"angaka terbesar adalah: {max}")
        break
    if N > max:
        max = N