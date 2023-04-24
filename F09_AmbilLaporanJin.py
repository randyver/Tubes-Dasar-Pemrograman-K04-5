import var
from util import *
from typing import *

# fungsi untuk menampilkan informasi seputar jin seperti total jin, total jin pada setiap role, jin terajin, jin termalas, dan jumlah bahan bangunan yang dimiliki
# jin terajin adalah jin yang membangun candi paling banyak
# jin termalas adalah jin yang membangun candi paling sedikit
def laporanJin() -> None:
    if (var.currentUser[2] != "bandung_bondowoso"):# pengecekan role apakah sudah sesuai atau belum
        print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")
    else:
        jinPengumpul = filterArr(var.users, lambda x: x[2] == "jin_pengumpul")
        jinPembangun = filterArr(var.users, lambda x: x[2] == "jin_pembangun")
        totalJinPengumpul = jinPengumpul[1]
        totalJinPembangun = jinPembangun[1]
        totalJin = totalJinPembangun + totalJinPengumpul

        jinTerajin = "-"
        jinTermalas = "-"
        maxCandi = 0
        minCandi = 0
        if (totalJin > 0): # pengecekan apakah bandung bondowoso mempunyai jin atau tidak
            jinTerajin = var.users[0][0][0]
            jinTermalas = var.users[0][0][0]
            maxCandi = filterArr(var.candi, lambda x: x[1] == var.users[0][0][0])[1]
            minCandi = maxCandi
            for i in range(1, var.users[1]):
                banyakCandi = filterArr(var.candi, lambda x: x[1] == var.users[0][i][0])[1]
                
                # mencari jin terajin
                if banyakCandi > maxCandi:
                    maxCandi = banyakCandi
                    jinTerajin = var.users[0][i][0]
                elif banyakCandi == maxCandi:
                    if var.users[0][i][0] < jinTerajin:
                        jinTerajin = var.users[0][i][0]

                # mencari jin termalas
                if banyakCandi < minCandi:
                    minCandi = banyakCandi
                    jinTermalas = var.users[0][i][0]
                elif banyakCandi == minCandi:
                    if var.users[0][i][0] > jinTermalas:
                        jinTermalas = var.users[0][i][0]

        totalPasir = var.bahanBangunan[0][0][2]
        totalBatu = var.bahanBangunan[0][1][2]
        totalAir = var.bahanBangunan[0][2][2]

        # menampilkan informasi ke layar
        print("\n> Total Jin: " + str(totalJin))
        print("> Total Jin Pengumpul: " + str(totalJinPengumpul))
        print("> Total Jin Pembangun: " + str(totalJinPembangun))
        print("> Jin Terajin: " + jinTerajin)
        print("> Jin Termalas: " + jinTermalas)
        print("> Jumlah Pasir: " + str(totalPasir) + " unit")
        print("> Jumlah Batu: " + str(totalBatu) + " unit")
        print("> Jumlah Air: " + str(totalAir) + " unit")