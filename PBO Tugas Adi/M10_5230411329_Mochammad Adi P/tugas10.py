import mysql.connector

conn = mysql.connector.connect(
    user = "root",
    host = "localhost",
    password = "",
    database = "penjual"
)   

cur = conn.cursor()

#Membuat database
# cur.execute("CREATE DATABASE penjual")

#membuat tabel Pegawai(done)
cur.execute("""CREATE TABLE pegawai(
            nik VARCHAR(25), 
            nama_pegawai VARCHAR(25), 
            alamat_pegawai VARCHAR(255)
            )""")

# #membuat tabel Transaksi(belum)
# cur.execute("""CREATE TABLE Kuliah (
#             Kode_MK CHAR(4) NOT NULL PRIMARY KEY,
#             Kode_Dos CHAR(4) ,
#             Waktu VARCHAR(25),
#             Tempat VARCHAR(15) )""")
# #membuat tabel Struk(belum)
# cur.execute("""CREATE TABLE Mata_Kuliah (
#             Kode_MK CHAR(4) NOT NULL PRIMARY KEY,
#             Nama_MK VARCHAR(25),
#             SKS INT(1),
#             Semester INT(2)
#              )""")

# membuat tabel Produk(done)
# cur.execute("""CREATE TABLE produk (
#             kode_produk CHAR(4) NOT NULL PRIMARY KEY,
#             nama_Produk VARCHAR(25),
#             jenis_Produk Varchar(25),
#             harga INT(6)
#             )""")

