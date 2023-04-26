import var
from util import *
from typing import *
import os

class Jin:
    def __init__(self, jenis):
        self.jenis = jenis
        self.bahan = {'pasir': 0, 'batu': 0, 'air': 0}
    
    def kumpulkan_bahan(self):
        for i in range(self.jenis):
            self.bahan['pasir'] += random.randint(1, 5)
            self.bahan['batu'] += random.randint(1, 5)
            self.bahan['air'] += random.randint(1, 5)
    
    def bangun_candi(self):
        bahan_candi = {'pasir': 0, 'batu': 0, 'air': 0}
        for i in range(self.jenis):
            bahan_candi['pasir'] += random.randint(1, 5)
            bahan_candi['batu'] += random.randint(1, 5)
            bahan_candi['air'] += random.randint(1, 5)
        
        for key, value in bahan_candi.items():
            if value > self.bahan[key]:
                print('Jin', self.jenis, 'gagal membangun candi')
                return False
        
        for key, value in bahan_candi.items():
            self.bahan[key] -= value
        print('Jin', self.jenis, 'berhasil membangun candi')
        return True

class BandungBondowoso:
    def __init__(self, jumlah_jin):
        self.jumlah_jin = jumlah_jin
        self.pasukan_jin = []
        for i in range(self.jumlah_jin):
            jenis = random.choice(['pengumpul', 'pembangun'])
            self.pasukan_jin.append(Jin(jenis))
    
    def batch_kumpul(self):
        for jin in self.pasukan_jin:
            if jin.jenis == 'pengumpul':
                jin.kumpulkan_bahan()
        print('Bahan yang berhasil dikumpulkan:')
        for key, value in self.jumlah_bahan().items():
            print(key.capitalize(), value)
    
    def batch_bangun(self):
        candi_berhasil = 0
        for jin in self.pasukan_jin:
            if jin.jenis == 'pembangun':
                if jin.bangun_candi():
                    candi_berhasil += 1
        if candi_berhasil == 0:
            print('Seluruh candi gagal dibangun')
    
    def jumlah_bahan(self):
        jumlah_bahan = {'pasir': 0, 'batu': 0, 'air': 0}
        for jin in self.pasukan_jin:
            for key, value in jin.bahan.items():
                jumlah_bahan[key] += value
        return jumlah_bahan
