import math

def luas_persegi(sisi):
    return sisi * sisi

def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

def luas_lingkaran(jari):
    return math.pi * jari * jari

print("=== MENU BANGUN DATAR ===")
print("1. Persegi")
print("2. Persegi Panjang")
print("3. Lingkaran")

try:
    pilih = int(input("Pilih menu : "))

    if pilih == 1:
        s = float(input("Masukkan sisi : "))
        print("Luas persegi =", luas_persegi(s))

    elif pilih == 2:
        p = float(input("Masukkan panjang : "))
        l = float(input("Masukkan lebar : "))
        print("Luas persegi panjang =", luas_persegi_panjang(p, l))

    elif pilih == 3:
        r = float(input("Masukkan jari-jari : "))
        print("Luas lingkaran =", luas_lingkaran(r))

    else:
        print("Pilihan tidak valid")

except ValueError:
    print("Input harus berupa angka!")