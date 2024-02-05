"""
Keyword else

else digunakan sebagai blok seleksi kondisi penutup ketika blok if dan/atau elif dalam satu chain tidak ada yang terpenuhi. Contoh:

"""

str_input = input("Enter the Grade : \n")
grade = int(str_input)

if grade == 100:
    print("perfect")
elif grade >= 85:
    print("awesome")
elif grade >= 65:
    print("passed the examp")
else:
    print("Below the passing Grade")