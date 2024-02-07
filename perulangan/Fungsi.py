"""
Fungsi range() menghasilkan object sequence, yaitu jenis data yang strukturnya mirip seperti list (tapi bukan list) 
yang kegunaan utamanya adalah untuk kontrol perulangan.

Object sequence bisa dikonversi bentuk list dengan cara dibungkus 
menggunakan fungsi list().
"""

r = range(15)
print("r:", list(r))