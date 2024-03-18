# kondisi percabangan IF ,IF ELSE, ELIF

# IF
member = input ("apakah member? (Y/N): ")

if (member == "Y"):
    print ("selamat dapat diskon 10%")
 
# IF ELSE

angka = int(input ("masukkan angka berapa saja: "))
hasil = angka%2

if (hasil == 1):
    print (angka, "adalah termasuk angka ganjil")
else:
    print (angka, "adalah termasuk angka genap")

# ELSE IF ELIF

nilai = int (input("masukkan nilai akhir: "))
if (nilai >= 86):
    print ("A")
elif (nilai >= 75):
    print ("B")
elif (nilai >= 65):
    print ("C")
else:
    print ("D")

