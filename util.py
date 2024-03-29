# file yang berisi fungsi-fungsi pendukung fungsi utama
import var
from typing import *
from collections.abc import Callable
import time  # untuk dijadikan seed pada lcg


# fungsi untuk mendapatkan index dari suatu elemen di dalam array
# arr: tempat suatu data akan dicari
# func: fungsi untuk menentukan kriteria elemen seperti apa yang dicari di dalam arr
# return: index dari suatu elemen atau -1 jika tidak ada elemen yang memenuhi kriteria
# fungsi ini akan mengembalikan index saat func mengembalikan nilai true
def getIndex(arr: Tuple[List[Tuple[str, str, str]], int] | Tuple[List[Tuple[int, str, int, int, int]], int], func: Callable[[Tuple[str, str, str]], bool] | Callable[[Tuple[int, str, int, int, int]], bool]) -> int:
    for i in range(0, arr[1]):
        if func(arr[0][i]):
            return i

    return -1


# fungsi untuk menambah data pada suatu array, data akan ditambahkan di akhir dari suatu array
# data: data yang mau ditambahkan ke arr
# arr: array dimana data akan ditambahkan
# return: sebuah array yang sudah ditambahkan data baru didalamnya
def add(data: Tuple[str, str, str] | Tuple[int, str, int, int, int] | Tuple[Tuple[str, str, str], Tuple[List[Tuple[int, str, int, int, int]], int]], arr: Tuple[List[Tuple[str, str, str]], int] | Tuple[List[Tuple[int, str, int, int, int]], int] | Tuple[List[Tuple[Tuple[str, str, str], Tuple[List[Tuple[int, str, int, int, int]], int]]], int]) -> Tuple[List[Tuple[str, str, str]], int] | Tuple[List[Tuple[int, str, int, int, int]], int] | Tuple[List[Tuple[Tuple[str, str, str], Tuple[List[Tuple[int, str, int, int, int]], int]]], int]:
    # inisialisasi array sementara dengan panjang + 1 dari panjang array arr
    temp = ["" for i in range(arr[1] + 1)]

    # penyalinan data pada array arr ke array temp dan penambahan data pada array temp
    for i in range(0, arr[1]+1):
        if i != arr[1]:
            temp[i] = arr[0][i]  # penyalinan
        else:
            temp[i] = data  # penambahan data

    return (temp, arr[1] + 1)  # panjang array ditambah 1

# fungsi untuk menghapus elemen dalam suatu array berdasarkan kriteria tertentu
# arr: array yang elemennya mau dihapus
# func: fungsi untuk menentukan kriteria elemen apa yang mau dihapus
# return: array yang sudah dihapus beberapa elemen didalamnya
# fungsi ini akan menghapus elemen dalam array ketika fungsi func mengembalikan nilai true
# fungsi ini bisa menghapus lebih dari satu elemen asalkan elemen tersebut masih memenuhi kriteria yang ditentukan
def delete(arr: Tuple[List[Tuple[str, str, str]], int] | Tuple[List[Tuple[int, str, int, int, int]], int], func: Callable[[Tuple[str, str, str]], bool] | Callable[[Tuple[int, str, int, int, int]], bool]) -> Tuple[List[Tuple[str, str, str]], int] | Tuple[List[Tuple[int, str, int, int, int]], int]:
    temp = ["" for i in range(arr[1])]  # inisialisasi array sementara

    pengurang = 0  # banyak elemen yang di hapus dalam array arr

    # penyalinan dan penggeseran elemen pada array arr ke array temp
    for i in range(0, arr[1]):
        if func(arr[0][i]):
            # persiapan penggeseran (penghapusan elemen)
            pengurang = pengurang + 1
        else:
            temp[i - pengurang] = arr[0][i]  # penyalinan

    temp2 = temp
    # pembuatan array dengan panjang yang sesuai
    temp = [temp2[i] for i in range(arr[1]-pengurang)]

    # panjang array dikurangkan sesuai dengan banyak elemen yang dihapus
    return (temp, arr[1] - pengurang)

