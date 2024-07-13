# NIM: 3312001105
# Nama: Kurniawan

print(
    "Hello World!\n",
    "My Name Is: Jodi Kurniawan\n",
    "With NIM: 3312001105\n"
)

# hitung luas persegi panjang
def luas_persegi_panjang():
    p = int(input('Masukan panjang persegi: '))
    l = int(input('Masukan lebar persegi: '))
    luas = p * l
    print('Luas persegi adalah: ', luas)

luas_persegi_panjang()

# hitung luas lingkaran
def luas_lingkaran():
    r = int(input('Masukan jari-jari lingkaran: '))
    luas = 3.14 * r * r
    print('Luas lingkaran adalah: ', luas)

luas_lingkaran()