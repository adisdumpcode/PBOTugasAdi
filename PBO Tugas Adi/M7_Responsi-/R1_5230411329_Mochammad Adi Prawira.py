class Pegawai:
    def __init__(self, pegawai, nama, alamat):
        self.pegawai = pegawai
        self.nama = nama
        self.alamat = alamat

class Transaksi:
    def __init__(self, no_transaksi, pegawai):
        self.no_transaksi = no_transaksi
        self.pegawai = pegawai
        self.produk_list = []

    def tambah_produk(self, produk):
        self.produk_list.append(produk)

    def detail_transaksi(self):
        details = f"Transaksi No: {self.no_transaksi}\nPegawai: {self.pegawai.nama}\n"
        total_harga = 0
        for produk in self.produk_list:
            details += f"{produk.nama_produk} - {produk.jenis_produk}: {produk.harga}\n"
            total_harga += produk.harga
        details += f"Total Harga: {total_harga}\n"
        return details

class Struk:
    def __init__(self, transaksi):
        self.no_transaksi = transaksi.no_transaksi
        self.nama_pegawai = transaksi.pegawai.nama
        self.produk_list = transaksi.produk_list

    def display_struk(self):
        struk_details = f"Struk No: {self.no_transaksi}\nPegawai: {self.nama_pegawai}\n"
        total_harga = 0
        for produk in self.produk_list:
            struk_details += f"{produk.nama_produk} - {produk.jenis_produk}: {produk.harga}\n"
            total_harga += produk.harga
        struk_details += f"Total Harga: {total_harga}\n"
        return struk_details

class Produk:
    def __init__(self, kode_produk, nama_produk, jenis_produk, harga):
        self.kode_produk = kode_produk
        self.nama_produk = nama_produk
        self.jenis_produk = jenis_produk
        self.harga = harga

class Snack(Produk):
    def __init__(self, kode_produk, nama_produk, harga):
        super().__init__(kode_produk, nama_produk, "Snack", harga)

class Makanan(Produk):
    def __init__(self, kode_produk, nama_produk, harga):
        super().__init__(kode_produk, nama_produk, "Makanan", harga)

class Minuman(Produk):
    def __init__(self, kode_produk, nama_produk, harga):
        super().__init__(kode_produk, nama_produk, "Minuman", harga)

def tambah_pegawai():
    print("===Tambah Pegawai===")
    id_pegawai = input("Masukkan No Pegawai: ")
    nama = input("Masukkan Nama Pegawai: ")
    alamat = input("Masukkan Alamat Pegawai: ")
    pegawai = Pegawai(id_pegawai, nama, alamat)
    pegawai_list.append(pegawai)
    print(f"Pegawai {nama} ditambahkan!")

def tambah_produk():
    print("===Tambah Produk===")
    print("1. Tambah Snack")
    print("2. Tambah Makanan")
    print("3. Tambah Minuman")
    pilihan = input("Pilih jenis produk: ")

    kode_produk = input("Masukkan Kode Produk: ")
    nama_produk = input("Masukkan Nama Produk: ")
    harga = int(input("Masukkan Harga Produk: "))

    if pilihan == "1":
        produk = Snack(kode_produk, nama_produk, harga)
    elif pilihan == "2":
        produk = Makanan(kode_produk, nama_produk, harga)
    elif pilihan == "3":
        produk = Minuman(kode_produk, nama_produk, harga)
    else:
        print("Pilihan tidak valid.")
        return

    produk_list.append(produk)
    print(f"Produk {nama_produk} berhasil ditambahkan.")

def add_transaksi():
    if not pegawai_list:
        print("Tidak ada pegawai terdaftar. Silakan tambahkan pegawai terlebih dahulu.")
        return

    no_transaksi = input("Masukkan No Transaksi: ")
    print("Daftar Pegawai:")
    for i, pegawai in enumerate(pegawai_list):
        print(f"{i + 1}. {pegawai.nama}")
    index_pegawai = int(input("Pilih pegawai: ")) - 1

    if index_pegawai < 0 or index_pegawai >= len(pegawai_list):
        print("Pilihan tidak valid.")
        return

    pegawai = pegawai_list[index_pegawai]
    transaksi = Transaksi(no_transaksi, pegawai)

    while True:
        print("\nDaftar Produk:")
        for i, produk in enumerate(produk_list):
            print(f"{i + 1}. {produk.nama_produk} - {produk.jenis_produk}: {produk.harga}")
        
        index_produk = input("Pilih produk (atau ketik 'd' untuk selesai): ")
        if index_produk.lower() == 'd':
            break

        index_produk = int(index_produk) - 1
        if index_produk < 0 or index_produk >= len(produk_list):
            print("Pilihan tidak valid.")
        else:
            transaksi.tambah_produk(produk_list[index_produk])
            print(f"Produk {produk_list[index_produk].nama_produk} berhasil ditambahkan ke transaksi.")

    transaksi_list.append(transaksi)
    print(f"Transaksi {no_transaksi} berhasil dibuat.")

def display_struk():
    if not transaksi_list:
        print("Tidak ada transaksi yang dibuat.")
        return

    print("\nDaftar Transaksi:")
    for i, transaksi in enumerate(transaksi_list):
        print(f"{i + 1}. Transaksi No: {transaksi.no_transaksi}")

    index_transaksi = int(input("Pilih transaksi untuk melihat struk: ")) - 1
    if index_transaksi < 0 or index_transaksi >= len(transaksi_list):
        print("Pilihan tidak valid.")
        return

    transaksi = transaksi_list[index_transaksi]
    struk = Struk(transaksi)
    print("\n=== Struk Pembelian ===")
    print(struk.display_struk())
    
pegawai_list = []
produk_list = []
transaksi_list = []


def menu():
    while True:
        print("\n=== Program Menu ===")
        print("1. Tambah Pegawai")
        print("2. Tambah Produk")
        print("3. Buat Transaksi")
        print("4. Tampilkan Struk")
        print("5. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_pegawai()
        elif pilihan == "2":
            tambah_produk()
        elif pilihan == "3":
            add_transaksi()
        elif pilihan == "4":
            display_struk()
        elif pilihan == "5":
            print("Tprogram ditutup")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
    
menu()
