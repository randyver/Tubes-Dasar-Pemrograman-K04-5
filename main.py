# file utama di mana program akan berjalan (entry point)
from B04_Undo import undo
from F01_Login import login
from F02_Logout import logout
from F03_SummonJin import summonJin
from F05_UbahTipeJin import ubahJin
from F06_JinPembangun import bangunCandi
from F07_Kumpul import kumpul
from F09_AmbilLaporanJin import laporanJin
from F10_AmbilLaporanCandi import laporanCandi
from F11_HancurkanCandi import hancurkanCandi
from F13_Load import load
from F14_Save import save
from F15_Help import help
from util import *
import var
from typing import *

# menjalankan fungsi load untuk mengambil data dari file csv sebelum game dimulai
load()

# main loop dari game
while not var.gameEnd:
    command: str = input(">>> ")
    if command == "login":
        login()
    elif (command == "exit"):
        # exitProgram()
        exit()
    elif (command == "help"):
        help()
    elif (command == "logout"):
        logout()
    elif (command == "save"):
        save()
    elif (command == "summonjin"):
        summonJin()
    # elif (command == "hapusjin"):
        # hapusJin()
    elif (command == "ubahjin"):
        ubahJin()
    # elif (command == "batchkumpul"):
        # batchKumpul()
    # elif (command == "batchbangun"):
        # batchBangun()
    elif (command == "laporanjin"):
        laporanJin()
    elif (command == "laporancandi"):
        laporanCandi()
    elif (command == "undo"):
        undo()
    elif (command == "hancurkancandi"):
        hancurkanCandi()
    # elif (command == "ayamberkokok"):
        # ayamBerkokok()
    elif (command == "bangun"):
        bangunCandi()
    elif (command == "kumpul"):
        kumpul()
    else:
        print("Tidak ada command tersebut")
