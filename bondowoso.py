# file yang berisi fungsi-fungsi utama yang dimiliki role bandung_bondowoso
from util import *
import var
from typing import *

# F03 Summon Jin


def summonJin() -> None:
    # SPESIFIKASI
    # prosedur untuk memanggil jin pengumpul atau jin pembangun dan menambahkannya sebagai user
    # prosedur hanya bisa diakses oleh Bandung Bondowoso
    # jumlah maksimal jin yang bisa di-summon adalah 100, username jin haruslah unik (tidak ada user dengan username sama), dan panjang password jin berada di rentang 5 sampai 25 (inklusif)
    # KAMUS LOKAL
    # jenisJin, role, usernameJin, passwordJin : string
    # validUsername : boolean
    # ALGORITMA
    if var.currentUser[2] == "bandung_bondowoso":
        if var.users[1] < 103:  # jumlah jin yang sudah di-summon < 100
            print("Jenis jin yang dapat dipanggil:", " (1) Pengumpul - Bertugas mengumpulkan bahan bangunan",
                  " (2) Pembangun - Bertugas membangun candi", "", sep='\n')
            # loop menerima masukan jenis jin dan berhenti jika masukan jenis jin valid: (1) jin pengumpul, (2) jin pembangun
            while True:
                jenisJin = input("Masukkan nomor jenis jin yang ingin dipanggil: ")
                if jenisJin == "1" or jenisJin == "2":
                    break
                else:
                    print(f"\nTidak ada jenis jin bernomor \"{jenisJin}\"!\n")
            # memberikan role pada jin
            if jenisJin == "1":
                print(f"\nMemilih jin \"Pengumpul\".\n")
                role = "jin_pengumpul"
            elif jenisJin == "2":
                print(f"\nMemilih jin \"Pembangun\".\n")
                role = "jin_pembangun"
            # loop menerima masukan username jin dan berhenti jika masukan username jin valid (tidak ada user lain di variabel users dengan username yang sama dengan masukan pengguna)
            while True:
                validUsername = True
                usernameJin = input("Masukkan username jin: ")
                for i in range(0, var.users[1]):
                    if usernameJin == var.users[0][i][0]:
                        print(f"\nUsername \"{usernameJin}\" sudah diambil!\n")
                        validUsername = False
                        break
                if validUsername:
                    break
            # loop menerima masukan password jin dan berhenti jika masukan password jin valid (panjang username jin berada di rentang 5 sampai 25 (inklusif))
            while True:
                passwordJin = input("Masukkan password jin: ")
                if 5 <= len(passwordJin) <= 25:
                    break
                else:
                    print("\nPassword panjangnya harus 5-25 karakter!\n")
            # menambahkan jin ke variabel users
            var.users = add(
                data=(usernameJin, passwordJin, role), arr=var.users)
            print("\nMengumpulkan sesajen...", "Menyerahkan sesajen...",
                  "Membacakan mantra...", sep='\n')
            print(f"\nJin {usernameJin} berhasil dipanggil!")
        else:  # jumlah jin yang telah di-summon == 100
            print(
                "Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
    else:  # var.currentUser[2] != "bandung_bondowoso"
        print("Summon jin hanya dapat diakses oleh akun Bandung Bondowoso.")

# F04 Hilangkan Jin
# fungsi untuk menghapus jin yang sudah dipanggil sebelumnya, hapus jin akan gagal jika username jin yang diinputkan tidak ada
# saat jin dihapus maka semua candi yang sudah dibangun oleh jin tersebut juga akan dihapus


def hapusJin() -> None:
    # pengecekan role apakah sudah sesuai atau belum
    if (var.currentUser[2] != "bandung_bondowoso"):
        print("Hapus jin hanya dapat diakses oleh akun Bandung Bondowoso.")
    else:
        # pengambilan input username jin yang mau dihapus
        usernameJin = input("Masukkan username Jin: ")
        # pengecekan apakah username jin tersebut ada atau tidak
        if filterArr(var.users, lambda x: x[0] == usernameJin)[1] != 0:
            masukan = input(
                "Apakah anda yakin ingin menghapus jin dengan username " + usernameJin + " (Y/N)? ")
            if masukan == "y" or masukan == "Y":
                deletedUser = filterArr(
                    var.users, lambda x: x[0] == usernameJin)[0][0]
                if deletedUser[2] == "jin_pembangun":
                    deletedCandi = filterArr(
                        var.candi, lambda x: x[1] == usernameJin)
                    dataUndo = (deletedUser, deletedCandi)
                elif deletedUser[2] == "jin_pengumpul":
                    dataUndo = (deletedUser, [(), 0])

                # menambah data jin yang dihapus ke stack undo
                var.stackUndo = add(dataUndo, var.stackUndo)

                # menghapus jin dari array of user dan menghapus candi yang telah dibangunnya dari array of candi
                var.users = delete(var.users,
                                   lambda x: x[0] == usernameJin)
                var.candi = delete(var.candi,
                                   lambda x: x[1] == usernameJin)
                print("Jin telah berhasil dihapus dari alam gaib.")
        else:
            print("Tidak ada jin dengan username tersebut.")

# FO5 Ubah Tipe Jin
# fungsi untuk mengubah role jin dari pembangun ke pengumpul atau sebaliknya
# ubah jin akan gagal jika username jin yang diinputkan tidak ada
# ketika jin pembangun diubah rolenya, candi yang dibangunnya akan tetap ada dan jin tersebut masih berpeluang untuk menjadi jin terajin atau termalas


def ubahJin() -> None:
    # pengecekan role apakah sudah sesuai atau belum
    if (var.currentUser[2] != "bandung_bondowoso"):
        print("Ubah jin hanya dapat diakses oleh akun Bandung Bondowoso.")
    else:  # var.currentUser[2] == "bandung_bondowoso"
        usernameJin = input("Masukkan username Jin: ")  # (string)
        index = getIndex(var.users, lambda x: x[0] == usernameJin and x[2]
                         != "bandung_bondowoso" and x[2] != "roro_jonggrang")  # (integer)
        if index != -1:  # pengecekan apakah username jin yang diinputkan ada atau tidak
            # mengubah tipe jin
            jin = var.users[0][index]  # (user)
            # (string)
            tipeJin = "Pengumpul" if jin[2] == "jin_pengumpul" else "Pembangun"
            masukan = input('Jin ini bertipe "' + tipeJin + '". Yakin ingin mengubah ke tipe "' +
                            ("Pengumpul" if tipeJin == "Pembangun" else "Pembangun") + '" (Y/N)? ')  # (string)
            if masukan == "y" or masukan == "Y":
                var.users[0][index] = (
                    jin[0], jin[1], ("jin_pengumpul" if tipeJin == "Pembangun" else "jin_pembangun"))
                print("\nJin telah berhasil diubah")
        else:  # index == -1
            print("\nTidak ada jin dengan username tersebut.")

# F08 Batch Kumpul
# fungsi untuk mengumpulkan bahan dengan semua jin pengumpul yang dimiliki oleh bandung bondowoso
# fungsi ini akan gagal jika bandung bondowoso tidak memiliki jin pengumpul sama sekali


def batchKumpul() -> None:
    # pengecekan role apakah sudah sesuai atau belum
    if (var.currentUser[2] != "bandung_bondowoso"):
        print("Batch kumpul hanya dapat diakses oleh akun Bandung Bondowoso.")
    else:
        jins = filterArr(
            var.users, lambda x: x[2] == "jin_pengumpul")  # mendapatkan semua jin pengumpul

        if jins[1] == 0:  # pengecekan apakah jin pengumpul ada atau tidak
            print(
                "Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
        else:
            sumPasir = 0  # (integer)
            sumBatu = 0  # (integer)
            sumAir = 0  # (integer)
            print("Mengerahkan " + str(jins[1]) +
                  " jin untuk mengumpulkan bahan.")
            for i in range(jins[1]):
                # penentuan jumlah bahan yang berhasil dikumpulkan oleh satu orang jin
                pasir = randomAngka(0, 5)  # (integer)
                batu = randomAngka(0, 5)  # (integer)
                air = randomAngka(0, 5)  # (integer)

                sumPasir = sumPasir + pasir
                sumBatu = sumBatu + batu
                sumAir = sumAir + air

            # menambah bahan yang didapat ke dakam array of nahan
            print("Jin menemukan total " + str(sumPasir) + " pasir, " +
                  str(sumBatu) + " batu, dan " + str(sumAir) + " air.")
            for i in range(var.bahanBangunan[1]):
                if (var.bahanBangunan[0][i][0] == "pasir"):
                    var.bahanBangunan[0][i] = (
                        "pasir", "", var.bahanBangunan[0][i][2] + sumPasir)
                elif (var.bahanBangunan[0][i][0] == "batu"):
                    var.bahanBangunan[0][i] = (
                        "batu", "", var.bahanBangunan[0][i][2] + sumBatu)
                elif (var.bahanBangunan[0][i][0] == "air"):
                    var.bahanBangunan[0][i] = (
                        "air", "", var.bahanBangunan[0][i][2] + sumAir)


# F08 Batch Bangun
# fungsi untuk membangun candi dengan semua jin pembangun yang dimiliki bandung bondowoso
# fungsi ini akan gagal ketika jumlah bahan bangunan tidak cukup
# ketika candi yang dibangun sudah lebih besar sama dengan 100 maka candi pada fungsi ini akan tetap dibangun namun tidak akan tercatat
def batchBangun() -> None:
    # pengecekan role apakah sudah sesuai atau belum
    if (var.currentUser[2] != "bandung_bondowoso"):
        print("Batch bangun hanya dapat diakses oleh akun Bandung Bondowoso.")
    else:
        indexPasir = getIndex(
            var.bahanBangunan, lambda x: x[0] == "pasir")  # (integer)
        indexBatu = getIndex(
            var.bahanBangunan, lambda x: x[0] == "batu")  # (integer)
        indexAir = getIndex(var.bahanBangunan,
                            lambda x: x[0] == "air")  # (integer)
        # mendapatkan semua jin pembangaun dari array user (arrUser)
        jins = filterArr(var.users, lambda x: x[2] == "jin_pembangun")
        # (array[0..jins[1]-1] of array[0..2] of integer)
        bahan = [(0, 0, 0) for i in range(jins[1])]

        if jins[1] == 0:  # pengecekan apakah jin pengumpul ada atau tidak
            print(
                "Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
        else:
            sumPasir = 0  # (integer)
            sumBatu = 0  # (integer)
            sumAir = 0  # (integer)
            for i in range(jins[1]):
                # penentuan jumlah bahan bangunan yang digunakan untuk membangun 1 candi
                pasir = randomAngka(1, 5)  # (integer)
                batu = randomAngka(1, 5)  # (integer)
                air = randomAngka(1, 5)  # (integer)

                bahan[i] = (pasir, batu, air)  # (array[0..2] of integer)

                sumPasir = sumPasir + pasir
                sumBatu = sumBatu + batu
                sumAir = sumAir + air
            print("Mengerahkan " + str(jins[1]) + " jin untuk membangun candi dengan total bahan " + str(
                sumPasir) + " pasir, " + str(sumBatu) + " batu, dan " + str(sumAir) + " air.")

            # pengecekan apakah bahan bangunan yang dimiiiki cukup atau tidak
            cukup = True
            if var.bahanBangunan[0][indexPasir][2] < sumPasir:
                cukup = False
            if var.bahanBangunan[0][indexBatu][2] < sumBatu:
                cukup = False
            if var.bahanBangunan[0][indexAir][2] < sumAir:
                cukup = False

            if cukup:
                # mengurangi jumlah bahan bangunan di array of bahan
                var.bahanBangunan[0][indexPasir] = (
                    "pasir", "", var.bahanBangunan[0][indexPasir][2] - sumPasir)
                var.bahanBangunan[0][indexBatu] = (
                    "batu", "", var.bahanBangunan[0][indexBatu][2] - sumBatu)
                var.bahanBangunan[0][indexAir] = (
                    "air", "", var.bahanBangunan[0][indexAir][2] - sumAir)

                # membangun candi
                for i in range(jins[1]):
                    idCandi = generateIdCandi()
                    if var.candi[1] < 100:
                        var.candi = add(
                            (idCandi, jins[0][i][0], bahan[i][0], bahan[i][1], bahan[i][2]), var.candi)

                print("Jin berhasil membangun total " +
                      str(jins[1]) + " candi.")
            else:
                pasirKurang = sumPasir - var.bahanBangunan[0][indexPasir][2]
                batuKurang = sumBatu - var.bahanBangunan[0][indexBatu][2]
                airKurang = sumAir - var.bahanBangunan[0][indexAir][2]

                if pasirKurang < 0:
                    pasirKurang = 0
                if batuKurang < 0:
                    batuKurang = 0
                if airKurang < 0:
                    airKurang = 0
                print("Bangun gagal. Kurang " + str(pasirKurang) + " pasir, " +
                      str(batuKurang) + " batu, dan " + str(airKurang) + " air.")

# F09 Ambil Laporan Jin
# fungsi untuk menampilkan informasi seputar jin seperti total jin, total jin pada setiap role, jin terajin, jin termalas, dan jumlah bahan bangunan yang dimiliki
# jin terajin adalah jin yang membangun candi paling banyak
# jin termalas adalah jin yang membangun candi paling sedikit


def laporanJin() -> None:
    # pengecekan role apakah sudah sesuai atau belum
    if (var.currentUser[2] != "bandung_bondowoso"):
        print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")
    else:  # var.currentUser[2] == "bandung_bondowoso"
        jinPengumpul = filterArr(
            var.users, lambda x: x[2] == "jin_pengumpul")  # (arrUser)
        jinPembangun = filterArr(
            var.users, lambda x: x[2] == "jin_pembangun")  # (arrUser)
        totalJinPengumpul = jinPengumpul[1]  # (integer)
        totalJinPembangun = jinPembangun[1]  # (integer)
        totalJin = totalJinPembangun + totalJinPengumpul  # (integer)
        jins = filterArr(
            var.users, lambda x: x[2] == "jin_pengumpul" or x[2] == "jin_pembangun")  # (arrUser)

        jinTerajin = "-"  # (string)
        jinTermalas = "-"  # (string)
        maxCandi = -9999  # (integer)
        minCandi = 9999  # (integer)
        if (totalJin > 0):  # pengecekan apakah bandung bondowoso mempunyai jin atau tidak
            for i in range(0, jins[1]):
                banyakCandi = filterArr(
                    var.candi, lambda x: x[1] == jins[0][i][0])[1]
                print("candi: " + str(banyakCandi))

                if not(banyakCandi == 0 and jins[0][i][2] == "jin_pengumpul"):  
                    # mencari jin terajin
                    if banyakCandi > maxCandi:
                        maxCandi = banyakCandi
                        jinTerajin = jins[0][i][0]
                    elif banyakCandi == maxCandi:
                        if jins[0][i][0] < jinTerajin:
                            jinTerajin = jins[0][i][0]

                    # mencari jin termalas
                    if banyakCandi < minCandi:
                        minCandi = banyakCandi
                        jinTermalas = jins[0][i][0]
                    elif banyakCandi == minCandi:
                        if jins[0][i][0] > jinTermalas:
                            jinTermalas = jins[0][i][0]

        totalPasir = 0  # (integer)
        totalBatu = 0  # (integer)
        totalAir = 0  # (integer)
        for i in range(var.bahanBangunan[1]):
            if (var.bahanBangunan[0][i][0] == "pasir"):
                totalPasir = var.bahanBangunan[0][i][2]  # (integer)
            elif (var.bahanBangunan[0][i][0] == "batu"):
                totalBatu = var.bahanBangunan[0][i][2]  # (integer)
            elif (var.bahanBangunan[0][i][0] == "air"):
                totalAir = var.bahanBangunan[0][i][2]  # (integer)

        # menampilkan informasi ke layar
        print("\n> Total Jin: " + str(totalJin))
        print("> Total Jin Pengumpul: " + str(totalJinPengumpul))
        print("> Total Jin Pembangun: " + str(totalJinPembangun))
        print("> Jin Terajin: " + jinTerajin)
        print("> Jin Termalas: " + jinTermalas)
        print("> Jumlah Pasir: " + str(totalPasir) + " unit")
        print("> Jumlah Batu: " + str(totalBatu) + " unit")
        print("> Jumlah Air: " + str(totalAir) + " unit")

# F10 Ambil Laporan Candi
# fungsi untuk mengambil laporan candi meliputi total bahan bangunan yang telah digunakan
# fungsi ini hanya dapat diakses oleh bandung bondowoso
# menentukan ID candi termahal dan termurah beserta harganya


def laporanCandi() -> None:
    if var.currentUser[2] != "bandung_bondowoso":
        print("Ambil laporan candi gagal! Laporan candi hanya dapat diakses oleh Bandung Bondowoso.")

    # jika user adalah bandung bondowoso
    else:
        # inisialisasi
        total_candi = var.candi[1]
        total_pasir = 0
        total_batu = 0
        total_air = 0
        harga_termahal = 0
        harga_termurah = 0
        id_termahal = ""
        id_termurah = ""

        if total_candi > 0:
            # menjumlahkan semua bahan bangunan yang dipakai
            for i in range(total_candi):
                total_pasir += var.candi[0][i][2]
                total_batu += var.candi[0][i][3]
                total_air += var.candi[0][i][4]

            # inisialisasi harga termahal, harga termurah, id termahal, dan id termurah
            harga_termahal = 10000 * \
                var.candi[0][0][2] + 15000 * \
                var.candi[0][0][3] + 7500*var.candi[0][0][4]
            harga_termurah = harga_termahal
            id_termahal = str(var.candi[0][0][0])
            id_termurah = str(var.candi[0][0][0])

            # menghitung harga setiap candi
            for i in range(total_candi):
                harga = 10000*var.candi[0][i][2] + 15000 * \
                    var.candi[0][i][3] + 7500*var.candi[0][i][4]

                # mengecek dan membandingkan harga setiap candi
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

# B04 Undo
# fungsi untuk menghidupkan kembali jin yang sudah di hapus sebelumnya
# undo akan gagal jika tidak ada jin yang bisa dibangkitkan kembali
# undo juga akan gagal jika username dari jin yang dibangkitkan sudah dipakai
# undo juga akan gagal jika jumlah jin yang ada sudah lebih besar sama dengan 100
# ketika jin dibangkitkan kembali maka candi yang mereka bangun sebelumnya juga akan dibangun kembali dengan id candi yang akan disesuaikan
# ketika jumlah candi sudah >= 100 dan jin yang dibangkitkan kembali pernah membangun candi sebelumnya, maka undo tetap berhasil hanya saja candi yang lebih tidak akan disimpan


def undo() -> None:
    # pengecekan role apakah sudah sesuai atau belum
    if (var.currentUser[2] != "bandung_bondowoso"):
        print("Undo hanya dapat diakses oleh akun Bandung Bondowoso.")
    else:
        if var.stackUndo[1] >= 1:  # pengecekan apakah ada jin yang bisa dibangkitkan kembali
            last = getLast()  # (undoData)
            jin = last[0]  # (user)
            candis = last[1]  # (arrCandi)
            # pengecekan apakah jumlah jin sudah >= 100 atau belum dan pengecekan apakah username jin yang mau dibangkitkan sudah ada atau belum
            if filterArr(var.users, lambda x: x[0] == jin[0])[1] != 0 or var.users[1] >= 102:
                print(
                    "Undo gagal (username jin sudah ada atau jumlah jin sudah maksimal)")
            else:
                # jin dibangkitkan kembali
                # menambah jin pada array of user
                var.users = add(jin, var.users)
                if candis[1] != 0:  # pengecekan apakah ada candi yang dibangun oleh jin ini atau tidak
                    # pembangunan ulang candi
                    for i in range(candis[1]):
                        id = generateIdCandi()
                        candiTemp = (id, candis[0][i][1], candis[0][i]
                                     [2], candis[0][i][3], candis[0][i][4])
                        if var.candi[1] < 100:
                            var.candi = add(candiTemp, var.candi)
                        else:
                            break
                print("Undo berhasil")
        else:
            print("Tidak ada jin yang bisa dihidupkan kembali")
