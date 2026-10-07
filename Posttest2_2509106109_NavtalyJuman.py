class Kartu:
    total_kartu = 0
    jenis_game = "Clash Royale"
    maksimal_elixir = 10

    def __init__(self, nama, rarity, elixir):
        self._nama = nama
        self.rarity = rarity
        self.__elixir = elixir
        Kartu.total_kartu += 1

    def tampilkan_kartu(self):
        print(
            f"Nama: {self._nama} | "
            f"Rarity: {self.rarity} | "
            f"Elixir: {self.__elixir}"
        )

    @property
    def elixir(self):
        return self.__elixir

    @elixir.setter
    def elixir(self, nilai):
        if nilai < 0:
            print("Elixir tidak boleh negatif.")
        elif nilai > Kartu.maksimal_elixir:
            print("Elixir maksimal adalah 10.")
        else:
            self.__elixir = nilai
            print("Elixir berhasil diperbarui.")

    @staticmethod
    def validasi_elixir(nilai):
        return 1 <= nilai <= 10

    @classmethod
    def tampilkan_total_kartu(cls):
        print(f"Total kartu: {cls.total_kartu}")


class KartuPasukan(Kartu):

    def __init__(self, nama, rarity, elixir, jumlah_pasukan):
        super().__init__(nama, rarity, elixir)
        self.jumlah_pasukan = jumlah_pasukan

    def tampilkan_kartu(self):
        super().tampilkan_kartu()
        print(f"Jumlah Pasukan: {self.jumlah_pasukan}")


class KartuMantra(Kartu):

    def __init__(self, nama, rarity, elixir, efek):
        super().__init__(nama, rarity, elixir)
        self.efek = efek

    def tampilkan_kartu(self):
        super().tampilkan_kartu()
        print(f"Efek Mantra: {self.efek}")


class Pemain:
    nama_game = "Clash Royale"
    versi_game = "2026"
    total_pemain = 0

    def __init__(self, nama, level, trophy):
        self.nama = nama
        self.level = level
        self.__trophy = trophy
        self.daftar_deck = []
        Pemain.total_pemain += 1

    def tampilkan_info(self):
        print(f"Nama   : {self.nama}")
        print(f"Level  : {self.level}")
        print(f"Trophy : {self.__trophy}")
        print(f"Jumlah Deck: {len(self.daftar_deck)}")

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

    def tambah_deck(self, deck):
        self.daftar_deck.append(deck)
        print(f"Deck '{deck.nama_deck}' ditambahkan ke pemain {self.nama}.")

    def lihat_deck(self, deck):
        print(f"\nPemain {self.nama} melihat deck '{deck.nama_deck}'.")
        deck.tampilkan_deck()


class Deck:
    total_deck = 0
    maksimal_kartu = 8
    jenis_deck = "Battle Deck"

    def __init__(self, nama_deck, jenis_deck):
        self.nama_deck = nama_deck
        self.jenis_deck = jenis_deck
        self.kartu = []
        Deck.total_deck += 1

    def tambah_kartu(self, kartu):
        if len(self.kartu) < Deck.maksimal_kartu:
            self.kartu.append(kartu)
            print(f"{kartu._nama} berhasil ditambahkan ke {self.nama_deck}.")
        else:
            print("Deck sudah berisi 8 kartu.")

    def buat_kartu_pasukan(
        self,
        nama,
        rarity,
        elixir,
        jumlah_pasukan
    ):
        if len(self.kartu) < Deck.maksimal_kartu:
            kartu = KartuPasukan(
                nama,
                rarity,
                elixir,
                jumlah_pasukan
            )

            self.kartu.append(kartu)

            print(
                f"{nama} berhasil dibuat dan "
                f"ditambahkan ke {self.nama_deck}."
            )
        else:
            print("Deck sudah berisi 8 kartu.")

    def buat_kartu_mantra(
        self,
        nama,
        rarity,
        elixir,
        efek
    ):
        if len(self.kartu) < Deck.maksimal_kartu:
            kartu = KartuMantra(
                nama,
                rarity,
                elixir,
                efek
            )

            self.kartu.append(kartu)

            print(
                f"{nama} berhasil dibuat dan "
                f"ditambahkan ke {self.nama_deck}."
            )
        else:
            print("Deck sudah berisi 8 kartu.")

    def tampilkan_deck(self):
        print("\n==========================================")
        print(f"Nama Deck : {self.nama_deck}")
        print(f"Jenis     : {self.jenis_deck}")
        print("Daftar Kartu:")
        print("==========================================")

        for nomor, kartu in enumerate(self.kartu, start=1):
            print(f"{nomor}. ", end="")
            kartu.tampilkan_kartu()

        print(f"Jumlah Kartu: {len(self.kartu)}/{Deck.maksimal_kartu}")


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

