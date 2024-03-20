import os

print ("Nama    : Fatih Indra Maulana")
print ("NIM     : 202251026")
print ("Kelas   : A")
print ("\n")

print ("===== PROGRAM LUAS LINGKARAN =====\n")

# pemilihan rumus
phi = 3.14

print ("mau pake jari-jari apa diameter broww\n\n1. pake jari-jari (r)\n2. diameter (D)\n")

rumus = input("pilih nomor 1 atau 2: ")
if rumus == "1" :
    r = float (input('masukkan jari-jari: '))
    Luas = phi*(r**2)
    print('\njadi luasnya adalah: ', Luas, '\n')
elif rumus == "2" :
    d = float (input('masukkan diameter: '))
    Luas = 1/4 * (phi * (d**2))
    print ('\njadi luasnya adalah: ', Luas, '\n')
else :
    os.system ('cls')
    