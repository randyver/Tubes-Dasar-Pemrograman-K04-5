from util import *
from var import *
from typing import *

def help() -> None:
    bantuanUmum = ('login\n   Untuk masuk menggunakan akun', 'logout\n   Untuk keluar dari akun yang digunakan sekarang', 'save\n   Untuk menyimpan data yang berada di program', 
                    'exit\n   Untuk keluar dari program dan kembali ke terminal')
    if currentUser[2] == '':
        print('=========== HELP ===========')
        print(f'1. {arrayBantuanUmum[0]}\n2. {arrayBantuanUmum[3]}')
    elif currentUser[2] == 'bandung_bondowoso':
        print('=========== HELP ===========')
        print(f'1. {arrayBantuanUmum[1]}')
        print('2. summonjin\n   Untuk memanggil jin')
        print('3. hapusjin\n   Untuk menghapus jin beserta candi yang dibuatnya')
        print('4. ubahjin\n   Untuk mengubah tipe jin')
        print('5. batchkumpul\n   Untuk mengerahkan seluruh pasukan jin pengumpul untuk mengumpulkan bahan atau pembangun')
        print('6. batchbangun\n   Untuk mengerahkan seluruh pasukan jin pembangun untuk membangun candi')
        print('7. laporancandi\n   Untuk menghasilkan laporan candi yang berisi jumlah candi yang telah dibangun beserta material yang digunakan, ID candi termahal, dan ID candi termurah')
        print(f'8. {arrayBantuanUmum[2]}')
        print(f'9. {arrayBantuanUmum[3]}')
    elif currentUser[2] == 'roro_jonggrang':
        print('=========== HELP ===========')
        print(f'1. {arrayBantuanUmum[1]}')
        print('2. hancurkancandi\n   Untuk menghancurkan candi yang tersedia')
        print('3. ayamberkokok\n   Untuk menyelesaikan permainan')
        print(f'4. {arrayBantuanUmum[2]}')
        print(f'5. {arrayBantuanUmum[3]}')
    elif currentUser[2] == 'jin_pengumpul':
        print('=========== HELP ===========')
        print(f'1. {arrayBantuanUmum[1]}')
        print('2. kumpul\n   Untuk mengumpulkan resource candi')
        print(f'3. {arrayBantuanUmum[2]}')
        print(f'4. {arrayBantuanUmum[3]}')
    else: # currentUser[2] == 'jin_pembangun':
        print('=========== HELP ===========')
        print(f'1. {arrayBantuanUmum[1]}')
        print('2. bangun\n   Untuk membangun candi')
        print(f'3. {arrayBantuanUmum[2]}')
        print(f'4. {arrayBantuanUmum[3]}')