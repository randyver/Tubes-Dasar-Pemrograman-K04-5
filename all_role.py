# file yang berisi fungsi-fungsi utama yang dimiliki oleh semua role
import var
from util import *
from typing import *
import argparse
import os

# F01 Login
# fungsi untuk login menjadi suatu user (bandung/jonggrang/jin)
# fungsi ini hanya bisa dijalankan jika belum ada user yang sedang login sebelumnya
# login akan gagal jika username tidak terdaftar atau password salah


def login() -> None:
    # cek apakah ada yang sudah login sebelumnya atau tidak
    if var.currentUser != ("", "", ""):
        print("Login gagal!")
        print('Anda telah login dengan username ' +
              var.currentUser[0] + ', silahkan lakukan "logout" sebelum melakukan login kembali.')
    else:  # var.currentUser == ("", "", "")
        # menerima input
        username = input("Username: ")  # (string)
        password = input("Password: ")  # (string)

        user = filterArr(var.users, lambda x: x[0] == username)
        if user[1] != 0:  # pengecekan apakah username ada atau tidak
            # pengecekan apakah password sudah benar atau tidak
            if password == user[0][0][1]:
                var.currentUser = user[0][0]
                print("")
                print("Selamat datang, " + username + "!")
                print(
                    'Masukkan command "help" untuk daftar command yang dapat kamu panggil.')
            else:  # password != user[0][0][1]
                print("Password salah!")
        else:  # user[1] == 0
            print("Username tidak terdaftar!")

# F02 Logout
# fungsi logout untuk keluar dari akun
# user akan kehilangan akses dari akun sebelumnya saat menjalankan fungsi ini
# setelah fungsi ini dijalankan, maka user lain dapat login


def logout() -> None:
    # jika tidak ada user yang sedang menjalankan game
    if var.currentUser == ("", "", ""):
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
    # jika ada user yang sedang menjalankan game maka tuple akan kosong saat logout
    else:
        var.currentUser = ("", "", "")

# F13 Load
# fungsi yang dijalankan pada awal permainan untuk mengambil data yang diperlukan pada game ini dari sebuah folder


def load() -> None:
    # pengambilan alamat folder data dari input pemain
    parser = argparse.ArgumentParser()
    parser.add_argument("folderPath", nargs= "?", default="")
    args = parser.parse_args()

    folderPath = args.folderPath  # (string)
    # pengecekan apakah alamat folder data yang diberikan kosong atau tidak
    if folderPath == "":
        print("\nTidak ada nama folder yang diberikan!")
        print("\nUsage: python main.py <nama_folder>")
        exit()

    folderPath = "save/" + args.folderPath  # (string)
    # pengecekan apakah alamat folder itu ada atau tidak
    if not os.path.isdir(folderPath):
        print('\nFolder "' + folderPath + '" tidak ditemukan.')
        exit()

    # pembacaan data pada file CSV
    print("\nLoading...")
    readCSV(folderPath)

    print('Selamat datang di program "Manajerial Candi"')
    print('Silahkan masukkan username anda')

# F14 Save
# fungsi untuk menyimpan data yang berada di program sesuai dengan struktur data eksternal
# jika nama folder tidak ditemukan, program akan membuat folder sesuai dengan masukan
# jika nama folder sudah ada, program akan menaruh file baru pada folder tersebut
# jika nama folder dan file sudah ada, program akan mengganti file pada folder tersebut dengan yang lebih baru


def save() -> None:
    # memasukkan nama folder
    inputPath = input("Masukkan nama folder: ")
    print("")

    # path awal untuk menyimpan data
    path = "save"

    # jika direktori belum ada
    if not (os.path.isdir(path)):
        print("Membuat folder " + path + "...")
        os.makedirs(path)

    # membuat path untuk direktori khusus yang dimasukkan
    path = path + "/" + inputPath

    # jika direktori khusus belum ada
    if not (os.path.isdir(path)):
        print("Membuat folder " + path + "...")
        os.makedirs(path)

    # menulis data ke dalam file CSV pada direktori yang telah dibuat
    writeCSV(path)

    # mereset stack undo
    var.stackUndo = [[], 0]

    print("\nSaving...\n")
    print("Berhasil menyimpan data di folder " + path + "!")

