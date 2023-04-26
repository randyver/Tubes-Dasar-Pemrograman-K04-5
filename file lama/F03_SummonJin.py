from util import *
import var
from typing import *

def summonJin() -> None:
    # SPESIFIKASI
    # fungsi untuk memanggil jin pengumpul atau jin pembangun dan menambahkannya sebagai user
    # fungsi hanya bisa diakses oleh Bandung Bondowoso
    # jumlah maksimal jin yang bisa di-summon adalah 100, username jin haruslah unik (tidak ada user dengan username sama), dan panjang password jin berada di rentang 5 sampai 25 (inklusif)
    # KAMUS LOKAL
    # jenisJin : integer
    # role, usernameJin, passwordJin : string
    # validUsername : boolean
    # ALGORITMA
    if var.currentUser[2] == "bandung_bondowoso":
        if var.users[1] < 103: # jumlah jin yang sudah di-summon < 100
            print("Jenis jin yang dapat dipanggil:"," (1) Pengumpul - Bertugas mengumpulkan bahan bangunan", " (2) Pembangun - Bertugas membangun candi", "", sep = '\n')
            while True: # loop menerima masukan jenis jin dan berhenti jika masukan jenis jin valid: (1) jin pengumpul, (2) jin pembangun
                jenisJin = (input("Masukkan nomor jenis jin yang ingin dipanggil: ")) 
                if jenisJin == "1":
                    print(f'\nMemilih jin \"Pengumpul\".\n')
                    role = 'jin_pengumpul'
                    break
                elif jenisJin == "2":
                    print(f"\nMemilih jin \"Pembangun\".\n")
                    role = "jin_pembangun"
                    break
                else:
                    print(f"\nTidak ada jenis jin bernomor \"{jenisJin}\"!\n")
            while True: # loop menerima masukan username jin dan berhenti jika masukan username jin valid (tidak ada user lain di variabel users dengan username masukan pengguna)
                validUsername = True
                usernameJin = input("Masukkan username jin: ")
                for i in range(0, var.users[1]):
                    if usernameJin == var.users[0][i][0]:
                        print(f'\nUsername "{usernameJin}" sudah diambil!\n')
                        validUsername = False
                        break
                if validUsername:
                    break
            while True: # loop menerima masukan password jin dan berhenti jika masukan password jin valid (panjang username jin berada di rentang 5 sampai 25 (inklusif))
                passwordJin = input("Masukkan password jin: ")
                if 5 <= len(passwordJin) <= 25:
                    break
                else:
                    print("\nPassword panjangnya harus 5-25 karakter!\n")
            
            var.users = add(data = (usernameJin, passwordJin, role), arr = var.users) # menambahkan jin ke variabel users
            print("\nMengumpulkan sesajen...", "Menyerahkan sesajen...", "Membacakan mantra...", sep = '\n')
            print(f"\nJin {usernameJin} berhasil dipanggil!")
        else: # jumlah jin yang telah di-summon == 100
            print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
    else: # var.currentUser[2] != "bandung_bondowoso"
        print("Summon jin hanya dapat diakses oleh akun Bandung Bondowoso.")
        
