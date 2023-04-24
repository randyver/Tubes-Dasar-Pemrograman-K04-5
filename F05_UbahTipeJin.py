import var
from util import *
from typing import *

# fungsi untuk mengubah role jin dari pembangun ke pengumpul atau sebaliknya
# ubah jin akan gagal jika username jin yang diinputkan tidak ada
# ketika jin pembangun diubah rolenya, candi yang dibangunnya akan tetap ada dan jin tersebut masih berpeluang untuk menjadi jin terajin atau termalas
def ubahJin() -> None:
    if (var.currentUser[2] != "bandung_bondowoso"):# pengecekan role apakah sudah sesuai atau belum
        print("Ubah jin hanya dapat diakses oleh akun Bandung Bondowoso.")
    else:
        usernameJin = input("Masukkan username Jin: ")
        index = getIndex(var.users, lambda x: x[0] == usernameJin)
        if index != -1: # pengecekan apakah username jin yang diinputkan ada atau tidak
            #mengubah tipe jin
            jin = var.users[0][index]
            tipeJin = "Pengumpul" if jin[2] == "jin_pengumpul" else "Pembangun"
            masukan = input('Jin ini bertipe "' + tipeJin + '". Yakin ingin mengubah ke tipe "' +
                            ("Pengumpul" if tipeJin == "Pembangun" else "Pembangun") + '" (Y/N)? ')
            if (masukan == "Y"):
                var.users[0][index] = (
                    jin[0], jin[1], ("jin_pengumpul" if tipeJin == "Pembangun" else "jin_pembangun"))
                print("Jin telah berhasil diubah")
        else:
            print("Tidak ada jin dengan username tersebut.")