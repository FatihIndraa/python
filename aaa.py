print ('===TOKO SEPATU===')
merek = int(input('mau pake merek apa\t: \n1.ventela \n2. patrobas\nsilahkan pilih 1/2 '))

if (merek == 1):
    jenis = int(input('SERI APA: \n1. BASIC\n2. ETHCNIC\n3. PUBLIC\n4. BTS\nPilih satu ya '))
    basic = 210000
    ethnic = 200000
    public = 290000
    bts = 280000
    if (jenis == 1):
        potongan = 40000
        jumlah = basic - potongan 
    elif (jenis == 2):
        potongan = 40000
        jumlah = ethnic - potongan
    elif ( jenis == 3):
        potongan = 50000
        jumlah = public - potongan
    elif ( jenis == 4):
        potongan = 50000
        jumlah = bts - potongan
    else :
        jenis
    
    print ('jadi totalnya adalah Rp. ', jumlah)
elif (merek == 2):
    jenis = int(input('SERI APA: \n1. ivan\n2. equip\n3. cloud\nPilih salah satu ya '))
    ivan = 260000
    equip = 280000
    cloud = 30000
    if (jenis == 1):
        potongan = 40000
        jumlah = ivan - potongan
    elif (jenis == 2):
        potongan = 50000
        jumlah = equip - potongan
    elif (jenis == 3):
        potongan = 50000
        jumlah = cloud - potongan
    
              