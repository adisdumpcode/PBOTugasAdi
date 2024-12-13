import mysql.connector

conn = mysql.connector.connect(
    user = "root",
    host = "localhost",
    password = "",
    database = "penjual"
)   

cur = conn.cursor()

# Membuat database
# cur.execute("CREATE DATABASE penjual")

# membuat tabel Pegawai(done)
# cur.execute("""CREATE TABLE pegawai(
#             nik CHAR(4) NOT NULL PRIMARY KEY, 
#             nama_pegawai VARCHAR(25), 
#             alamat_pegawai VARCHAR(255)
#             )""")

# membuat tabel Transaksi(done)
# cur.execute("""CREATE TABLE transaksi (
#             no_transaksi CHAR(4) NOT NULL PRIMARY KEY,
#             nama_pegawai CHAR(4) ,
#             tanggal VARCHAR(25)
#             )""")

# membuat tabel Struk(don)
# cur.execute("""CREATE TABLE struk (
#             no_struk CHAR(4) NOT NULL PRIMARY KEY,
#             no_transaksi CHAR(4),
#             kode_produk CHAR(4),
#             jumlah_produk INT(4),
#             total_harga INT(6)
#              )""")

# membuat tabel Produk(done)
# cur.execute("""CREATE TABLE produk (
#             kode_produk CHAR(4) NOT NULL PRIMARY KEY,
#             nama_Produk VARCHAR(25),
#             jenis_Produk Varchar(25),
#             harga INT(6)
#             )""")

# Add Foreign Key(struk)
# cur.execute("""ALTER TABLE struk
#             ADD FOREIGN KEY (no_transaksi)
#             REFERENCES transaksi (no_transaksi)""")

# foreign key kode_produk
# cur.execute("""ALTER TABLE struk
#             ADD FOREIGN KEY (kode_produk)
#             REFERENCES transaksi (kode_produk)""")

# cur.execute("""ALTER TABLE struk
#             ADD FOREIGN KEY(no_transaksi)
#             REFERENCES transaksi(no_transaksi)""")


def tampil_data_transaksi():
    cur.execute("SELECT * FROM transaksi")
    data = cur.fetchall()
    print("\nData Transaksi:")
    for row in data:
        print(row)

def input_produk():
    kode_produk = input("Masukkan kode produk (4 karakter): ")
    nama_produk = input("Masukkan nama produk: ")
    jenis_produk = input("Masukkan jenis produk: ")
    harga = int(input("Masukkan harga produk: "))
    cur.execute("INSERT INTO produk (kode_produk, nama_produk, jenis_produk, harga) VALUES (%s, %s, %s, %s)",
                (kode_produk, nama_produk, jenis_produk, harga))
    conn.commit()
    print("Produk berhasil ditambahkan!")

def tampil_data_produk():
    cur.execute("SELECT * FROM produk")
    data = cur.fetchall()
    print("\nDaftar Produk:")
    for row in data:
        print(row)

def update_produk():
    kode_produk = input("Masukkan kode produk yang ingin diupdate: ")
    cur.execute("SELECT * FROM produk WHERE kode_produk = %s", (kode_produk,))
    if cur.fetchone():
        nama_produk = input("Masukkan nama produk baru: ")
        jenis_produk = input("Masukkan jenis produk baru: ")
        harga = int(input("Masukkan harga baru: "))
        cur.execute("UPDATE produk SET nama_produk = %s, jenis_produk = %s, harga = %s WHERE kode_produk = %s",
                    (nama_produk, jenis_produk, harga, kode_produk))
        conn.commit()
        print("Produk berhasil diperbarui!")
    else:
        print("Kode produk tidak ditemukan!")

def delete_produk():
    kode_produk = input("Masukkan kode produk yang ingin dihapus: ")
    cur.execute("SELECT * FROM produk WHERE kode_produk = %s", (kode_produk,))
    if cur.fetchone():
        cur.execute("DELETE FROM produk WHERE kode_produk = %s", (kode_produk,))
        conn.commit()
        print("Produk berhasil dihapus!")
    else:
        print("Kode produk tidak ditemukan!")

