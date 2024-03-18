'''
tujuan = str(input('masukkan lokasi tujuan: (JATIM/JABAR/JATENG)'))
berat = float(input('masukkan beratnya: '))

jatim = 50000
jabar = 75000
jateng = 25000

if (tujuan == "JATIM"):
    tipe = int(input('masukkan tipe yang diinginkan \n1. regular\n2. expres\npilih (1/2)\n'))
    if (tipe == 1):
        print("ongkirnya yaitu: ", jatim * berat)
    elif (tipe == 2):
        print("ongkirnya yaitu: ", jatim * berat + 50000)
        
if (tujuan == "JABAR"):
    tipe = int(input('masukkan tipe yang diinginkan \n1. regular\n2. expres\npilih (1/2)\n'))
    if (tipe == 1):
        print("ongkirnya yaitu: ", jabar * berat)
    elif (tipe == 2):
        print("ongkirnya yaitu: ", jabar * berat + 50000)

if (tujuan == "JATENG"):
    tipe = int(input('masukkan tipe yang diinginkan \n1. regular\n2. expres\npilih (1/2)\n'))
    if (tipe == 1):
        print("ongkirnya yaitu: ", jateng * berat)
    elif (tipe == 2):
        print("ongkirnya yaitu: ", jateng * berat + 50000)

'''
tujuan = str(input('masukkan lokasi tujuan: (JATIM/JABAR/JATENG)'))
berat = float(input('masukkan beratnya: '))
expres = str(input('mau pake expres: (Y/N)'))

if (tujuan == "JATIM"):
    biaya = 50000
elif (tujuan == "JABAR"):
    biaya = 75000
elif (tujuan == 'JATENG'):
    biaya = 25000
elif (tujuan == "JATENG"):
    biaya = 25000
else :
    biaya = 30000
if(expres == "Y"):
    total = biaya*berat+20000
else:
    total = biaya*berat
    
print ("total ongkirnya Rp.", total)
    
