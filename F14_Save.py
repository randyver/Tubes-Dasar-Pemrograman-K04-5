import var
from util import *
from typing import *
import os

def save() -> None:
    inputPath = input("Masukkan nama folder: ")
    print("")
    
    path = "save"
    if not (os.path.isdir(path)):
        print("Membuat folder " + path + "...")
        os.makedirs(path)
    
    path = path + "/" + inputPath    
    if not (os.path.isdir(path)):
        print("Membuat folder " + path + "...")
        os.makedirs(path)

    writeCSV(path + "/user.csv", "user")
    writeCSV(path + "/candi.csv", "candi")
    writeCSV(path + "/bahan_bangunan.csv", "bahan")
    
    print("")
    print("Saving...")
    print("")
    print("Berhasil menyimpan data di folder " + path + "!")