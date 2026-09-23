
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
