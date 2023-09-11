class Hewan:
    nama_latin = "Animalia"
    def __init__(self, nama, umur, porsi_makan):
        self.nama = nama
        self.umur = umur
        self.porsi_makan = porsi_makan

    def bangun(self): #instance method
        if self.umur > 2.5:
            print("Hewan bernama {} ({} tahun) bangun di 8am".format(self.nama,self.umur))
        else:
            print("Hewan bernama {} ({} tahun) bangun di 10am".format(self.nama,self.umur))

    @classmethod
    def makan(cls, nama, umur, jumlah_pagi, jumlah_sore):
        banyak = jumlah_pagi + jumlah_sore
        return cls(nama, umur, banyak)

    @staticmethod
    def tidur(nama, umur):
        if umur > 2.5:
            print("Durasi tidur hewan, {} selama 2 jam atau lebih".format(nama))
        else:
            print("Durasi tidur hewan,{} selama 1-2 jam".format(nama))

class Kucing(Hewan):
    nama_latin = 'Felis Catus'

    def __init__(self, nama, umur, porsi_makan, kecepatan=10):
        super().__init__(nama,umur, porsi_makan)
        self.kecepatan = kecepatan

    def tidur(nama, umur):
        if umur > 2.5:
            print("Durasi tidur hewan, {} selama 13 jam atau lebih".format(nama))
        else:
            print("Durasi tidur hewan,{} selama 20 jam".format(nama))
    
    def lari(self):
        if self.kecepatan > 10:
            print("{} lari dengan Cepat Sekali".format(self.nama))
        else:
            print("{} lari dengan Lamban".format(self.nama))

class Kelinci(Hewan):
    nama_latin = 'Oryctolagus cuniculus'

    def __init__(self, nama, umur, porsi_makan, kecepatan=10):
        super().__init__(nama,umur, porsi_makan)
        self.kecepatan = kecepatan

    def tidur(nama, umur):
        if umur > 2.5:
            print("Durasi tidur hewan, {} selama 14 jam atau lebih".format(nama))
        else:
            print("Durasi tidur hewan,{} selama 12 jam".format(nama))

    def lari(self):
        if self.kecepatan > 10:
            print("{} lari dengan Cepat Sekali".format(self.nama))
        else:
            print("{} lari dengan Lamban".format(self.nama))

print(Hewan.nama_latin)
animal_1 = Hewan(nama="Panda Jantan", umur=15, porsi_makan=100)
print(animal_1.nama, animal_1.umur, animal_1.porsi_makan)
animal_1.bangun()
animal_1.tidur(animal_1.nama,animal_1.umur)

animal_2 = Hewan.makan("Panda Betina", 10, 45, 50)
print("Porsi makan {} per hari sebanyak {}".format(animal_2.nama, animal_2.porsi_makan))

print("")
print(Kucing.nama_latin)
animal_3 = Kucing(nama="Cat", umur=10, porsi_makan=10,kecepatan=100)
print(animal_3.nama, animal_3.umur, animal_3.porsi_makan)
animal_3.bangun()
animal_3.lari()

print("")
print(Kelinci.nama_latin)
animal_4 = Kelinci(nama="Rabbit", umur=10, porsi_makan=10)
print(animal_4.nama, animal_4.umur, animal_4.porsi_makan)
animal_4.bangun()
animal_4.lari()