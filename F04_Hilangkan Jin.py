import var
from util import *
from typing import *
import os

def hapusjin(list_user, list_pass, list_role, id, pembuat, pasir, batu, air):
    uname = input("Masukkan username jin: ") #ifrit, lala, zaki
    user, password, role = [], [], []
    for i in range(0, len(list_user)):
        if uname == list_user[i] and (list_role[i] == "jin_pengumpul" or list_role[i] == 'jin_pembangun'):
            confirm = str(input("Apakah anda yakin ingin menghapus jin dengan username "+str(uname)+" (Y/N)?"))
            while(confirm != "Y" and confirm != "N"):
                print()
                print("Input tidak valid ulangi lagi!")
                confirm = str(input("Apakah anda yakin ingin menghapus jin dengan username "+str(uname)+" (Y/N)?"))
                print()

            if confirm == "Y":
                for j in range(0, i):
                    user.append(str(list_user[j]))
                    password.append(str(list_pass[j]))
                    role.append(str(list_role[j]))

                for j in range(i + 1, len(list_user)):
                    user.append(str(list_user[j]))
                    password.append(str(list_pass[j]))
                    role.append(str(list_role[j]))

                for j in range(0, len(id)):
                    if uname == pembuat[j]:
                        id[j] = 0
                        pembuat[j] = 'none'
                        pasir[j] = 0
                        batu[j] = 0
                        air[j] = 0

                print("Jin telah berhasil dihapus dari alam gaib.")
                return user, password, role, id, pembuat, pasir, batu, air

            else: #confirm == "N"
                print("Jin gagal dihapus dari alam gaib.")
                return list_user, list_pass, list_role, id, pembuat, pasir, batu, air

    print()
    print("Tidak ada jin dengan username tersebut.") #Jika tidak ada
    return list_user, list_pass, list_role, id, pembuat, pasir, batu, air
