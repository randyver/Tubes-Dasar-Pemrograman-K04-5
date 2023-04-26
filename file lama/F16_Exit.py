import var
from util import *
from typing import *
import os

def keluar():
    while True:
        simpan = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        if simpan.lower() == 'y':
            # Simpan permainan
            save(jumlahusers, users, jumlahcandi, candi, bahan)
            print("Permainan disimpan.")
            break
        elif simpan.lower() == 'n':
            # Keluar dari permainan tanpa menyimpan
            print("Permainan tidak disimpan.")
            break
        else:
            # Input tidak valid, tanyakan lagi
            print("Input tidak valid, silakan masukkan y atau n.")
