import var
from util import *
from typing import *

def logout() -> None:
    if var.currentUser == ("","",""):
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
    else:
        var.currentUser = ("","","")