import var
from util import *
from typing import *

# fungsi untuk login menjadi suatu user (bandung/jonggrang/jin)
# fungsi ini hanya bisa dijalankan jika belum ada user yang sedang login sebelumnya
# login akan gagal jika username tidak terdaftar atau password salah
def login() -> None:
    # cek apakah ada yang sudah login sebelumnya atau tidak
    if var.currentUser != ("", "", ""):
        print("Login gagal!")
        print('Anda telah login dengan username ' +
              var.currentUser[0] + ', silahkan lakukan "logout" sebelum melakukan login kembali.')
    else:
        # menerima input
        username = input("Username: ")
        password = input("Password: ")

        user = filterArr(var.users, lambda x: x[0] == username)
        if user[1] != 0:  # pengecekan apakah username ada atau tidak
            # pengecekan apakah password sudah benar atau tidak
            if password == user[0][0][1]:
                var.currentUser = user[0][0]
                print("")
                print("Selamat datang, " + username + "!")
                print(
                    'Masukkan command "help" untuk daftar command yang dapat kamu panggil.')
            else:
                print("Password salah!")
        else:
            print("Username tidak terdaftar!")
