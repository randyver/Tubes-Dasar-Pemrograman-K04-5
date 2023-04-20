import var
from util import *
from typing import *

def bangunCandi() -> None:
    if (var.currentUser[2] != "jin_pembangun"):
        print("Bangun candi gagal! Bangun candi hanya dapat dilakukan oleh jin pembangun")
    else:
        pasir = randomAngka(1,5)
        batu = randomAngka(1,5)
        air = randomAngka(1,5)

        print(pasir, batu, air)

        pasir_avail = var.bahanBangunan[0][0][2]
        batu_avail = var.bahanBangunan[0][1][2]
        air_avail = var.bahanBangunan[0][2][2]

        if pasir <= pasir_avail and batu <= batu_avail and air <= air_avail:
            var.bahanBangunan[0][0] = ("pasir", "", var.bahanBangunan[0][0][2] - pasir)
            var.bahanBangunan[0][1] = ("batu", "", var.bahanBangunan[0][1][2] - batu)
            var.bahanBangunan[0][2] = ("air", "", var.bahanBangunan[0][2][2] - air)

            idCandi = generateIdCandi()

            if var.candi[1] < 100:
                var.candi = add((idCandi, var.currentUser[0], pasir, batu, air), var.candi)
                print("Candi berhasil dibangun.")
                print(f"Sisa candi yang perlu dibangun: {100-var.candi[1]}.")
            else:
                print("Candi berhasil dibangun.")
                print("Sisa candi yang perlu dibangun: 0.")
        else:
            print("Bahan bangunan tidak mencukupi.")
            print("Candi tidak bisa dibangun!")

    print(var.candi)