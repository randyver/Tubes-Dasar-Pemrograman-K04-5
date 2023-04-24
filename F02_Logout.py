import var
from util import *
from typing import *

# fungsi logout untuk keluar dari akun
# user akan kehilangan akses dari akun sebelumnya saat menjalankan fungsi ini
# setelah fungsi ini dijalankan, maka user lain dapat login
def logout() -> None:
    # jika tidak ada user yang sedang menjalankan game
    if var.currentUser == ("","",""):
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
    # jika ada user yang sedang menjalankan game maka tuple akan kosong saat logout
    else:
        var.currentUser = ("","","")