# fungsi ini mengembalikan elemen terakhir pada array stackUndo
# return: elemen terakhir array stackUndo (elemen terakhir akan dihapus)
def getLast() -> Tuple[Tuple[str, str, str], Tuple[List[Tuple[int, str, int, int, int]], int]]:
    data = var.stackUndo[0][var.stackUndo[1]-1]  # pengambilan data terakhir

    # penghapusan data terakhir
    temp = ([var.stackUndo[0][i]
            for i in range(var.stackUndo[1] - 1)], var.stackUndo[1] - 1)
    var.stackUndo = temp

    return data

# fungsi untuk menentukan id Candi dari candi yang akan dibangun
# return: id candi yang valid (belum ada pada array candi), id candi berada pada rentang 1-100
def generateIdCandi() -> int:
    idCandi = 1
    while True:
        ada = False
        for i in range(var.candi[1]):
            if var.candi[0][i][0] == idCandi:  # pengecekan id candi sudah ada atau belum
                ada = True
                break
        if ada:  # id candi sudah anda pencarian dilanjutkan
            idCandi = idCandi + 1
        else:  # id candi belum ada pencarian id selesai
            break
    return idCandi

# fungsi untuk memfilter isi dari suatu array
# arr: array yang mau difilter isinya
# func: fungsi untuk menentukan kriteria dari filter yang akan dilakukan, ketika fungsi func mengembalikan false maka suatu elemen akan dihapuskan dari dalam array
# return: array yang sudah difilter, array ini berisi semua elemen yang memenuhi kriteria yang sudah ditentukan pada fungsi func
def filterArr(arr: Tuple[List[Tuple[str, str, str]], int] | Tuple[List[Tuple[int, str, int, int, int]], int], func: Callable[[Tuple[str, str, str]], bool] | Callable[[Tuple[int, str, int, int, int]], bool]) -> Tuple[List[Tuple[str, str, str]], int] | Tuple[List[Tuple[int, str, int, int, int]], int]:
    temp = ([], 0)  # inisialisasi array sementara

    for i in range(arr[1]):
        # elemen pada array arr yang memenuhi kriteria akan ditambahkan pada array temp
        if (func(arr[0][i])):
            temp = add(arr[0][i], temp)

    return temp

# fungsi untuk membaca file CSV kemudian menyimpannya dalam sebuah array
# path: alamat dari file CSV yang mau dibaca
# tipe: data file CSV apa yang mau dibaca, ada 3 tipe yaitu bahan, candi, dan user
# return: array yang berisi data dari file CSV yang dibaca
def readCSV(path: str) -> None:
    # pembacaan file user
    arsipUser = open(path + "/user.csv", "r")
    arsipUser.readline()
    # membaca 1 baris pada file dan diberi mark
    rekUser = arsipUser.readline() + "@"
    while rekUser != "@":  # pengecekan mark (akhir file)
        i = 0
        data = ["" for i in range(3)]
        indexData = 0
        word = ""
        while indexData < 3:
            # pengecekan mark (akhir baris) dan pengecekan separator
            if rekUser[i] == ";" or rekUser[i] == "@" or rekUser[i] == "\n":
                data[indexData] = word
                indexData = indexData + 1
                word = ""
            else:
                word = word + rekUser[i]
            i = i + 1

        var.users = add(tuple(data), var.users)  # memasukan data pada array

        # membaca 1 baris pada file dan diberi mark
        rekUser = arsipUser.readline() + "@"

    # pembacaan file candi
    arsipCandi = open(path + "/candi.csv", "r")
    arsipCandi.readline()
    # membaca 1 baris pada file dan diberi mark
    rekCandi = arsipCandi.readline() + "@"
    while rekCandi != "@":  # pengecekan mark (akhir file)
        i = 0
        data = ["" for i in range(5)]
        indexData = 0
        word = ""
        while indexData < 5:
            # pengecekan mark (akhir baris) dan pengecekan separator
            if rekCandi[i] == ";" or rekCandi[i] == "@" or rekCandi[i] == "\n":
                if indexData == 1:
                    data[indexData] = word
                else:
                    data[indexData] = int(word)
                indexData = indexData + 1
                word = ""
            else:
                word = word + rekCandi[i]
            i = i + 1

        var.candi = add(tuple(data), var.candi)  # memasukan data pada array

        # membaca 1 baris pada file dan diberi mark
        rekCandi = arsipCandi.readline() + "@"

    # pembacaan file bahan bangunan
    arsipBahan = open(path + "/bahan_bangunan.csv", "r")
    arsipBahan.readline()
    
    # membaca 1 baris pada file dan diberi mark
    rekBahan = arsipBahan.readline() + "@"
    if rekBahan == "@":
        var.bahanBangunan = add(("pasir", "contoh bahan material yang berbentuk butiran", 0), var.bahanBangunan)
        var.bahanBangunan = add(("batu", "benda alam yang tersusun atas kumpulan mineral penyusun kerak bumi yang menyatu secara padat maupun yang berserakan", 0), var.bahanBangunan)
        var.bahanBangunan = add(("air", "suatu zat yang tersusun dari unsur kimia hidrogen dan oksigen dan berada dalam bentuk gas, cair, dan padat", 0), var.bahanBangunan)
    else:
        while rekBahan != "@":  # pengecekan mark (akhir file)
            i = 0
            data = ["" for i in range(3)]
            indexData = 0
            word = ""
            while indexData < 3:
                # pengecekan mark (akhir baris) dan pengecekan separator
                if rekBahan[i] == ";" or rekBahan[i] == "@" or rekBahan[i] == "\n":
                    if indexData == 2:
                        data[indexData] = int(word)
                    else:
                        data[indexData] = word
                    indexData = indexData + 1
                    word = ""
                else:
                    word = word + rekBahan[i]
                i = i + 1

            # memasukan data pada array
            var.bahanBangunan = add(tuple(data), var.bahanBangunan)

            # membaca 1 baris pada file dan diberi mark
            rekBahan = arsipBahan.readline() + "@"

    arsipUser.close()
    arsipCandi.close()
    arsipBahan.close()

