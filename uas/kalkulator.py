import math
def pertambahan(a, b):
    hasil = a+b
    return hasil

def pengurangan(a, b):
    hasil = a-b
    return hasil

def perkalian(a, b):
    hasil = a*b
    return hasil

def pembagian(a, b):
    hasil = a/b
    return hasil

def runkali():
    print(' ')
    print('Anda memilih program "Perkalian"')
    a=int(input("Masukan angka pertama: "))
    b=int(input('Masukan angka kedua: '))
    print('hasil perkalian dari',(a),'x',(b),'adalah',(perkalian(a, b)))
    print(' ')

def runbagi():
    print(' ')
    print('Anda memilih program "Pembagian"')
    a=int(input("Masukan angka pertama: "))
    b=int(input('Masukan angka kedua: '))
    print('hasil pembagian dari',(a),':',(b),'adalah',(pembagian(a, b)))
    print(' ')

def runplus():
    print(' ')
    print('Anda memilih program "Pertambahan"')
    a=int(input("Masukan angka pertama: "))
    b=int(input('Masukan angka kedua: '))
    print('hasil pertambahan dari',(a),'+',(b),'adalah',(pertambahan(a, b)))
    print(' ')

def runminus():
    print(' ')
    print('Anda memilih program "Pengurangan"')
    a=int(input('Masukan angka pertama: '))
    b=int(input('Masukan angka kedua: '))
    print('hasil pengurangan dari',(a),'-',(b),'adalah',(pengurangan(a, b)))
    print(' ')

while True:
    print ('Pilih Program: ')
    print ('1. Pertambahan')
    print ('2. Pengurangan')
    print ('3. Perkalian')
    print ('4. Pembagian')
    a=input('Masukan kode program: ')
    if a == '1':
        runplus()
    elif a == '2':
        runminus()
    elif a == '3':
        runkali()
    elif a == '4':
        runbagi()
    else:
        break
