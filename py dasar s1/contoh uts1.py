print ('==TOKO PAKET PREMIUM==')
paket = int(input('MAU BELLI YANG MANA BROWW: \n1. NETFLIX\t(Rp 35.000/bulan)\n2. VIU\t\t(Rp 25.000/bulan)\n3. PRIME VIDEO\t(Rp 40.000/bulan)\nPILIH SALAH SATU YA\t'))
lama = int (input('MAU BELI BUAT BERAPA BULAN: '))

netflix = 35000
viu = 25000
prime_video = 40000

if (paket == 1):
    total = netflix * lama
elif (paket == 2):
    total = viu * lama
elif (paket == 3):
    total = prime_video * lama
else :
    print ('cuma ada 3 paket')

pilihan = int(input ('MAU PAKE YANG MANA : \n1. BASIC\t(+Rp 5.000/bulan)\n2. PREMIUM\t(+Rp 10.000/bulan)\nPILIH SALAH SATU: '))
basic = 5000
premium = 10000

if (pilihan == 1):
    bulan = basic * lama
elif (pilihan == 2):
    bulan = premium * lama
else :
    print ('-')

total_tanpa_diskon = total + bulan

voucher = str(input ('MASUKKAN KODE VOUCRE BILA ADA: '))
if (voucher == "diskonmahasiswa"):
    potongan = 10/100
    diskon = total_tanpa_diskon * potongan
    total_pakai_diskon = total_tanpa_diskon - diskon
    print ('maka total yang harus dibayar yaitu Rp ', total_pakai_diskon)
else:
    print ('maka total yang harus dibayar yaitu Rp ', total_tanpa_diskon)