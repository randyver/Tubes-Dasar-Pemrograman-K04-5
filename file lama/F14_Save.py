import var
from util import *
from typing import *
import os

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
    
    print("\nSaving...\n")
    print("Berhasil menyimpan data di folder " + path + "!")