from util import *
import var
from typing import *

def kumpul() -> None:
    # SPESIFIKASI
    # fungsi untuk mengumpulkan bahan-bahan yang diperlukan untuk membangun candi
    # fungsi hanya bisa diakses oleh Jin Pengumpul
    # fungsi akan menambah jumlah bahan-bahan yang tersedia di variabel bahanBangunan sebesar angka random (0-5)
    # KAMUS LOKAL
    # jumlahPasir, jumlahBatu, jumlahAir : integer
    # ALGORITMA
    if var.currentUser[2] == "jin_pengumpul":
        jumlahPasir = randomAngka(0, 5) # mendapatkan angka random di rentang 0-5
        jumlahBatu = randomAngka(0, 5) # mendapatkan angka random di rentang 0-5
        jumlahAir = randomAngka(0, 5) # mendapatkan angka random di rentang 0-5
        
        print(f"Jin menemukan {jumlahPasir} pasir, {jumlahBatu} batu, dan {jumlahAir} air.")
        
        var.bahanBangunan[0][0] = ("pasir", "", var.bahanBangunan[0][0][2] + jumlahPasir)
        var.bahanBangunan[0][1] = ("batu", "", var.bahanBangunan[0][1][2] + jumlahBatu)
        var.bahanBangunan[0][2] = ("air", "", var.bahanBangunan[0][2][2] + jumlahAir)
    else: # var.currentUser[2] != "jin_pengumpul"
        print("Kumpul hanya dapat diakses oleh akun Jin Pengumpul.")
        
