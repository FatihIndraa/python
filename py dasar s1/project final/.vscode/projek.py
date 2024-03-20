admin = 'A'
ventela= []
patrobas = []
vans = []

while (admin == 'A'):
    print ('===SELAMAT DATANG===')
    print ('\n1. Lihat data \n2. tambah data\n3. edit data \n4. keluar program')
    pilihan = int (input ('pilih salah satu data: '))
    if (pilihan == 1):
        print ('===MAU LIHAT DATA YANG MNANA?===')
        print ('\n1. VENNTELA\n2. PAROBAS\n3. VANS\n4. kembali')
        pilihan = input ('\nmau pilih yang mana: ')
        if (pilihan ==1):
            if (ventela):
                for act in ventela:
                    jual = act.split("/")

                    print (f"\nMerk Sepatu : {jual[0]}\nSize : {jual[1]}\nJumlah : {jual[2]}")
                print ("=================================================")
            else:
                print ("Data Kosong")
        elif (pilihan == 2):
            if (patrobas):
                for act in patrobas:
                    jual: act.split ('/')
                    
                    print (f"\nMerk Sepatu : {jual[0]}\nSize : {jual[1]}\nJumlah : {jual[2]}")
                print ("=================================================")
        #==========belom
    if (pilihan == 2):
        print ('===TAMBAH BARANG===')
        print ('\n1. VENTELA\n2. PATROBAS\n3. VANS')
        pilihan = int(input('pilih barang mana yang mau ditambah: '))
        if (pilihan == 1):
            serial = input ('masukkan serialnya:')
            harga = int (input ('masukkan harganya: '))
            jumlah = int (input ('masukkan jumlah barang: '))
        if (pilihan == 2):
            serial = input ('masukkan serialnya:')
            harga = int (input ('masukkan harganya: '))
            jumlah = int (input ('masukkan jumlah barang: '))
        if (pilihan == 3):
            serial = input ('masukkan serialnya:')
            harga = int (input ('masukkan harganya: '))
            jumlah = int (input ('masukkan jumlah barang: '))
        ventela.append(f"{serial}/{harga}/{jumlah}")
        patrobas.append(f"{serial}/{harga}/{jumlah}")
        vans.append(f"{serial}/{harga}/{jumlah}")