# fungsi untuk menuliskan data ke file CSV
# path: alamat file CSV yang mau dituliskan
# tipe: data apa yang mau dituliskan ke CSV, tipe ada tiga yaitu: user, candi, dan bahan
def writeCSV(path: str) -> None:
    rekUser = "username;password;role\n"
    rekCandi = "id;pembuat;pasir;batu;air\n"
    rekBahan = "nama;deskripsi;jumlah\n"

    # penyusunan data array of user
    for i in range(var.users[1]):
        dataUser = var.users[0][i][0] + ";" + var.users[0][i][1] + ";" + var.users[0][i][2] + "\n"
        rekUser = rekUser + dataUser
    # penyusunan data array of candi
    for i in range(var.candi[1]):
        dataCandi = str(var.candi[0][i][0]) + ";" + var.candi[0][i][1] + ";" + str(
            var.candi[0][i][2]) + ";" + str(var.candi[0][i][3]) + ";" + str(var.candi[0][i][4]) + "\n"
        rekCandi = rekCandi + dataCandi
    # penyusunan data array of bahan
    for i in range(var.bahanBangunan[1]):
        dataBahan = var.bahanBangunan[0][i][0] + ";" + var.bahanBangunan[0][i][1] + ";" + str(var.bahanBangunan[0][i][2]) + "\n"
        rekBahan = rekBahan + dataBahan

    #penulisan data ke file
    arsipUser = open(path + "/user.csv", "w")
    arsipCandi = open(path + "/candi.csv", "w")
    arsipBahan = open(path + "/bahan_bangunan.csv", "w")
    arsipUser.write(rekUser)
    arsipCandi.write(rekCandi)
    arsipBahan.write(rekBahan)
    arsipUser.close()
    arsipCandi.close()
    arsipBahan.close()

# fungsi Linear Congruential Generator untuk membantu menghasilkan bilangan acak
def lcg(modulus: int, a: int, b: int, seed: int) -> Generator[int, None, None]:
    while True:
        seed = (a * seed + b) % modulus  # rumus lcg
        # dibagi modulus mengembalikan hasil pada rentang [0,1]
        yield seed / (modulus)


x = lcg(2**31, 1103515245, 12345, time.time())

# B01 Random Number Generator
# fungsi untuk mengenerate random int pada suatu rentang
# min: batas bawah random integer (inklusif)
# max: batas atas random integer (inklusif)
# return: sebuah random integer di antara min dan max
def randomAngka(min: int, max: int) -> int:
    # menyesuaikan dengan batas yang ditentukan
    return int(next(x) * ((max+1)-min) + min)