def input_transaksi():
    # Tampilkan daftar pegawai terlebih dahulu
    tampil_data_pegawai()
    
    # Input transaksi baru
    no_transaksi = input("Masukkan nomor transaksi (4 karakter): ")
    nik_pegawai = input("Masukkan NIK pegawai yang melayani: ")
    
    # Validasi apakah NIK pegawai ada
    cur.execute("SELECT nama_pegawai FROM pegawai WHERE nik = %s", (nik_pegawai,))
    pegawai = cur.fetchone()
    if not pegawai:
        print("NIK pegawai tidak ditemukan!")
        return
    
    tanggal = input("Masukkan tanggal transaksi (YYYY-MM-DD): ")
    
    # Simpan transaksi ke tabel transaksi
    cur.execute("INSERT INTO transaksi (no_transaksi, nama_pegawai, tanggal) VALUES (%s, %s, %s)",
                (no_transaksi, nik_pegawai, tanggal))
    conn.commit()
    print(f"Transaksi berhasil ditambahkan oleh {pegawai[0]}!")

    # Tambahkan produk ke tabel struk
    while True:
        no_struk = input("Masukkan nomor struk (4 karakter): ")
        kode_produk = input("Masukkan kode produk: ")
        jumlah_produk = int(input("Masukkan jumlah produk: "))
        
        # Ambil harga produk dari tabel produk
        cur.execute("SELECT harga FROM produk WHERE kode_produk = %s", (kode_produk,))
        result = cur.fetchone()
        if result is None:
            print("Kode produk tidak ditemukan!")
            continue
        harga = result[0]
        total_harga = jumlah_produk * harga
        
        # Simpan detail produk ke tabel struk
        cur.execute(
            "INSERT INTO struk (no_struk, no_transaksi, kode_produk, jumlah_produk, total_harga) VALUES (%s, %s, %s, %s, %s)",
            (no_struk, no_transaksi, kode_produk, jumlah_produk, total_harga))
        conn.commit()
        print("Produk berhasil ditambahkan ke struk!")
        
        tambah_lagi = input("Tambah produk lain ke transaksi ini? (y/n): ").lower()
        if tambah_lagi == 'n':
            break


def delete_transaksi():
    no_transaksi = input("Masukkan nomor transaksi yang ingin dihapus: ")
    cur.execute("SELECT * FROM transaksi WHERE no_transaksi = %s", (no_transaksi,))
    if cur.fetchone():
        cur.execute("DELETE FROM transaksi WHERE no_transaksi = %s", (no_transaksi,))
        conn.commit()
        print("Transaksi berhasil dihapus!")
    else:
        print("Nomor transaksi tidak ditemukan!")

def tampil_struk():
    no_transaksi = input("Masukkan nomor transaksi: ")
    
    # Query dengan metode JOIN untuk mendapatkan data struk lengkap
    query = """
        SELECT s.no_struk, s.kode_produk, p.nama_produk, s.jumlah_produk, p.harga, s.total_harga
        FROM struk s
        JOIN produk p ON s.kode_produk = p.kode_produk
        WHERE s.no_transaksi = %s
    """
    cur.execute(query, (no_transaksi,))
    data = cur.fetchall()
    
    if data:
        print("\nStruk untuk transaksi nomor:", no_transaksi)
        print(f"{'No. Struk':<10}{'Kode Produk':<12}{'Nama Produk':<25}{'Jumlah':<8}{'Harga':<10}{'Total':<10}")
        print("-" * 75)
        for row in data:
            print(f"{row[0]:<10}{row[1]:<12}{row[2]:<25}{row[3]:<8}{row[4]:<10}{row[5]:<10}")
    else:
        print("Tidak ada data struk untuk nomor transaksi ini.")

def tampil_data_pegawai():
    cur.execute("SELECT nik, nama_pegawai FROM pegawai")
    data = cur.fetchall()
    print("\nDaftar Pegawai:")
    print(f"{'NIK':<10}{'Nama Pegawai':<25}")
    print("-" * 35)
    for row in data:
        print(f"{row[0]:<10}{row[1]:<25}")

def input_pegawai():
    nik = input("Masukkan NIK pegawai (4 karakter): ")
    nama_pegawai = input("Masukkan nama pegawai: ")
    alamat_pegawai = input("Masukkan alamat pegawai: ")

    cur.execute("INSERT INTO pegawai (nik, nama_pegawai, alamat_pegawai) VALUES (%s, %s, %s)",
                (nik, nama_pegawai, alamat_pegawai))
    conn.commit()
    print("Pegawai berhasil ditambahkan!")

