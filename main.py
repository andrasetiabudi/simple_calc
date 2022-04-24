#!/usr/bin/python3

# menerima input dari user:
# angka 1
angka1 = int(input("Masukan angka pertama: "))

# angka 2
angka2 = int(input("Masukan angka kedua: "))

# operasi yang dilakukan
    # 1 penjumlahan
    # 2 pengurangan
    # 3 pembagian
    # 4 perkalian
print("""Masukan operasi: 
        1 : penjumlahan
        2 : pengurangan
        3 : penjumlahan
        4 : perkalian
        5 : pembagian dengan pembulatan kebawah""")
operasi = int(input("Masukan operasi:  "))

# melakukan operasi terhada angkanya
    if operasi == 1:
        print(angka1+angka2)
    elif operasi == 2:
        print(angka1-angka2)
    elif operasi == 3:
        print(angka1/angka2)
    elif operasi == 4:
        print(angka1*angka2)
    elif operasi == 5:
        print(angka1//angka2)
