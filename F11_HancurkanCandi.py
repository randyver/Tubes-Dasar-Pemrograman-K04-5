from util import *
import var
from typing import *

def hancurkanCandi() -> None:
    if var.currentUser[2] == 'roro_jonggrang':
        idCandi = int(input('Masukkan ID candi: '))
        validIdCandi = False
        for i in range(var.candi[1]):
            if var.candi[0][i][0] == idCandi:
                validIdCandi = True
        if validIdCandi:
            confirmed = ( 'Y' == input(f'Apakah anda yakin ingin menghancurkan candi ID: {idCandi} (Y/N)? '))
            if confirmed:
                var.candi = delete(arr = var.candi, func = lambda x : x[0] == idCandi )
                print('\nCandi telah berhasil dihancurkan.')
        else:
            print('\nTidak ada candi dengan ID tersebut.')
    else:
        print("Hancurkan candi hanya dapat diakses oleh akun Roro Jonggrang.")
        