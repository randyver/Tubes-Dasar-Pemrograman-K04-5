from util import *
import var
from typing import *

def hancurkanCandi() -> None:
    # SPESIFIKASI
    # fungsi untuk menghancurkan candi yang sudah dibangun oleh jin pembangun dan Bandung Bondowoso
    # fungsi hanya bisa diakses oleh Roro Jonggrang
    # jika ID candi yang ingin dihancurkan valid (tersedia di daftar candi yang sudah dibangun), candi dengan ID tersebut akan dihapus dari daftar candi yang sudah dibangun
    # KAMUS LOKAL
    # idCandi : integer
    # validIdCandi, confirmed : boolean
    # ALGORITMA
    if var.currentUser[2] == 'roro_jonggrang':
        idCandi = int(input('Masukkan ID candi: ')) # menerima masukan ID candi yang ingin dihancurkan
        validIdCandi = False
        for i in range(var.candi[1]): # mencari candi dengan ID sama dengan idCandi
            if var.candi[0][i][0] == idCandi: # candi dengan ID sama dengan idCandi ditemukan (ID valid), validIdCandi menjadi True
                validIdCandi = True
        if validIdCandi: # validIdCandi == True
            confirmed = ( 'Y' == input(f'Apakah anda yakin ingin menghancurkan candi ID: {idCandi} (Y/N)? '))
            if confirmed: # confirmed == True
                var.candi = delete(arr = var.candi, func = lambda x : x[0] == idCandi ) # menghapus candi dengan ID sama dengan idCandi dari daftar candi
                print('\nCandi telah berhasil dihancurkan.')
        else: # validIdCandi == False
            print('\nTidak ada candi dengan ID tersebut.')
    else: # var.currentUser[2] != "roro_jonggrang"
        print("Hancurkan candi hanya dapat diakses oleh akun Roro Jonggrang.")
        
