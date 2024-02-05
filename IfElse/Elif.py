"""
elif (kependekan dari else if) digunakan untuk menambahkan blok seleksi kondisi baru, 
untuk mengantisipasi blok if yang tidak terpenuhi.
Dalam penerapannya, suatu blok seleksi kondisi harus diawali dengan if. 
Keyword elif hanya bisa dipergunakan pada kondisi setelahnya yang masih satu rantai (masih satu chain). 
"""

str_input = input("Enter the Grades... ")
grade = int(str_input)

if grade == 100:
    print("Nilai Sempurna")
elif grade <= 90:
    print("Nilai Bagus")
elif grade <=80:
    print("Ayo belajar lagi ya")