# F15 Help
def help() -> None:
    # SPESIFIKASI
    # prosedur untuk menampilkan semua command beserta deskripsinya yang dapat digunakan sesuai dengan akses yang dimiliki pemain
    # KAMUS LOKAL
    # type bantuanUmum : <command : string, deskripsi : string>
    # logout, save, exit : bantuanUmum
    # ALGORITMA
    logout = ("logout\n", "Untuk keluar dari akun yang digunakan sekarang")
    save = ("save\n", "Untuk menyimpan data permainan")
    exit = ("exit\n", "Untuk keluar dari program dan kembali ke terminal")
    print('=========== HELP ===========')
    if var.currentUser[2] == '':
        print("1. login\n   Untuk masuk menggunakan akun")
        print(f"2. {exit[0]}   {exit[1]}")
    elif var.currentUser[2] == "bandung_bondowoso":
        print(f"1. {logout[0]}   {logout[1]}")
        print("2. summonjin\n   Untuk memanggil jin")
        print("3. hapusjin\n   Untuk menghapus jin beserta candi yang dibuatnya")
        print("4. ubahjin\n   Untuk mengubah tipe jin")
        print("5. batchkumpul\n   Untuk mengerahkan seluruh pasukan jin pengumpul agar mengumpulkan bahan atau pembangun")
        print("6. batchbangun\n   Untuk mengerahkan seluruh pasukan jin pembangun agar membangun candi")
        print("7. laporanjin\n   Untuk menampilkan informasi berupa jumlah jin yang tersedia, jumlah jin pada setiap", "\n   role yang tersedia, jin terajin, jin termalas, dan jumlah bahan bangunan yang dimiliki")
        print("8. laporancandi\n   Untuk menampilkan informasi berupa jumlah candi yang telah dibangun beserta", "\n   material yang digunakan untuk membangunnya, ID candi termahal beserta harganya,", "\n   dan ID candi termurah beserta harganya")
        print(f"9. {save[0]}   {save[1]}")
        print(f"10.{exit[0]}   {exit[1]}")
    elif var.currentUser[2] == "roro_jonggrang":
        print(f"1. {logout[0]}   {logout[1]}")
        print("2. hancurkancandi\n   Untuk menghancurkan candi yang tersedia")
        print("3. ayamberkokok\n   Untuk menyelesaikan permainan dan menampilkan pemenang")
        print(f"4. {save[0]}   {save[1]}")
        print(f"5. {exit[0]}   {exit[1]}")
    elif var.currentUser[2] == 'jin_pengumpul':
        print(f"1. {logout[0]}   {logout[1]}")
        print("2. kumpul\n   Untuk mengumpulkan resource candi")
        print(f"3. {save[0]}   {save[1]}")
        print(f"4. {exit[0]}   {exit[1]}")
    else:  # var.currentUser[2] == 'jin_pembangun':
        print(f"1. {logout[0]}   {logout[1]}")
        print("2. bangun\n   Untuk membangun candi")
        print(f"3. {save[0]}   {save[1]}")
        print(f"4. {exit[0]}   {exit[1]}")

# F16 Exit
# fungsi untuk keluar dari program game ini
# sebelum keluar akan ditanyakan apakah mau men-save atau tidak
# jika ya maka data akan di-save, jika tidak maka data tidak akan di-save


def exitProgram() -> None:
    pilihan = ""

    while True:  # input akan diminta ulang hingga masukan pemain valid
        pilihan = input(
            "Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        if pilihan == "y" or pilihan == "Y" or pilihan == "n" or pilihan == "N":
            break

    # pengecekan apakah pemain mau men-save data sebelum keluar atau tidak
    if pilihan == "y" or pilihan == "Y":
        save()
        exit()
    elif pilihan == "n" or pilihan == "N":
        exit()
