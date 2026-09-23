class Pemain:
    nama_game = "Clash Royale"
    versi_game = "2026"
    total_pemain = 0

    def __init__(self, nama, level, trophy):
        self.nama = nama
        self.level = level
        self.__trophy = trophy
        Pemain.total_pemain += 1

    def tampilkan_info(self):
        print(f"Nama   : {self.nama}")
        print(f"Level  : {self.level}")
        print(f"Trophy : {self.__trophy}")

    @property
    def trophy(self):
        return self.__trophy

    @trophy.setter
    def trophy(self, nilai):
        if nilai < 0:
            print("Trophy tidak boleh negatif.")
        else:
            self.__trophy = nilai
            print("Trophy berhasil diperbarui.")

    @classmethod
    def dari_data(cls, data):
        return cls(
            data["nama"],
            data["level"],
            data["trophy"]
        )

class Deck:
    total_deck = 0
    maksimal_kartu = 8
    def __init__(self, nama_deck, jenis_deck, pemain):
        self.nama_deck = nama_deck
        self.jenis_deck = jenis_deck
        self.pemain = pemain
        self.kartu = []
        Deck.total_deck += 1

    def tambah_kartu(self, kartu):
        if len(self.kartu) < Deck.maksimal_kartu:
            self.kartu.append(kartu)
            print(f"{kartu.nama} berhasil ditambahkan.")
        else:
            print("Deck sudah berisi 8 kartu.")

    def tampilkan_deck(self):
        print(f"\nNama Deck : {self.nama_deck}")
        print(f"Jenis     : {self.jenis_deck}")
        print(f"Pemain    : {self.pemain.nama}")
        print("Daftar Kartu:")

        for kartu in self.kartu:
            print(
                f"- {kartu.nama} | "
                f"{kartu.rarity} | "
                f"Elixir: {kartu.elixir}"
            )
        print(f"Jumlah Kartu: {len(self.kartu)}/8")

class Kartu:
    total_kartu = 0
    jenis_game = "Clash Royale"
    def __init__(self, nama, rarity, elixir):
        # Atribut instance
        self.nama = nama
        self.rarity = rarity
        self.__elixir = elixir
        Kartu.total_kartu += 1

    @property
    def elixir(self):
        return self.__elixir

    @elixir.setter
    def elixir(self, nilai):
        if nilai < 0:
            print("Elixir tidak boleh negatif.")
        else:
            self.__elixir = nilai
            print("Elixir berhasil diperbarui.")

    def tampilkan_kartu(self):
        print(
            f"Nama: {self.nama}, "
            f"Rarity: {self.rarity}, "
            f"Elixir: {self.__elixir}"
        )

    @staticmethod
    def validasi_elixir(nilai):
        return 1 <= nilai <= 10

print("==========================================")
print(" SISTEM MANAJEMEN DECK DAN PEMAIN")
print("             CLASH ROYALE")
print("==========================================")

data_pemain1 = {
    "nama": "Navtaly",
    "level": 15,
    "trophy": 6500
}

data_pemain2 = {
    "nama": "Orang",
    "level": 14,
    "trophy": 5800
}

pemain1 = Pemain.dari_data(data_pemain1)
pemain2 = Pemain.dari_data(data_pemain2)

print("\n========== DATA PEMAIN ==========")
pemain1.tampilkan_info()
print()
pemain2.tampilkan_info()

print("\n========== TEST SETTER TROPHY ==========")
print("Trophy sebelum:", pemain1.trophy)
pemain1.trophy = 7000
print("Trophy setelah:", pemain1.trophy)
pemain1.trophy = -500
print("Trophy tetap:", pemain1.trophy)
kartu1 = Kartu("Knight", "Rare", 3)
kartu2 = Kartu("Fireball", "Rare", 4)
kartu3 = Kartu("Archers", "Common", 3)
kartu4 = Kartu("Hog Rider", "Rare", 4)
kartu5 = Kartu("Cannon", "Common", 3)
kartu6 = Kartu("Ice Spirit", "Common", 1)
kartu7 = Kartu("Skeletons", "Common", 1)
kartu8 = Kartu("The Log", "Legendary", 2)

print("\n========== DATA KARTU ==========")
kartu1.tampilkan_kartu()
kartu2.tampilkan_kartu()

print("\n========== STATIC METHOD ==========")
print(
    "Elixir 4 valid:",
    Kartu.validasi_elixir(4)
)

print(
    "Elixir 15 valid:",
    Kartu.validasi_elixir(15)
)

print("\n========== TEST SETTER ELIXIR ==========")
print("Elixir sebelum:", kartu1.elixir)
kartu1.elixir = 4
print("Elixir setelah:", kartu1.elixir)
kartu1.elixir = -2
print("Elixir tetap:", kartu1.elixir)

deck1 = Deck(
    "Deck Navtaly",
    "Hog Rider Cycle",
    pemain1
)

deck2 = Deck(
    "Deck Orang",
    "Beatdown",
    pemain2
)

deck1.tambah_kartu(kartu1)
deck1.tambah_kartu(kartu2)
deck1.tambah_kartu(kartu3)
deck1.tambah_kartu(kartu4)
deck1.tambah_kartu(kartu5)
deck1.tambah_kartu(kartu6)
deck1.tambah_kartu(kartu7)
deck1.tambah_kartu(kartu8)

deck2.tambah_kartu(kartu8)
deck2.tambah_kartu(kartu7)
deck2.tambah_kartu(kartu6)
deck2.tambah_kartu(kartu5)
deck2.tambah_kartu(kartu4)
deck2.tambah_kartu(kartu3)
deck2.tambah_kartu(kartu2)
deck2.tambah_kartu(kartu1)

print("\n========== DATA DECK ==========")
deck1.tampilkan_deck()
deck2.tampilkan_deck()

print("\n========== TEST BATAS DECK ==========")
kartu_tambahan = Kartu("Mini P.E.K.K.A", "Rare", 4)
deck1.tambah_kartu(kartu_tambahan)

print("\n========== ATRIBUT KELAS ==========")
print("Nama Game       :", Pemain.nama_game)
print("Versi Game      :", Pemain.versi_game)
print("Total Pemain    :", Pemain.total_pemain)
print("Total Deck      :", Deck.total_deck)
print("Maksimal Kartu  :", Deck.maksimal_kartu)
print("Total Kartu     :", Kartu.total_kartu)
print("Jenis Game      :", Kartu.jenis_game)