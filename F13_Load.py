import var
from util import *
from typing import *
import argparse
import os

# fungsi yang dijalankan pada awal permainan untuk mengambil data yang diperlukan pada game ini dari sebuah folder
def load() -> None:
    # pengambilan alamat folder data dari input pemain
    parser = argparse.ArgumentParser()
    parser.add_argument("folderPath")
    args = parser.parse_args()

    folderPath = args.folderPath
    if folderPath == "":  # pengecekan apakah pemain game sudah memberikan alamat folder data atau tidak
        print("Tidak ada nama folder yang diberikan!")
        print("")
        print("Usage: python main.py <nama_folder>")
        exit()

    folderPath = "save/" + args.folderPath
    # pengecekan apakah alamat folder itu ada atau tidak
    if not os.path.isdir(folderPath):
        print('Folder "' + folderPath + '" tidak ditemukan.')
        exit()

    # pembacaan data pada file CSV
    print("Loading...")
    readCSV(folderPath)

    print('Selamat datang di program "Manajerial Candi"')
    print('Silahkan masukkan username anda')