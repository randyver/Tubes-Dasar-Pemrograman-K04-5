import var
from util import *
from typing import *

# fungsi untuk bangun candi yang hanya dapat diakses oleh jin pembangun
# jumlah dari masing-masing bahan bangunan ditentukan secara acak dari 1 hingga 5
# jika salah satu bahan bangunan tidak mencukupi, maka pembangunan candi gagal
def bangunCandi() -> None:
    # jika role bukan jin pembangun
    if (var.currentUser[2] != "jin_pembangun"):
        print("Bangun candi gagal! Bangun candi hanya dapat dilakukan oleh jin pembangun")
    # role adalah jin pembangun
    else:
        # ambil satu angka secara acak dari 1 hingga 5
        pasir = randomAngka(1,5)
        batu = randomAngka(1,5)
        air = randomAngka(1,5)

        # bahan bangunan yang tersedia
        pasir_avail = var.bahanBangunan[0][0][2]
        batu_avail = var.bahanBangunan[0][1][2]
        air_avail = var.bahanBangunan[0][2][2]

        # sisa bahan bangunan
        if pasir <= pasir_avail and batu <= batu_avail and air <= air_avail:
            var.bahanBangunan[0][0] = ("pasir", "", var.bahanBangunan[0][0][2] - pasir)
            var.bahanBangunan[0][1] = ("batu", "", var.bahanBangunan[0][1][2] - batu)
            var.bahanBangunan[0][2] = ("air", "", var.bahanBangunan[0][2][2] - air)

            # membuat ID candi
            idCandi = generateIdCandi()

            # jika jumlah candi sudah maksimum (100)
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