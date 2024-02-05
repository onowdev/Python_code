"""
Seleksi kondisi bercabang / nested
Seleksi kondisi bisa saja berada di dalam suatu blok seleksi kondisi. 
Teknik ini biasa disebut dengan seleksi kondisi bercabang atau bersarang.

Di Python, cara penerapannya cukup dengan menuliskan blok seleksi kondisi tersebut. 
Gunakan indentation yang lebih ke kanan untuk seleksi kondisi terdalam.
"""

str_input = input("Enter your Grade: \n")
grade = int(str_input)

if grade == 100:
    print("perfect")
elif grade >= 85:
    print("Awesome")
elif grade <= 65:
    print("passed the exam")
    
    if grade <=70:
        print("You Need to improve it")
    else:
        print("With oke Grade")
else:
    print("Below the passing grade")