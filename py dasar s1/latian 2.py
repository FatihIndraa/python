mobil = int(input('mau pake mobil yg mana brow\t: \n1. LCGC\n2. MPV\n3. SPORT\n\nPilih salah satu ya: '))
hari = int(input("\nmau nyewa berapa hari: "))
sopir = str(input('\nmau pake sopir apa gak: (Y/N) '))

if (mobil == 1):
    biaya = 300000
elif (mobil == 2):
    biaya = 500000
elif (mobil == 3):
    biaya = 1000000
else :
    print ('gaada cok')
    
if (sopir == "Y"):
    tambahan = 200000 * hari

print ("totalnya jadi Rp.", biaya*hari+tambahan)

if (hari > 3):
    print ('\nSELAMAT ANDA MENDAPATKAN BONUS VOUCHER BELANJA')
else :
    print ('\nKEMBALIKAN TEPAT WAKTU YA')