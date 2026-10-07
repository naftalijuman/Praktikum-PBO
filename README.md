
# Sistem Manajemen Deck dan Pemain Clash Royale

## Deskripsi Program

Program ini dibuat menggunakan bahasa Python dengan pendekatan
Pemrograman Berorientasi Objek (PBO). Program digunakan untuk mengelola
data pemain, deck, dan kartu pada Clash Royale.

Program memiliki tiga class utama, yaitu `Pemain`, `Deck`, dan `Kartu`.

## Struktur Class

### 1. Class Pemain
Class `Pemain` digunakan untuk menyimpan data pemain seperti nama,
level, dan trophy.

### 2. Class Deck
Class `Deck` digunakan untuk mengelola deck yang dimiliki oleh pemain.
Setiap deck memiliki maksimal 8 kartu.

### 3. Class Kartu
Class `Kartu` digunakan untuk menyimpan data kartu seperti nama,
rarity, dan elixir.

## Atribut dan Method

Program menggunakan atribut kelas dan atribut instance.

Jenis method yang digunakan:
- Instance method
- Class method
- Static method

## Encapsulation dan Property

Encapsulation diterapkan pada atribut private:
- `__trophy` pada class `Pemain`
- `__elixir` pada class `Kartu`

Atribut private diakses menggunakan `@property` sebagai getter dan
`@property.setter` sebagai setter.

Setter memiliki validasi sehingga nilai trophy dan elixir tidak boleh
bernilai negatif.

## Pengujian Program

Pengujian dilakukan dengan:
1. Membuat minimal 2 object dari setiap class.
2. Menampilkan data pemain, deck, dan kartu.
3. Menggunakan instance method.
4. Menggunakan class method.
5. Menggunakan static method.
6. Menguji setter dengan data yang valid.
7. Menguji setter dengan data yang tidak valid.
8. Menguji batas maksimal 8 kartu dalam satu deck.

## Cara Menjalankan Program

Pastikan Python sudah terpasang, kemudian jalankan file program melalui
terminal dengan perintah:

```bash
python Posttest1_2509106109_NavtalyJuman.py



# Posttest 2
## Sistem Manajemen Deck dan Pemain Clash Royale

### Deskripsi Program
Program Posttest 2 merupakan pengembangan dari program Posttest 1 dengan menerapkan relasi antar objek dan konsep inheritance pada Pemrograman Berorientasi Objek (PBO).

Program menggunakan tema Sistem Manajemen Deck dan Pemain Clash Royale dengan class Pemain, Deck, Kartu, KartuPasukan, dan KartuMantra.

### Struktur Class

#### 1. Class Kartu
Class Kartu merupakan superclass yang digunakan sebagai dasar untuk jenis kartu pada program.

Atribut yang digunakan:
- `_nama`
- `rarity`
- `__elixir`

#### 2. Class KartuPasukan
Class KartuPasukan merupakan subclass dari Kartu.

Atribut khusus:
- `jumlah_pasukan`

Class ini menggunakan `super().__init__()` untuk memanggil constructor dari superclass Kartu.

Method `tampilkan_kartu()` juga dioverride untuk menampilkan informasi jumlah pasukan.

#### 3. Class KartuMantra
Class KartuMantra merupakan subclass dari Kartu.

Atribut khusus:
- `efek`

Class ini menggunakan `super().__init__()` untuk memanggil constructor dari superclass Kartu.

Method `tampilkan_kartu()` dioverride untuk menampilkan efek mantra.

#### 4. Class Pemain
Class Pemain digunakan untuk menyimpan data pemain dan deck yang dimiliki pemain.

Atribut yang digunakan:
- `nama`
- `level`
- `__trophy`
- `daftar_deck`

#### 5. Class Deck
Class Deck digunakan untuk mengelola kartu yang terdapat dalam deck.

Setiap deck memiliki maksimal 8 kartu.

### Relasi UML

#### 1. Association
Association diterapkan antara class Pemain dan Deck melalui method `lihat_deck()`.

Pemain dapat melihat informasi sebuah deck yang diberikan sebagai parameter.

#### 2. Aggregation
Aggregation diterapkan pada hubungan Pemain dengan Deck.

Objek Deck dibuat secara terpisah kemudian dimasukkan ke dalam `daftar_deck` milik Pemain menggunakan method `tambah_deck()`.

#### 3. Composition
Composition diterapkan pada hubungan Deck dengan Kartu.

Objek `KartuPasukan` dan `KartuMantra` dibuat dari dalam class Deck melalui method `buat_kartu_pasukan()` dan `buat_kartu_mantra()` kemudian dimasukkan ke dalam deck.

### Inheritance

Inheritance diterapkan dengan menggunakan:

- Superclass: `Kartu`
- Subclass: `KartuPasukan`
- Subclass: `KartuMantra`

Kedua subclass memanggil constructor superclass menggunakan `super().__init__()`.

Masing-masing subclass memiliki atribut khusus:
- `KartuPasukan` memiliki `jumlah_pasukan`
- `KartuMantra` memiliki `efek`

Method `tampilkan_kartu()` pada superclass dioverride oleh kedua subclass.

### Encapsulation

Encapsulation tetap diterapkan pada program.

Atribut private yang digunakan:
- `__trophy` pada class Pemain
- `__elixir` pada class Kartu

Atribut `_nama` pada class Kartu menggunakan protected attribute karena diperlukan oleh subclass.

Akses terhadap atribut private dilakukan menggunakan property getter dan setter.

### Pengujian Program

Pengujian dilakukan dengan:

1. Membuat dua object Pemain.
2. Membuat dua object Deck.
3. Menambahkan deck ke pemain menggunakan aggregation.
4. Membuat kartu pasukan dan kartu mantra melalui Deck.
5. Menguji relasi association melalui method `lihat_deck()`.
6. Menguji inheritance melalui class KartuPasukan dan KartuMantra.
7. Menguji pemanggilan `super().__init__()`.
8. Menguji overriding method `tampilkan_kartu()`.
9. Menguji static method `validasi_elixir()`.
10. Menguji class method `tampilkan_total_kartu()`.
11. Menguji setter trophy dengan nilai valid dan tidak valid.
12. Menguji setter elixir dengan nilai valid dan tidak valid.
13. Menguji batas maksimal 8 kartu dalam deck.

### Cara Menjalankan Program

Pastikan Python sudah terpasang, kemudian jalankan file Posttest 2 melalui terminal dengan perintah:

```bash
python Posttest2_2509106109_NavtalyJuman.py
