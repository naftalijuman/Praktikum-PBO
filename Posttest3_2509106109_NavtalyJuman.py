from abc import ABC, abstractmethod

class Kartu(ABC):
    total_kartu = 0
    maksimal_elixir = 10

    def __init__(self, nama, rarity, elixir):
        self._nama = nama
        self.rarity = rarity
        self.__elixir = elixir
        Kartu.total_kartu += 1

    @property
    def elixir(self):
        return self.__elixir

    @elixir.setter
    def elixir(self, nilai):
        if 0 <= nilai <= self.maksimal_elixir:
            self.__elixir = nilai
            print("Elixir berhasil diperbarui.")
        else:
            print("Elixir harus berada antara 0 dan 10.")

    @abstractmethod
    def gunakan(self):
        pass

    @abstractmethod
    def detail_khusus(self):
        pass

    def jalankan(self):
        self.detail_khusus()
        self.gunakan()

    def tampilkan_kartu(self):
        print(
            f"Nama: {self._nama} | "
            f"Rarity: {self.rarity} | "
            f"Elixir: {self.__elixir}"
        )

class KartuPasukan(Kartu):
    def __init__(self, nama, rarity, elixir, jumlah_pasukan):
        super().__init__(nama, rarity, elixir)
        self.jumlah_pasukan = jumlah_pasukan

    def detail_khusus(self):
        print(f"Jumlah pasukan: {self.jumlah_pasukan}")

    def gunakan(self):
        print(f"{self._nama} dikerahkan ke arena.")

    def tampilkan_kartu(self):
        super().tampilkan_kartu()
        print(f"Jumlah Pasukan: {self.jumlah_pasukan}")

class KartuMantra(Kartu):
    def __init__(self, nama, rarity, elixir, efek):
        super().__init__(nama, rarity, elixir)
        self.efek = efek

    def detail_khusus(self):
        print(f"Efek mantra: {self.efek}")

    def gunakan(self):
        print(f"{self._nama} digunakan: {self.efek}.")

    def tampilkan_kartu(self):
        super().tampilkan_kartu()
        print(f"Efek Mantra: {self.efek}")

class KartuBangunan(Kartu):
    def __init__(self, nama, rarity, elixir, target):
        super().__init__(nama, rarity, elixir)
        self.target = target

    def detail_khusus(self):
        print(f"Target bangunan: {self.target}")

    def gunakan(self):
        print(f"{self._nama} dipasang di arena.")

    def tampilkan_kartu(self):
        super().tampilkan_kartu()
        print(f"Target: {self.target}")

class Pemain:
    total_pemain = 0

    def __init__(self, nama, level, trophy):
        self.nama = nama
        self.level = level
        self.__trophy = trophy
        self.daftar_deck = []
        Pemain.total_pemain += 1

    @property
    def trophy(self):
        return self.__trophy

    @trophy.setter
    def trophy(self, nilai):
        if nilai >= 0:
            self.__trophy = nilai
            print("Trophy berhasil diperbarui.")
        else:
            print("Trophy tidak boleh negatif.")

    def tampilkan_info(self):
        print(
            f"Nama: {self.nama} | "
            f"Level: {self.level} | "
            f"Trophy: {self.__trophy}"
        )

    def tambah_deck(self, deck):
        self.daftar_deck.append(deck)
        print(f"Deck {deck.nama_deck} ditambahkan ke {self.nama}.")

    def lihat_deck(self, deck):
        print(f"{self.nama} melihat deck {deck.nama_deck}.")
        deck.tampilkan_deck()

    def tampilkan_ringkasan(self):
        print(
            f"Pemain {self.nama} memiliki "
            f"{len(self.daftar_deck)} deck."
        )

class Deck:
    maksimal_kartu = 8
    total_deck = 0

    def __init__(self, nama_deck, jenis_deck):
        self.nama_deck = nama_deck
        self.jenis_deck = jenis_deck
        self.kartu = []
        Deck.total_deck += 1

    def tambah_kartu(self, kartu: Kartu):
        if len(self.kartu) < self.maksimal_kartu:
            self.kartu.append(kartu)
            print(f"{kartu._nama} ditambahkan ke {self.nama_deck}.")
        else:
            print("Deck sudah berisi 8 kartu.")

    def buat_kartu_pasukan(
        self, nama, rarity, elixir, jumlah_pasukan
    ):
        if len(self.kartu) >= self.maksimal_kartu:
            print("Deck sudah berisi 8 kartu.")
            return

        kartu = KartuPasukan(
            nama, rarity, elixir, jumlah_pasukan
        )
        self.tambah_kartu(kartu)

    def buat_kartu_mantra(self, nama, rarity, elixir, efek):
        if len(self.kartu) >= self.maksimal_kartu:
            print("Deck sudah berisi 8 kartu.")
            return

        kartu = KartuMantra(nama, rarity, elixir, efek)
        self.tambah_kartu(kartu)

    def tampilkan_deck(self):
        print(f"\nDeck: {self.nama_deck}")
        print(f"Jenis: {self.jenis_deck}")

        for nomor, kartu in enumerate(self.kartu, start=1):
            print(f"\n{nomor}. ", end="")
            kartu.tampilkan_kartu()

        print(f"Jumlah kartu: {len(self)}/{self.maksimal_kartu}")

    def tampilkan_ringkasan(self):
        print(f"Deck {self.nama_deck} berisi {len(self)} kartu.")

    def __len__(self):
        return len(self.kartu)

    def __str__(self):
        return f"{self.nama_deck} ({len(self)}/8 kartu)"

