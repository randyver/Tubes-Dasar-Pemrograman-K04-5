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
    else: # var.currentUser == ("", "", "")
        # menerima input
        username = input("Username: ") # (string)
        password = input("Password: ") # (string)

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
        else: # user[1] == 0
            print("Username tidak terdaftar!")
        
# F02 Logout    
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
        
# F13 Load
# fungsi yang dijalankan pada awal permainan untuk mengambil data yang diperlukan pada game ini dari sebuah folder
def load() -> None:
    # pengambilan alamat folder data dari input pemain
    parser = argparse.ArgumentParser()
    parser.add_argument("folderPath")
    args = parser.parse_args() 

    folderPath = args.folderPath # (string)
    if folderPath == "":  # pengecekan apakah pemain game sudah memberikan alamat folder data atau tidak
        print("Tidak ada nama folder yang diberikan!\n")
        print("Usage: python main.py <nama_folder>")
        exit()

    folderPath = "save/" + args.folderPath # (string)
    # pengecekan apakah alamat folder itu ada atau tidak
    if not os.path.isdir(folderPath):
        print('Folder "' + folderPath + '" tidak ditemukan.')
        exit()

    # pembacaan data pada file CSV
    print("Loading...")
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
    # prosedur untuk menampikan semua command yang dapat digunakan dengan akses yang dimiliki pemain 
    # KAMUS LOKAL
    # bantuanUmum : tuple of string
    # ALGORITMA
    bantuanUmum = ('login\n   Untuk masuk menggunakan akun', 'logout\n   Untuk keluar dari akun yang digunakan sekarang', 'save\n   Untuk menyimpan data yang berada di program', 
                    'exit\n   Untuk keluar dari program dan kembali ke terminal')
    if var.currentUser[2] == '':
        print('=========== HELP ===========')
        print(f'1. {bantuanUmum[0]}\n2. {bantuanUmum[3]}')
    elif var.currentUser[2] == 'bandung_bondowoso':
        print('=========== HELP ===========')
        print(f'1. {bantuanUmum[1]}')
        print('2. summonjin\n   Untuk memanggil jin')
        print('3. hapusjin\n   Untuk menghapus jin beserta candi yang dibuatnya')
        print('4. ubahjin\n   Untuk mengubah tipe jin')
        print('5. batchkumpul\n   Untuk mengerahkan seluruh pasukan jin pengumpul untuk mengumpulkan bahan atau pembangun')
        print('6. batchbangun\n   Untuk mengerahkan seluruh pasukan jin pembangun untuk membangun candi')
        print('7. laporancandi\n   Untuk menghasilkan laporan candi yang berisi jumlah candi yang telah dibangun beserta material yang digunakan, ID candi termahal, dan ID candi termurah')
        print(f'8. {bantuanUmum[2]}')
        print(f'9. {bantuanUmum[3]}')
    elif var.currentUser[2] == 'roro_jonggrang':
        print('=========== HELP ===========')
        print(f'1. {bantuanUmum[1]}')
        print('2. hancurkancandi\n   Untuk menghancurkan candi yang tersedia')
        print('3. ayamberkokok\n   Untuk menyelesaikan permainan')
        print(f'4. {bantuanUmum[2]}')
        print(f'5. {bantuanUmum[3]}')
    elif var.currentUser[2] == 'jin_pengumpul':
        print('=========== HELP ===========')
        print(f'1. {bantuanUmum[1]}')
        print('2. kumpul\n   Untuk mengumpulkan resource candi')
        print(f'3. {bantuanUmum[2]}')
        print(f'4. {bantuanUmum[3]}')
    else: # var.currentUser[2] == 'jin_pembangun':
        print('=========== HELP ===========')
        print(f'1. {bantuanUmum[1]}')
        print('2. bangun\n   Untuk membangun candi')
        print(f'3. {bantuanUmum[2]}')
        print(f'4. {bantuanUmum[3]}')

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

