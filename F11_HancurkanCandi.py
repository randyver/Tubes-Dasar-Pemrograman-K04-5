from util import *
from var import *
from typing import *

def hancurkanCandi() -> None:
    global candi
    if currentUser[2] == 'roro_jonggrang':
        idCandi = int(input('Masukkan ID candi: '))
        validIdCandi = False
        for i in range(candi[1]):
            if candi[0][i][0] == idCandi:
                validIdCandi = True
        if validIdCandi:
            confirmed = ( 'Y' == input(f'Apakah anda yakin ingin menghancurkan candi ID: {idCandi} (Y/N)? '))
            if confirmed:
                candi = delete(arr = candi, func = lambda x : x[0] == idCandi )
                print('\nCandi telah berhasil dihancurkan.')
        else:
            print('\nTidak ada candi dengan ID tersebut.')