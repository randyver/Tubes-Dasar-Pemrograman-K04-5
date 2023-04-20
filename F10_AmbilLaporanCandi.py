import var
from util import *
from typing import *

def laporanCandi() -> None:
    if var.currentUser[2] != "bandung_bondowoso":
        print("Ambil laporan candi gagal! Laporan candi hanya dapat diakses oleh Bandung Bondowoso.")
    else:
        total_candi = var.candi[1]
        total_pasir = 0
        total_batu = 0
        total_air = 0

        for i in range(total_candi):
            total_pasir += var.candi[0][i][2]
            total_batu += var.candi[0][i][3]
            total_air += var.candi[0][i][4]

        harga_termahal = 10000*var.candi[0][0][2] + 15000*var.candi[0][0][3] + 7500*var.candi[0][0][4]
        harga_termurah = harga_termahal
        id_termahal = str(var.candi[0][0][0])
        id_termurah = str(var.candi[0][0][0])

        for i in range(total_candi):
            harga = 10000*var.candi[0][i][2] + 15000*var.candi[0][i][3] + 7500*var.candi[0][i][4]

            if harga > harga_termahal:
                harga_termahal = harga
                id_termahal = str(var.candi[0][i][0])
            
            if harga < harga_termurah:
                harga_termurah = harga
                id_termurah = str(var.candi[0][i][0])

        print(f"> Total Candi: {total_candi}")
        print(f"> Total Pasir yang digunakan: {total_pasir}")
        print(f"> Total Batu yang digunakan: {total_batu}")
        print(f"> Total Air yang digunakan: {total_air}")
        if total_candi > 0:
            print(f"> ID Candi Termahal: {id_termahal} (Rp {harga_termahal})")
            print(f"> ID Candi Termurah: {id_termurah} (Rp {harga_termurah})")
        else:
            print(f"> ID Candi Termahal: -")
            print(f"> ID Candi Termurah: -")