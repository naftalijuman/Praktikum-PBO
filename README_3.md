POSTTEST 3 PBO

Sistem Manajemen Deck dan Pemain Clash Royale

Deskripsi Program

Program ini merupakan pengembangan sistem manajemen deck dan pemain Clash Royale menggunakan Python. Program menerapkan konsep Abstract Base Class (ABC), inheritance, polymorphism, duck typing, dan operator overloading.

1. Class Diagram UML

![Class Diagram UML](<Diagram Tanpa Judul.drawio.png>)

2. Penjelasan Relasi Antarclass

a. Asosiasi ("Pemain" dan "Deck")

Relasi asosiasi terdapat pada method "lihat_deck(deck)" di class "Pemain", yang menggunakan objek "Deck" untuk menampilkan isi deck.

b. Agregasi ("Pemain" dan "Deck")

Relasi agregasi terdapat pada atribut "daftar_deck" dan method "tambah_deck(deck)" di class "Pemain. Objek "Deck` dibuat secara terpisah sebelum ditambahkan ke pemain, sehingga deck tidak harus dibuat langsung oleh pemain.

c. Komposisi ("Deck" dan "Kartu")

Class "Deck" membuat objek kartu melalui method "buat_kartu_pasukan()" dan "buat_kartu_mantra()", kemudian menyimpannya dalam atribut "kartu". Hal ini menggambarkan hubungan kepemilikan deck terhadap kartu yang dimasukkan ke dalamnya.

d. Inheritance ("Kartu" dan subclass)

Class "KartuPasukan", "KartuMantra", dan "KartuBangunan" mewarisi class abstrak "Kartu". Setiap subclass memiliki atribut khusus dan mengimplementasikan method abstrak dengan perilaku yang berbeda.

3. Penerapan Abstraksi

Abstraksi diterapkan melalui class "Kartu" yang mewarisi "ABC". Class ini memiliki dua abstract method, yaitu "gunakan()" dan "detail_khusus()", serta method konkret "jalankan()" yang digunakan oleh subclass.

Subclass "KartuPasukan", "KartuMantra", dan "KartuBangunan" mengimplementasikan kedua abstract method tersebut. Program juga menggunakan "try-except TypeError" untuk menunjukkan bahwa class abstrak "Kartu" tidak dapat diinstansiasi secara langsung.

Screenshot Bukti Abstraksi

![Bukti Abstraksi](<Cuplikan layar 2026-10-27 204722.png>)

4. Penerapan Polimorfisme

a. Polimorfisme melalui Inheritance

Polimorfisme diterapkan dengan meng-override method "gunakan()" pada class "KartuPasukan", "KartuMantra", dan "KartuBangunan". Ketiga objek dipanggil melalui satu loop sehingga masing-masing menunjukkan perilaku yang berbeda.

b. Duck Typing

Duck typing diterapkan melalui fungsi "cetak_ringkasan(objek)". Fungsi ini dapat menerima objek "Pemain" maupun "Deck" karena keduanya memiliki method "tampilkan_ringkasan()", meskipun kedua class tersebut tidak memiliki hubungan inheritance.

c. Operator Overloading

Operator overloading diterapkan pada class "Deck" melalui method "__str__()" untuk menampilkan informasi deck dan "__len__()" untuk menghitung jumlah kartu dalam deck.

Screenshot Bukti Polimorfisme

![Bukti Polimorfisme](<Cuplikan layar 2026-10-27 204751.png>)

5. Kesimpulan

Program ini menerapkan abstraksi, inheritance, dan berbagai bentuk polimorfisme untuk mengelola kartu, deck, dan pemain Clash Royale. Diagram UML menunjukkan hubungan antarclass, sedangkan hasil eksekusi program membuktikan penerapan konsep tersebut.
