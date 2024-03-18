'''
sebuah toko sepatu punya beberapa jenis merek yaitu ventela patrobas dan vans.
tiap merk berbeda harganya dan jenisnya. buatlah program tersebut
'''
admin = 'A'
ventela = []
harga_ventela = []
patrobas = []
harga_patrobas = []
vans = []
harga_vans = []


# pilihan pertama
while (admin == 'A'):
    print('\n=== SELAMAT DATANG ===')
    print('\n1. Lihat data Ventela\n2. Lihat data patrobas\n3. Lihat data vans\n4. Tambah data\n5. Kelular program')
    pilihan1 = int(input('pilih salah satu: '))

# lihat data

    if (pilihan1 == 1):
        if (ventela):
            x = 0
            print('=== DATA VENTELA ===')
            while (x < len(ventela)):
                print(f'\nSerial: {ventela[x]}\nHarga: {harga_ventela[x]}\n')
                x += 1
                print('================')
        else:
            print('\n====TIDAK ADA DATA====\n')
    elif (pilihan1 == 2):
        if (patrobas):
            x = 0
            print('=== DATA VENTELA ===')
            while (x < len(patrobas)):
                print(
                    f'\nSerial: {patrobas[x]}\nHarga: {harga_patrobas[x]}\n')
                x += 1
                print('================')
        else:
            print('\n====TIDAK ADA DATA====\n')
    elif (pilihan1 == 3):
        if (vans):
            x = 0
            print('=== DATA VENTELA ===')
            while (x < len(vans)):
                print(f'\nSerial: {vans[x]}\nHarga: {harga_vans[x]}\n')
                x += 1
                print('================')
        else:
            print('\n====TIDAK ADA DATA====\n')

# tambah data

    elif (pilihan1 == 4):
        print('\n\n=== Pilih data yang ingin ditambahkan ===\n')
        print('1. ventela\n2. patrobas\n3. vans')
        pilihan2 = int(input('mana yang ingin ditambahkan data: '))

        if (pilihan2 == 1):
            serial = input('masukkan serialnya: ')
            harga = int(input("masukkkan harganya: "))

            ventela.append(serial)
            harga_ventela.append(harga)
        if (pilihan2 == 2):
            serial = input('masukkan serialnya: ')
            harga = int(input("masukkkan harganya: "))

            patrobas.append(serial)
            harga_patrobas.append(harga)
        if (pilihan2 == 3):
            serial = input('masukkan serialnya: ')
            harga = int(input("masukkkan harganya: "))

            vans.append(serial)
            harga_vans.append(harga)
    elif (pilihan1 == 5):
        admin = 'n'
        print ('\n\n\n=== KELUAR PROGRAM ===\n\n\n')