# bangun datar

print('==PROGRAM LUAS BANGUN DATAR==')
luas = int(input('masukkan program luas yang mau di cari: \n1. persegi\n2. persegi panjang \n3. segitiga\n4. jajar genjang\n5. lingkaran\nmasukkan salah satu ya:\t'))

if (luas == 1):
    sisi = float(input('masukkan sisi dari persegi: '))
    hasil = sisi**2
    print ('jadi luasnya yaitu: ', hasil)
    
elif (luas == 2):
    alas = float(input('masukkan alas dari persegi panjang: '))
    tinggi = float(input('masukkan tinggi dari persegi panjang: '))
    hasil = alas * tinggi
    print ('jadi luasnya yaitu: ', hasil)
    
elif (luas == 3):
    alas = float(input('masukkan alas segitiga: '))
    tinggi = float(input('masukkan tinggi dari segitiga: '))
    hasil = alas * tinggi / 2
    print ('jadi luasnya yaitu: ', hasil)
    
elif (luas == 4):
    alas = float(input('masukkan alas jajargenjang: '))
    tinggi = float(input('masukkan tinggi dari jajar genjang: '))
    hasil = alas * tinggi
    print ('jadi luasnya yaitu: ', hasil)
    
elif (luas == 5):
    r = float(input('masukkan jari jari lingkaran: '))
    phi = 3.14
    hasil = phi * (r**2)
    print ('jadi luasnya yaitu: ', hasil)
    
else:
    print('hanya 5 rumus')
