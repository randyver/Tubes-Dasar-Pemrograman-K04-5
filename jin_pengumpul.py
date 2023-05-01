# file yang berisi fungsi-fungsi utama yang dimiliki jin_pengumpul
from util import *
import var
from typing import *

# F07 Jin Pengumpul
def kumpul() -> None:
    # SPESIFIKASI
    # prosedur untuk mengumpulkan bahan-bahan yang diperlukan untuk membangun candi
    # prosedur hanya bisa diakses oleh Jin Pengumpul
    # prosedur akan menambah jumlah bahan-bahan yang tersedia di variabel bahanBangunan sebesar angka random (0-5)
    # KAMUS LOKAL
    # jumlahPasir, jumlahBatu, jumlahAir : integer
    # ALGORITMA
    if var.currentUser[2] == "jin_pengumpul":
        jumlahPasir = randomAngka(0, 5) # mendapatkan angka random di rentang 0-5
        jumlahBatu = randomAngka(0, 5) # mendapatkan angka random di rentang 0-5
        jumlahAir = randomAngka(0, 5) # mendapatkan angka random di rentang 0-5
        
        print(f"Jin menemukan {jumlahPasir} pasir, {jumlahBatu} batu, dan {jumlahAir} air.")
        # memperbarui jumlah bahan bangunan
        for i in range(var.bahanBangunan[1]):
            if (var.bahanBangunan[0][i][0] == "pasir"):
                var.bahanBangunan[0][i] = ("pasir", "", var.bahanBangunan[0][i][2] + jumlahPasir)
            elif (var.bahanBangunan[0][i][0] == "batu"):
                var.bahanBangunan[0][i] = ("batu", "", var.bahanBangunan[0][i][2] + jumlahBatu)
            elif (var.bahanBangunan[0][i][0] == "air"):
                var.bahanBangunan[0][i] = ("air", "", var.bahanBangunan[0][i][2] + jumlahAir)
    else: # var.currentUser[2] != "jin_pengumpul"
        print("Kumpul hanya dapat diakses oleh akun Jin Pengumpul.")
        
