from math import sqrt

print("Dolf-0650019000040 KALKULATOR PYTHAGORAS\n")

pertanyaan = input("Masukkan sisi mana yang ingin dihitung? (a,b,c) = ")

if pertanyaan == "c" :
    a = int(input("Masukkan  a = "))
    b = int(input("Masukkan  b = "))
    c = sqrt(a*a + b*b)
    print("Panjang sisi c  = ",c)

elif pertanyaan == "a" :
    b = int(input("Masukkan  b = "))
    c = int(input("Masukkan  c = "))
if (c<b):
    print("c tidak valid bos! ")
    c = int(input("Masukkan  c = "))
    a = sqrt(c*c - b*b)
    print("Panjang sisi a  = ",a)
    
    
elif pertanyaan == "b" :
    a = int(input("Masukkan  a = "))
    c = int(input("Masukkan  c = "))
if (c<a):
    print("c tidak valid bos! ")
    c = int(input("Masukkan  c = "))
    b = sqrt(c*c - a*a)
    print("Panjang sisi b  = ",b)