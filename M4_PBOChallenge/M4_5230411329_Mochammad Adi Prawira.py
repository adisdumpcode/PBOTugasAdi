class Debitur:
    def __init__(self, nama, ktp, limpin):
        self.nama = nama
        self.__KTP = ktp
        self._limpin = limpin
        self.pinjaman_list = []
        
    def display(self):
        print("\n.Detail debitur")
        print("Nama: ", {self.nama})
        print("KTP: ", {self.__KTP})
        print("Total Pinjaman: ", {self._limpin})

class Pinjol():
    def __init__(self):
        self.debitur_list = []
    
    def tambah_debitur(self):
        while True:
            inktp = input("Masukkan KTP: ")
            if len(inktp) == 3:
                ktp = inktp
            else:
                print("Ktp Kurang/Lebih dari 3 digit. Masukkan lagi.")
                continue
            ktp_duplicate = any(debitur._Debitur__KTP == ktp for debitur in self.debitur_list)
            if ktp_duplicate:
                print(f"ktp {ktp} telah dimasukkan")
            else:
                nama = input("Masukkan Nama: ")
                _limpin = int(input("Masukkan limit pinjaman: "))
                debitur = Debitur(nama, ktp, _limpin)
                self.debitur_list.append(debitur)
                print(f"Debitur {nama} berhasil ditambahkan.")
                break

    def display(self):
        if not self.debitur_list:
            print("Belum ada debitur yang terdaftar.")
        else:
            for debitur in self.debitur_list:
                debitur.display()

    def sort(self, nama):
        for debitur in self.debitur_list:
            if debitur.nama.lower() == nama.lower():
                debitur.display()
                return
        print(f"Debitur dengan nama {nama} tidak ditemukan.")

    def validasi_ktp(self, identification):
        for debitur in self.debitur_list:
            if debitur._Debitur__KTP == identification:
                return debitur
        return None 

class Pinjaman:
    def __init__(self, pinjol):
        self.pinjol = pinjol

    def tambah_pinjaman(self):
        identification = int(input("Masukkan KTP debitur yang ingin ditambah pinjaman: "))
        debitur = self.pinjol.validasi_ktp(identification)

        if debitur:
            jumlah_pinjaman = int(input(f"Masukkan jumlah pinjaman untuk {debitur.nama}: "))
            if jumlah_pinjaman <= debitur._limpin:
                bunga = float(input("Masukkan persentase bunga (misal: 5 untuk 5%): "))
                periode_bulan = int(input("Masukkan periode (dalam bulan): "))

                
                angsuran_pokok = jumlah_pinjaman * (bunga / 100)
                angsuran_bulanan = angsuran_pokok / periode_bulan
                total_angsuran = angsuran_pokok + angsuran_bulanan

                pinjaman_info = {
                    'jumlah': jumlah_pinjaman,
                    'bunga': bunga,
                    'angsuran_pokok': angsuran_pokok,
                    'angsuran_bulanan': angsuran_bulanan,
                    'total_angsuran': total_angsuran
                }

                debitur.pinjaman_list.append(pinjaman_info)
                print(f"Pinjaman berhasil ditambahkan untuk {debitur.nama}.")
                print(f"Angsuran Pokok: {angsuran_pokok}, Angsuran Bulanan: {angsuran_bulanan}, Total Angsuran: {total_angsuran}")
            else:
                print(f"Pinjaman melebihi limit. Limit pinjaman {debitur._limpin}.")
        else:
            print(f"Debitur dengan KTP {identification} tidak ditemukan.")

    def tampilkan_pinjaman(self):
        identification = input("Masukkan nama atau KTP debitur untuk melihat pinjaman: ")
        debitur = self.pinjol.validasi_ktp(identification)

        if debitur:
            debitur.display()
        else:
            print(f"Debitur dengan nama/KTP {identification} tidak ditemukan.")

        

def menu_utama():
    pinjol = Pinjol()
    pinjaman = Pinjaman(pinjol)
    while True:
        print("Pinjol")
        print("1. KELOLA DEBITUR")
        print("2. KELOLA PINJAMAN")
        print("3. Exit")
        menut = input("Masukkan Pilihan(1/2/3): ")
        if menut == "1":
            print("===KELOLA DEBITUR== \n1. Tampilkan Debitur \n2. Cari Debitur \n3. Tambah Debitur")
            menu1 = input("Masukkan pilihan:(1/2/3):")
            if menu1 == "1":
                print("===TAMPILKAN DEBITUR===")
                pinjol.display()
            elif menu1 == "2":
                print("===Cari Debitur===")
                nama = input("Masukkan nama yang ingin dicari: ")
                pinjol.sort(nama)

            elif menu1 == "3":
                print("===TAMBAH DEBITUR===")
                pinjol.tambah_debitur()

        elif menut == "2":
            print("===KELOLA PINJAMAN== \n1. Tambah Pinjaman \n2. Tampilkan Pinjaman")
            menu2 = input("Masukkan Pilihan:(1/2): ")
            if menu2 == "1":
                print("==Tambah Pinjaman==")
                pinjaman.tambah_pinjaman()
            elif menu2 == "2":
                print("==Tampilkan Pinjaman==")
                pinjaman.tampilkan_pinjaman()
        
        else:
            print("Selesai")
            break


menu_utama()