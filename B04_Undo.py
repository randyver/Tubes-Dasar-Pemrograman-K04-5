import var
from util import *
from typing import *

# fungsi untuk menghidupkan kembali jin yang sudah di hapus sebelumnya
# undo akan gagal jika tidak ada jin yang bisa dibangkitkan kembali
# undo juga akan gagal jika username dari jin yang dibangkitkan sudah dipakai
# undo juga akan gagal jika jumlah jin yang ada sudah lebih besar sama dengan 100
# ketika jin dibangkitkan kembali maka candi yang mereka bangun sebelumnya juga akan dibangun kembali dengan id candi yang akan disesuaikan
def undo() -> None:
    if (var.currentUser[2] != "bandung_bondowoso"):# pengecekan role apakah sudah sesuai atau belum
        print("Undo hanya dapat diakses oleh akun Bandung Bondowoso.")
    else:
        if var.stackUndo[1] >= 1: # pengecekan apakah ada jin yang bisa dibangkitkan kembali
            last = getLast()
            user = last[0]
            candis = last[1]
            if filterArr(var.users, lambda x: x[0] == user[0])[1] != 0 or var.users[1] >= 102:# pengecekan apakah jumlah jin sudah >= 100 atau belum dan pengecekan apakah username jin yang mau dibangkitkan sudah ada atau belum
                print("Undo gagal")
            else:
                # jin dibangkitkan kembali
                var.users = add(user, var.users)# menambah jin pada array of user
                if candis[1] != 0:# pengecekan apakah ada candi yang dibangun oleh jin ini atau tidak
                    # pembangunan ulang candi
                    for i in range(candis[1]):
                        id = generateIdCandi()
                        candi = (id, candis[0][i][1], candis[0][i]
                                 [2], candis[0][i][3], candis[0][i][4])
                        var.candi = add(candi, var.candi)
                print("Undo berhasil")
        else:
            print("Tidak ada yang bisa di undo")