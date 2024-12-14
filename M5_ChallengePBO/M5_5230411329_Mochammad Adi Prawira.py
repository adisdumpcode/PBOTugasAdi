class Music:

    def __init__(self, Judul, Penyanyi, Genre):
        self.Judul = Judul
        self.Penyanyi = Penyanyi
        self.Genre = Genre
    
    def display(self):
        print(f"Judul: ", self.Judul, "Penyanyi: ", self.Penyanyi, "Genre: ", self.Genre)

class Pop(Music):
    def __init__(self, Judul, Penyanyi):
        self.Judul = Judul
        self.Penyanyi = Penyanyi    
        super().__init__(Judul, Penyanyi, "Pop")
        self.playlist = []

    def add(self):
        self.playlist.append(self.Judul)
        print(f"lagu {self.Judul} Ditambah")
        
    def delete(self):
        if self.Judul in self.playlist:
            self.playlist.remove(self.Judul)
            print(f"Lagu: {self.Judul} Dihapus.")
        else:
            print("Tidak ditemukan")

class Rock(Music):
    def __init__(self, Judul, Penyanyi):
        self.Judul = Judul
        self.Penyanyi = Penyanyi    
        super().__init__(Judul, Penyanyi, "Rock")
        self.playlist = []

    def add(self):
        self.playlist.append(self.Judul)
        print(f"lagu {self.Judul} Ditambah")
        
    def delete(self):
        if self.Judul in self.playlist:
            self.playlist.remove(self.Judul)
            print(f"Lagu: {self.Judul} Dihapus.")
        else:
            print("Tidak ditemukan")

def tambah_lagu():
    judul = input("Masukkan Judul Lagu: ")
    penyanyi = input("Masukkan Nama Penyanyi: ")
    genre = input("Masukkan Genre (Pop/Rock/Jawa): ").lower()

    if genre == "pop":
        lagu = Pop(judul, penyanyi)
    elif genre == "rock":
        lagu = Rock(judul, penyanyi)
    elif genre == "jawa":
        lagu = Jawa(judul, penyanyi)
    else:
        print("Genre tidak valid.")
        return

    lagu.add()
    playlist.append(lagu)

class Jawa(Music):
    def __init__(self, Judul, Penyanyi):
        self.Judul = Judul
        self.Penyanyi = Penyanyi    
        super().__init__(Judul, Penyanyi," Jawa")
        self.playlist = []

    def add(self):
        self.playlist.append(self.Judul)
        print(f"lagu {self.Judul} ditambah.")
        
    def delete(self):
        if self.Judul in self.playlist:
            self.playlist.remove(self.Judul)
            print(f"Lagu: {self.Judul} dihapus.")
        else:
            print("Tidak ditemukan")

def lihat_playlist():
    if len(playlist) == 0:
        print("Playlist kosong, tidak ada lagu yang dapat diurutkan.")
    else:
        playlist_sorted = sorted(playlist, key=lambda lagu: lagu.Judul.lower())
        print("\nDaftar lagu di playlist (diurutkan A-Z):")
        for i, lagu in enumerate(playlist_sorted, start=1):
            print(f"{i}. Judul: {lagu.Judul}, Penyanyi: {lagu.Penyanyi}, Genre: {lagu.Genre}")

def hapus_lagu():
    judul_hapus = input("Masukkan judul lagu yang ingin dihapus: ")
    lagu_ditemukan = False

    for lagu in playlist:
        if lagu.Judul.lower() == judul_hapus.lower():
            playlist.remove(lagu) 
            print(f"Lagu '{lagu.Judul}' telah dihapus dari playlist.")
            lagu_ditemukan = True
            break
    
    if not lagu_ditemukan:
        print(f"Lagu tidak ditemukan di playlist.")

def menu_utama():
    global playlist
    playlist = []
    while True:
        print("=======")
        print("1. Tambah lagu")
        print("2. Lihat Playlist lagu")
        print("3. Hapus Lagu")
        print("4. Keluar")
        menut = input("Masukkan Pilihan(1/2/3): ")
        if menut == "1":
            print("===Tambah Lagu===")
            tambah_lagu()
        
        elif menut == "2":
            print("===Lihat Playlist lagu A-Z===")
            lihat_playlist()
        
        elif menut == "3":
            print("===Hapus Lagu===")
            hapus_lagu()

        elif menut == "4":
            print("===Berhasil Keluar===")
            break

        else:
            print("invalid, Masukkan lagi")
        continue

menu_utama()    