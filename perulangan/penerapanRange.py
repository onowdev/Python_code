"""
Penerapan fungsi range()
Statement range(n) menghasilkan data range sejumlah n yang isinya dimulai dari angka 0. Syntax range(n) adalah bentuk paling sederhana penerapan fungsi ini.

Selain range(n) ada juga beberapa cara penulisan lainnya:

Menggunakan range(start, stop). Hasilnya data range dimulai dari start dan hingga stop - 1. Sebagai contoh, range(1, 4) menghasilkan data range [1, 2, 3].

Menggunakan range(start, stop, step). Hasilnya data range dimulai dari start dan hingga stop - 1, dengan nilai increment sejumlah step. Sebagai contoh, range(1, 10, 3) menghasilkan data range [1, 4, 7].
"""

for i in range(9):
    print("urutan: ", i)
    
print("\n")

for i in range(0, 10):
    print("Index ke : ", i)


print("\n")


for i in range(0, 15, 3):
    print("Index ke: ", i)