def update_pegawai():
    nik = input("Masukkan NIK pegawai yang ingin diupdate: ")
    
    # Cek apakah NIK pegawai ada di database
    cur.execute("SELECT * FROM pegawai WHERE nik = %s", (nik,))
    pegawai = cur.fetchone()
    
    if pegawai:
        print(f"Pegawai ditemukan: {pegawai}")
        nama_pegawai = input("Masukkan nama pegawai baru (kosongkan jika tidak ingin diubah): ") or pegawai[1]
        alamat_pegawai = input("Masukkan alamat pegawai baru (kosongkan jika tidak ingin diubah): ") or pegawai[2]
        
        # Update data pegawai
        cur.execute("UPDATE pegawai SET nama_pegawai = %s, alamat_pegawai = %s WHERE nik = %s",
                    (nama_pegawai, alamat_pegawai, nik))
        conn.commit()
        print("Data pegawai berhasil diperbarui!")
    else:
        print("NIK pegawai tidak ditemukan.")

def delete_pegawai():
    nik = input("Masukkan NIK pegawai yang ingin dihapus: ")
    
    # Cek apakah NIK pegawai ada di database
    cur.execute("SELECT * FROM pegawai WHERE nik = %s", (nik,))
    if cur.fetchone():
        cur.execute("DELETE FROM pegawai WHERE nik = %s", (nik,))
        conn.commit()
        print("Pegawai berhasil dihapus!")
    else:
        print("NIK pegawai tidak ditemukan.")




def menu():
    while True:
        print("\nKasir Dafina:")
        print("1. Kelola Data Pegawai")
        print("2. Kelola Data Produk")
        print("3. Kelola Transaksi dan Struk")
        print("0. Keluar")
        
        pilihan = input("Pilih menu (1/2/3/0): ")
        if pilihan == '1':
            menu_pegawai()
        elif pilihan == '2':
            menu_produk()
        elif pilihan == '3':
            menu_transaksi_dan_struk()
        elif pilihan == '0':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def menu_pegawai():
    while True:
        print("\nMenu Kelola Data Pegawai:")
        print("1. Tampilkan Data Pegawai")
        print("2. Tambahkan Data Pegawai")
        print("3. Update Data Pegawai")
        print("4. Hapus Data Pegawai")
        print("0. Kembali ke Menu Utama")
        
        pilihan = input("Pilih menu (1/2/3/4/0): ")
        if pilihan == '1':
            tampil_data_pegawai()
        elif pilihan == '2':
            input_pegawai()
        elif pilihan == '3':
            update_pegawai()
        elif pilihan == '4':
            delete_pegawai()
        elif pilihan == '0':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def menu_produk():
    while True:
        print("\nMenu Kelola Data Produk:")
        print("1. Tampilkan Data Produk")
        print("2. Tambahkan Produk Baru")
        print("3. Update Produk")
        print("4. Hapus Produk")
        print("0. Kembali ke Menu Utama")
        
        pilihan = input("Pilih menu (1/2/3/4/0): ")
        if pilihan == '1':
            tampil_data_produk()
        elif pilihan == '2':
            input_produk()
        elif pilihan == '3':
            update_produk()
        elif pilihan == '4':
            delete_produk()
        elif pilihan == '0':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def menu_transaksi_dan_struk():
    while True:
        print("\nMenu Kelola Transaksi dan Struk:")
        print("1. Tampilkan Data Transaksi")
        print("2. Tambahkan Transaksi Baru")
        print("3. Hapus Transaksi")
        print("4. Tampilkan Struk")
        print("0. Kembali ke Menu Utama")
        
        pilihan = input("Pilih menu (1/2/3/4/0): ")
        if pilihan == '1':
            tampil_data_transaksi()
        elif pilihan == '2':
            input_transaksi()
        elif pilihan == '3':
            delete_transaksi()
        elif pilihan == '4':
            tampil_struk()
        elif pilihan == '0':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")




menu()

# Tutup koneksi
cur.close()
conn.close()
