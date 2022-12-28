# Nama : Dandi Purnomo
# NIM : D0221078
# Kelas : F


class Bangun_Datar:
    def luas (self):
        pass

class Persegi (Bangun_Datar):
    def __init__ (self, sisi):
        self.sisi = sisi
    def luas (self):
        return self.sisi * self.sisi

class Segitiga (Bangun_Datar):
    def __init__ (self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
        
    def luas (self):
        return self.alas * self.tinggi / 2
    
class Lingkaran (Bangun_Datar):
    def __init__ (self, jari_jari):
        self.jari = jari_jari
        
    def luas (self):
        return 22/7 * self.jari * self.jari




class Bangun_Ruang:
    def volume (self):
        pass
    
class Kubus (Bangun_Ruang):
    def __init__ (self, sisi):
        self.sisi = sisi
        
    def volume (self):
        return self.sisi * self.sisi * self.sisi
    
class Limas (Bangun_Ruang):
    def __init__ (self, alas, tinggi_alas, tinggi_limas):
        self.alas = alas
        self.ta = tinggi_alas
        self.tl = tinggi_limas
        
    def volume (self):
        return 1/3 * ((1/2 * self.alas * self.ta) * self.tl)

class Tabung (Bangun_Ruang):
    def __init__ (self, jari_jari, tinggi):
        self.jari = jari_jari
        self.tinggi = tinggi
        
    def volume (self):
        return 22/7 * self.jari * self.jari * self.tinggi




def menu():
    while True:
        print("-" * 30)
        print(" Luas & Volume ".center(30," "))
        print("-" * 30)
        print("\n1. Luas \n2. Volume \n3. Keluar")
        pilihan = int(input("\nPilih Menu : "))
        if pilihan == 1:
            luas()
            
        elif pilihan == 2:
            volume()
        
        elif pilihan == 3:
            print("~" * 30)
            print(" KELUAR ".center(30," "))
            print("~" * 30)
            exit()
        
        else:
            print("Perintah Tidak Ditemukan!")
            


def luas():
    while True:
        print("-" * 30)
        print(" LUAS BANGUN DATAR ".center(30, " "))
        print("-" * 30)
        print("\n1. Persegi \n2. Segitiga \n3. Lingkaran \n4. Kembali")
        pilihan = int(input("\nPilih Menu : "))
        if pilihan == 1:
            print("-" * 30)
            print(" LUAS PERSEGI ".center(30," "))
            print("-" * 30)
            sisi = float(input("Sisi : "))
            persegi = Persegi (sisi)
            print("Luas Persegi : ", persegi.luas(), "Cm2")
            print("-" * 30)

        elif pilihan == 2:
            print("-" * 30)
            print(" LUAS SEGITGA ".center(30," "))
            print("-" * 30)
            alas = float(input("Alas Segitiga : "))
            tinggi = float(input("Tinggi Segitiga : "))
            segitiga = Segitiga (alas, tinggi)
            print("Luas Segitiga : ", segitiga.luas(), "Cm2")
            print("-" * 30)

        elif pilihan == 3:
            print("-" * 30)
            print(" LUAS LINGKARAN ".center(30," "))
            print("-" * 30)
            jari_jari = float(input("Jari-Jari : "))
            lingkaran = Lingkaran (jari_jari)
            print("Luas Lingkaran : ", lingkaran.luas(), "Cm2")
            print("-" * 30)

        elif pilihan == 4:
            menu()
        else:
            print("Perintah Tidak Ditemukan")
        


def volume():
    while True:
        print("-" * 30)
        print(" MENGHITUNG VOLUME ".center(30, " "))
        print("-" * 30)
        print("\n1. Kubus \n2. Limas Segitiga \n3. Tabung \n4. Kembali")
        pilihan = int(input("\nPilih Menu : "))
        if pilihan == 1:
            print("-" * 30)
            print(" VOLUME KUBUS ".center(30," "))
            print("-" * 30)
            sisi = float(input("Sisi : "))
            kubus = Kubus (sisi)
            print("Volume Kubus : ", kubus.volume(), "Cm3")
            print("-" * 30)
            
        elif pilihan == 2:
            print("-" * 30)
            print(" VOLUME LIMAS SEGITIGA ".center(30,"="))
            print("-" * 30)
            alas = float(input("Alas : "))
            tinggi_alas = float(input("Tinggi Alas : "))
            tinggi_limas = float(input("Tinggi Limas : "))
            limas = Limas (alas, tinggi_alas, tinggi_limas)
            print("Volume Limas : ", limas.volume(), "Cm3")
            print("-" * 30)

        elif pilihan == 3:
            print("-" * 30)
            print(" VOLUME TABUNG ".center(30," "))
            print("-" * 30)
            jari_jari = float(input("Jari-Jari Lingkaran Tabung : "))
            tinggi = float(input("Tinggi Tabung : "))
            tabung = Tabung (jari_jari, tinggi)
            print("Volume Tabung : ", tabung.volume(), "Cm3")
            print("-" * 30)
            
        elif pilihan == 4:
                menu()
        else:
            print("Perintah Tidak Ditemukan")
            
            
menu()