deck1 = Deck(
    "Deck Navtaly",
    "Hog Rider Cycle"
)

deck2 = Deck(
    "Deck Orang",
    "Beatdown"
)

print("\n========== RELASI AGREGASI ==========")

pemain1.tambah_deck(deck1)
pemain2.tambah_deck(deck2)

print("\n========== MEMBUAT KARTU DECK 1 ==========")

deck1.buat_kartu_pasukan(
    "Knight",
    "Rare",
    3,
    1
)

deck1.buat_kartu_mantra(
    "Fireball",
    "Rare",
    4,
    "Memberikan damage area"
)

deck1.buat_kartu_pasukan(
    "Archers",
    "Common",
    3,
    2
)

deck1.buat_kartu_pasukan(
    "Hog Rider",
    "Rare",
    4,
    1
)

deck1.buat_kartu_pasukan(
    "Cannon",
    "Common",
    3,
    1
)

deck1.buat_kartu_pasukan(
    "Ice Spirit",
    "Common",
    1,
    1
)

deck1.buat_kartu_pasukan(
    "Skeletons",
    "Common",
    1,
    3
)

deck1.buat_kartu_mantra(
    "The Log",
    "Legendary",
    2,
    "Mendorong dan memberikan damage"
)

print("\n========== MEMBUAT KARTU DECK 2 ==========")

deck2.buat_kartu_pasukan(
    "Giant",
    "Rare",
    5,
    1
)

deck2.buat_kartu_mantra(
    "Arrows",
    "Common",
    3,
    "Memberikan damage area"
)

deck2.buat_kartu_pasukan(
    "Wizard",
    "Rare",
    5,
    1
)

deck2.buat_kartu_pasukan(
    "Mini P.E.K.K.A",
    "Rare",
    4,
    1
)

deck2.buat_kartu_pasukan(
    "Bomber",
    "Common",
    2,
    1
)

deck2.buat_kartu_pasukan(
    "Musketeer",
    "Rare",
    4,
    1
)

deck2.buat_kartu_pasukan(
    "Mega Minion",
    "Rare",
    3,
    1
)

deck2.buat_kartu_mantra(
    "Zap",
    "Common",
    2,
    "Memberikan damage dan stun"
)

print("\n========== DATA DECK ==========")

deck1.tampilkan_deck()
deck2.tampilkan_deck()

print("\n========== RELASI ASOSIASI ==========")

pemain1.lihat_deck(deck1)
pemain2.lihat_deck(deck2)

print("\n========== TEST INHERITANCE ==========")

kartu_pasukan1 = KartuPasukan(
    "Valkyrie",
    "Rare",
    4,
    1
)

kartu_pasukan2 = KartuPasukan(
    "Pekka",
    "Epic",
    7,
    1
)

kartu_mantra1 = KartuMantra(
    "Rocket",
    "Rare",
    6,
    "Damage besar pada area"
)

kartu_mantra2 = KartuMantra(
    "Freeze",
    "Epic",
    4,
    "Membekukan pasukan"
)

print("\n--- Kartu Pasukan ---")

kartu_pasukan1.tampilkan_kartu()

print()

kartu_pasukan2.tampilkan_kartu()

print("\n--- Kartu Mantra ---")

kartu_mantra1.tampilkan_kartu()

print()

kartu_mantra2.tampilkan_kartu()

print("\n========== STATIC METHOD ==========")

print(
    "Elixir 4 valid:",
    Kartu.validasi_elixir(4)
)

print(
    "Elixir 15 valid:",
    Kartu.validasi_elixir(15)
)

print("\n========== CLASS METHOD ==========")

Kartu.tampilkan_total_kartu()

print("\n========== TEST SETTER ELIXIR ==========")

print(
    "Elixir sebelum:",
    kartu_pasukan1.elixir
)

kartu_pasukan1.elixir = 5

print(
    "Elixir setelah:",
    kartu_pasukan1.elixir
)

kartu_pasukan1.elixir = -2

print(
    "Elixir tetap:",
    kartu_pasukan1.elixir
)

print("\n========== TEST BATAS DECK ==========")

deck1.buat_kartu_pasukan(
    "Mini P.E.K.K.A",
    "Rare",
    4,
    1
)

print("\n========== ATRIBUT KELAS ==========")

print("Nama Game       :", Pemain.nama_game)
print("Versi Game      :", Pemain.versi_game)
print("Total Pemain    :", Pemain.total_pemain)
print("Total Deck      :", Deck.total_deck)
print("Maksimal Kartu  :", Deck.maksimal_kartu)
print("Total Kartu     :", Kartu.total_kartu)
print("Jenis Game      :", Kartu.jenis_game)