from util import *
import var
from typing import *

def summonJin() -> None:
    if var.currentUser[2] == 'bandung_bondowoso':
        if var.users[1] < 103:
            print('Jenis jin yang dapat dipanggil:',' (1) Pengumpul - Bertugas mengumpulkan bahan bangunan', ' (2) Pembangun - Bertugas membangun candi', '', sep = '\n')
            validJenisJin = False
            while not(validJenisJin):
                jenisJin = (input('Masukkan nomor jenis jin yang ingin dipanggil: '))
                if jenisJin == "1" or jenisJin == "2":
                    validJenisJin = True
                else:
                    print(f'\nTidak ada jenis jin bernomor "{jenisJin}"!\n')
            if jenisJin == "1":
                print(f'\nMemilih jin {"Pengumpul"}.\n')
                role = 'jin_pengumpul'
            else:
                print(f'\nMemilih jin {"Pembangun"}.\n')
                role = 'jin_pembangun'
                
            validPassword = False
            while True:
                validUsername = True
                usernameJin = input("Masukkan username jin: ")
                for i in range(0, var.users[1]):
                    if usernameJin == var.users[0][i][0]:
                        print(f'\nUsername "{usernameJin}" sudah diambil!\n')
                        validUsername = False
                        break
                if validUsername:
                    break
                else:
                    print('Username “' + usernameJin + '” sudah diambil!')
            while True:
                passwordJin = input('Masukkan password jin: ')
                if 5 <= len(passwordJin) <= 25:
                    break
                else:
                    print('\nPassword panjangnya harus 5-25 karakter!\n')
            
            var.users = add(data = (usernameJin, passwordJin, role), arr = var.users)
            print('\nMengumpulkan sesajen...', 'Menyerahkan sesajen...', 'Membacakan mantra...', sep = '\n')
            print(f'\nJin {usernameJin} berhasil dipanggil!')
        else:
            print('Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu')
    else:
        print('Summon jin hanya dapat diakses oleh akun Bandung Bondowoso.')
        