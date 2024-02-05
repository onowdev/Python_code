"""
Perulangan atau loop merupakan teknik untuk mengulang-ulang
eksekusi suatu blok kode, atau mengiterasi elemen milik tipe data kolektif (contohnya: list).


Perulangan di Python bisa dibuat menggunakan kombinasi keyword for dan fungsi range().

Keyword for adalah keyword untuk perulangan, dalam penerapannya diikuti dengan keyword in.
Fungsi range() digunakan untuk membuat object range, yang umumnya dipakai sebagai kontrol perulangan.

"""

for i in range(5):
    print("index", i)


"""
Penjelasan:

Statement print("index:", i) muncul 5 kali, karena perulangan dilakukan dengan kontrol range(5) dimana statement tersebut menghasilkan object range dengan isi deret angka sejumlah 5 dimulai dari angka 0 hingga 4.

Statement for i in range(5): adalah contoh penulisan perulangan menggunakan for dan range(). Variabel i berisi nilai counter setiap iterasi, yang pada konteks ini adalah angka 0 hingga 4.

Statement print("index:", i) wajib ditulis menjorok ke kanan karena merupakan isi dari blok perulangan for i in range(5):...
"""