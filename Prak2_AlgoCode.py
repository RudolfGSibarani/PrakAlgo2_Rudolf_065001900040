# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 19:10:40 2021

@author: Rudolf
"""
input1 = int(input("Masukkan angka ke-1: "))
input2 = int(input("Masukkan angka ke-2: "))
input3 = int(input("Masukkan angka ke-3: "))


if (input1 > input2) and (input1 > input3):
    terbesar = input1
elif (input2 > input1) and (input2 > input3):
    terbesar = input2
else:
    terbesar = input3


print("\nAngka yang paling besar adalah:", terbesar)
