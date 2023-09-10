class Hewan:
    nama_latin = "Animalia"
    def __int__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def bangun(self): #instance method
        if self.umur > 2.5:
            print("Hewan bernama {} ({} tahun) bangun di 8am".format(self.nama,self.umur))
        else:
            print("Hewan bernama {} ({} tahun) bangun di 10am".format(self.nama,self.umur))

    @classmethod
    def makan(jumlah, nama, umur):
        return jumlah(nama, umur)

    @staticmethod
    def tidur(nama, umur):
        if umur > 2.5:
            print("Durasi tidur hewan, {} selama 2 jam atau lebih".format(nama))
        else:
            print("Durasi tidur hewan,{} selama 1-2 jam".format(nama))

class Kucing(Hewan):
    nama_latin = 'Felis Catus'

    def __int__(self, nama, umur):
        super().__init__(nama,umur)

    def bangun(self): #instance method
        if self.umur > 2.5:
            print("Hewan bernama {} ({} tahun) bangun di 8am".format(self.nama,self.umur))
        else:
            print("Hewan bernama {} ({} tahun) bangun di 10am".format(self.nama,self.umur))

    @classmethod
    def makan(jumlah, nama, umur):
        return jumlah(nama, umur)

    @staticmethod
    def tidur(nama, umur):
        if umur > 2.5:
            print("Durasi tidur hewan, {} selama 13 jam atau lebih".format(nama))
        else:
            print("Durasi tidur hewan,{} selama 20 jam".format(nama))
    
    def lari(kecepatan=10):
        if kecepatan > 10:
            print("Cepat Sekali")
        else:
            print("Lamban")

class Kelinci(Hewan):
    nama_latin = 'Oryctolagus cuniculus'

    def __int__(self, nama, umur):
        super().__init__(nama,umur)

    def bangun(self): #instance method
        if self.umur > 2.5:
            print("Hewan bernama {} ({} tahun) bangun di 8am".format(self.nama,self.umur))
        else:
            print("Hewan bernama {} ({} tahun) bangun di 10am".format(self.nama,self.umur))

    @classmethod
    def makan(jumlah, nama, umur):
        return jumlah(nama, umur)

    @staticmethod
    def tidur(nama, umur):
        if umur > 2.5:
            print("Durasi tidur hewan, {} selama 14 jam atau lebih".format(nama))
        else:
            print("Durasi tidur hewan,{} selama 12 jam".format(nama))
    
    def lari(kecepatan=10):
        if kecepatan > 10:
            print("Cepat Sekali")
        else:
            print("Lamban")