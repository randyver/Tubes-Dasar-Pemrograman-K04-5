from util import *
from var import *
from typing import *

def kumpul() -> None:
    if currentUser[2] == 'jin_pengumpul':
        jumlahPasir = randomAngka(0, 5)
        jumlahBatu = randomAngka(0, 5)
        jumlahAir = randomAngka(0, 5)
        for i in range(bahanBangunan[1]):
            if bahanBangunan[0][i][0] == 'pasir':
                bahanBangunan[0][i][2] += jumlahPasir
            elif bahanBangunan[0][i][0] == 'batu':
                bahanBangunan[0][i][2] += jumlahBatu
            elif bahanBangunan[0][i][0] == 'air':
                bahanBangunan[0][i][2] += jumlahAir
        print(f'Jin menemukan {jumlahPasir} pasir, {jumlahBatu} batu, dan {jumlahAir} air.')