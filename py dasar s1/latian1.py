print ('=====PROGRAM NILAI MAHASISWA=====')
total_presensi = int(input('sudah berapa kali presensi: '))
total_tugas = float(input('nilai tugasnya berapa: '))
total_uts = float(input('nilai UTS berapa: '))
total_uas = float(input('nilai uas beapa: '))

# rumus presentase
presensi = (total_presensi / 16) * (10/100 * 100)
tugas = 40/100 * total_tugas
uts = 20/100 * total_uts
uas = 30/100 * total_uas
nilai = presensi + tugas + uts + uas

# program nilai
if (total_presensi <= 16):
    print ('================================')
    print (presensi, '+', tugas, '+', uts, '+', uas, '=', nilai,)
    print ('JADI NILAI KAMU ADALAH: ', nilai)
    print ('================================')
else:
    print('kamu tidak lulus')

#program grade konversi
if (nilai >= 86):
    print ('selamat kamu mendapat grade A')
elif (nilai >= 75):
    print ('selamat kamu mendapat grade AB')
elif (nilai >= 66):
    print ('kamu dapat grade B')
elif (nilai >= 55):
    print ('kamu dapat grade BC')
else :
    print ('grade kamu C')
    