def cetak_ringkasan(objek):
    objek.tampilkan_ringkasan()

print("=" * 45)
print(" SISTEM MANAJEMEN DECK DAN PEMAIN")
print("             CLASH ROYALE")
print("=" * 45)

print("\n========== BUKTI ABSTRAKSI ==========")

try:
    kartu_abstrak = Kartu("Contoh", "Rare", 3)
except TypeError as error:
    print("Abstract class tidak dapat dibuat menjadi objek.")
    print("Error:", error)

pemain1 = Pemain("Navtaly", 15, 6500)
pemain2 = Pemain("Pemain Kedua", 14, 5800)

deck1 = Deck("Deck Navtaly", "Hog Rider Cycle")
deck2 = Deck("Deck Pemain Kedua", "Beatdown")

print("\n========== DATA PEMAIN ==========")
pemain1.tampilkan_info()
pemain2.tampilkan_info()

print("\n========== RELASI AGREGASI ==========")
pemain1.tambah_deck(deck1)
pemain2.tambah_deck(deck2)

print("\n========== MEMBUAT KARTU ==========")

deck1.buat_kartu_pasukan("Knight", "Rare", 3, 1)
deck1.buat_kartu_mantra(
    "Fireball", "Rare", 4, "Memberikan damage area"
)
deck1.buat_kartu_pasukan("Archers", "Common", 3, 2)
deck1.buat_kartu_pasukan("Hog Rider", "Rare", 4, 1)
deck1.buat_kartu_pasukan("Cannon", "Common", 3, 1)
deck1.buat_kartu_pasukan("Ice Spirit", "Common", 1, 1)
deck1.buat_kartu_pasukan("Skeletons", "Common", 1, 3)
deck1.buat_kartu_mantra(
    "The Log", "Legendary", 2, "Mendorong pasukan lawan"
)

deck2.buat_kartu_pasukan("Giant", "Rare", 5, 1)
deck2.buat_kartu_mantra(
    "Arrows", "Common", 3, "Memberikan damage area"
)

print("\n========== DATA DECK ==========")
deck1.tampilkan_deck()
deck2.tampilkan_deck()

print("\n========== RELASI ASOSIASI ==========")
pemain1.lihat_deck(deck1)

print("\n========== ABSTRAKSI DAN POLIMORFISME ==========")

daftar_kartu = [
    KartuPasukan("Valkyrie", "Rare", 4, 1),
    KartuMantra("Freeze", "Epic", 4, "Membekukan pasukan"),
    KartuBangunan("Tesla", "Common", 4, "Pasukan udara dan darat")
]

for kartu in daftar_kartu:
    kartu.tampilkan_kartu()
    kartu.jalankan()
    print()

print("\n========== DUCK TYPING ==========")
cetak_ringkasan(pemain1)
cetak_ringkasan(deck1)

print("\n========== OPERATOR OVERLOADING ==========")
print("Informasi deck:", deck1)
print("Jumlah kartu deck 1:", len(deck1))

print("\n========== TEST PROPERTY ==========")
print("Trophy awal:", pemain1.trophy)
pemain1.trophy = 7000
print("Trophy sekarang:", pemain1.trophy)
pemain1.trophy = -500
print("Trophy setelah nilai tidak valid:", pemain1.trophy)

kartu_uji = daftar_kartu[0]
print("Elixir awal:", kartu_uji.elixir)
kartu_uji.elixir = 5
print("Elixir sekarang:", kartu_uji.elixir)
kartu_uji.elixir = 15
print("Elixir setelah nilai tidak valid:", kartu_uji.elixir)

print("\n========== BATAS DECK ==========")
print("Jumlah kartu deck 1:", len(deck1))
deck1.buat_kartu_pasukan("Mini P.E.K.K.A", "Rare", 4, 1)

print("\n========== TOTAL DATA ==========")
print("Total pemain:", Pemain.total_pemain)
print("Total deck:", Deck.total_deck)
print("Total kartu:", Kartu.total_kartu)