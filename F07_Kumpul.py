from util import *
import var
from typing import *

def kumpul() -> None:
    if var.currentUser[2] == 'jin_pengumpul':
        jumlahPasir = randomAngka(0, 5)
        jumlahBatu = randomAngka(0, 5)
        jumlahAir = randomAngka(0, 5)
        
        print(f'Jin menemukan {jumlahPasir} pasir, {jumlahBatu} batu, dan {jumlahAir} air.')
        
        var.bahanBangunan[0][0] = ("pasir", "", var.bahanBangunan[0][0][2] + jumlahPasir)
        var.bahanBangunan[0][1] = ("batu", "", var.bahanBangunan[0][1][2] + jumlahBatu)
        var.bahanBangunan[0][2] = ("air", "", var.bahanBangunan[0][2][2] + jumlahAir)
    else:
        print("Kumpul hanya dapat diakses oleh akun Jin Pengumpul.")
        