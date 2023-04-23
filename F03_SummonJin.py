from util import *
from var import *
from typing import *

def summonJin() -> None:
    global users
    if currentUser[2] == 'bandung_bondowoso':
        if users[1] < 103:
            print('Jenis jin yang dapat dipanggil:',' (1) Pengumpul - Bertugas mengumpulkan bahan bangunan', ' (2) Pembangun - Bertugas membangun candi', '', sep = '\n')
            validJenisJin = False
            while not(validJenisJin):
                jenisJin = int(input('Masukkan nomor jenis jin yang ingin dipanggil: '))
                if jenisJin == 1 or jenisJin == 2:
                    validJenisJin = True
                else:
                    print(f'\nTidak ada jenis jin bernomor "{jenisJin}"!\n')
            if jenisJin == 1:
                print(f'\nMemilih jin {"Pengumpul"}.\n')
                role = 'jin_pengumpul'
            else:
                print(f'\nMemilih jin {"Pembangun"}.\n')
                role = 'jin_pembangun'

            validUsername = False
            validPassword = False
            while not(validUsername):
                usernameJin = input('Masukkan username jin: ')
                for i in range(1, users[1]):
                    if usernameJin == users[0][i][0]:
                        print(f'\nUsername "{usernameJin}" sudah diambil!\n')
                        break
                    else:
                        if i == users[1] - 1:
                            validUsername = True
            while not(validPassword):
                passwordJin = input('Masukkan password jin: ')
                if 5 <= len(passwordJin) <= 25:
                    validPassword = True
                else:
                    print('\nPassword panjangnya harus 5-25 karakter!\n')
            
            users = add(data = (usernameJin, passwordJin, role), arr = users)
            print('\nMengumpulkan sesajen...', 'Menyerahkan sesajen...', 'Membacakan mantra...', sep = '\n')
            print(f'\nJin {usernameJin} berhasil dipanggil!')
        else:
            print('Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu')