# STATUS 
customer = 'C'
menu = 'M'

# LIST PENJUALAN 
ventela = [['public 76s',290000],['bts',280000], ['republic',260000]]
patrobas = [['new ivan', 260000],['equip',290000],['cloud',300000]]
vans = [['checkerboard',550000],['oldskool', 500000]]
penjualan = [ventela, patrobas, vans]

# LIST PMEBELI 
beli = []
total = 0
while (menu == 'M'):
    pilihan = int (input ('\nMASUK SEBAGAI: \n\n1. PENJUAL \n2. PEMBELI\n\npilih salah satu: '))
    
    # PENUJUAL 
    if (pilihan == 1):
        admin = 'Y'
        while (admin == 'Y'):
            print ('\n\t===== SELAMAT DATANG =====\t\n')
            print ("Input Menu\n1. Tambah Data\n2. Tampilkan Data\n3. Edit Data\n4. Hapus Data\n5. Keluar Aplikasi")
            pilihan = int(input("Masukkan nomor pilihan anda: "))
            
            #=====TAMBAH DATA======
            if (pilihan == 1):
                print ('=====MASUK MENU TAMBAH DATA=====\n')
                pilihan = int (input ('1. VENTELA\n2. PATROBAS \n3. VANS\n4. KEMBALI\nPILIH SALAH SATU: '))
                
                # VENTELA APPEND
                if (pilihan == 1):
                    serial = input ('masukkan serialnya: ')
                    harga = int (input ('masukkan harganya: '))
                    
                    dataProduk = [serial,harga]
                    ventela.append(dataProduk)
                
                # PATROBAS APPEND
                elif (pilihan == 2):
                    serial = input ('masukkan serialnya: ')
                    harga = int (input ('masukkan harganya: '))
                    
                    dataProduk = [serial,harga]
                    patrobas.append(dataProduk)
                
                # VANS APPEND
                elif (pilihan == 3):
                    serial = input ('masukkan serialnya: ')
                    harga = int (input ('masukkan harganya: '))
                    
                    dataProduk = [serial,harga]
                    vans.append(dataProduk)
                
                # LOOPING BACK
                else: 
                    print ('')
            # LIHAT DATA
            elif (pilihan == 2):
                print ('=====MASUK MENU LIHAT DATA=====\n')
                pilihan = int (input ('1. VENTELA\n2. PATROBAS \n3. VANS\n4. KEMBALI\nPILIH SALAH SATU: '))
                
                # LIHAT DATA VENTELA
                if (pilihan == 1):
                    if (ventela):
                        for index, jual in enumerate (ventela):
                            print (f'\t|{index+1}|\tSerial: {jual [0]}\t\t\t|Harga: Rp {jual [1]} \t|')  
                
                # LIHAT DATA PATROBAS
                elif (pilihan == 2):
                    if (patrobas):
                        for index, jual in enumerate (patrobas):
                            print (f'\t|{index+1}|\tSerial: {jual [0]}\t\t\t|Harga: Rp {jual [1]} \t|') 
                
                # LIHAT DATA VANS
                elif (pilihan == 3):
                    if (vans):
                        for index, jual in enumerate (vans):
                            print (f'\t|{index+1}|\tSerial: {jual [0]}\t\t\t|Harga: Rp {jual [1]} \t|')   
                
                # LOOPING BACK
                else: 
                    print ('')     
            
            #===== EDIT DATA =====
            elif (pilihan == 3):
                print ('=====MASUK MENU EDIT DATA=====\n')
                pilihan = int (input ('1. VENTELA\n2. PATROBAS \n3. VANS\n4. KEMBALI\nPILIH SALAH SATU: '))
                
                # EDIT DATA VENTELA
                if (pilihan == 1):
                     if (ventela):
                        for index, jual in enumerate (ventela):
                            print (f'\t|{index+1}|\tSerial: {jual [0]}\t\t\t|Harga: Rp {jual [1]} \t|') 
                            
                        newData = int (input ('PILIH DATA MANA YANG MAU DI UBAH: '))
                        
                        seriBaru = input ('masukkan serial baru: ')
                        hargaBaru = int (input ('masukkan harga baru: '))
                        databaru = [seriBaru,hargaBaru]
                        
                        ventela [newData-1] = databaru
               
                # EDIT DATA PATROBAS
                elif (pilihan == 2):
                    if (patrobas):
                        for index, jual in enumerate (patrobas):
                            print (f'\t|{index+1}|\tSerial: {jual [0]}\t\t\t|Harga: Rp {jual [1]} \t|') 
                            
                        newData = int (input ('PILIH DATA MANA YANG MAU DI UBAH: '))
                        
                        seriBaru = input ('masukkan serial baru: ')
                        hargaBaru = int (input ('masukkan harga baru: '))
                        databaru = [seriBaru,hargaBaru]
                        
                        patrobas [newData-1] = databaru
                
                # EDIT DATA VANS        
                elif (pilihan == 3): 
                    if (vans):
                        for index, jual in enumerate (vans):
                            print (f'\t|{index+1}|\tSerial: {jual [0]}\t\t\t|Harga: Rp {jual [1]} \t|') 
                            
                        newData = int (input ('PILIH DATA MANA YANG MAU DI UBAH: '))
                        
                        seriBaru = input ('masukkan serial baru: ')
                        hargaBaru = int (input ('masukkan harga baru: '))
                        databaru = [seriBaru,hargaBaru]
                        
                        vans [newData-1] = databaru
                # LOOPING BACK
                else :
                    print ('')
            
            #===== HAPUS DATA =====
            elif (pilihan == 4):
                print ('=====MASUK MENU HAPUS DATA=====\n')
                pilihan = int (input ('1. VENTELA\n2. PATROBAS \n3. VANS\n4. KEMBALI\nPILIH SALAH SATU: '))
                
                # HAPUS DATA VENTELA
                if (pilihan == 1):
                    if (ventela):
                        for index, jual in enumerate (ventela):
                            print (f'\t{index+1}|Serial: {jual [0]} \t|Harga: {jual [1]} \t|Jumlah: {jual [2]} \t|')
                    hapus = int(input("Masukkan nama data yang akan dihapus: "))
                    del ventela[hapus-1]
                    print ('\n===BERHASIL MENGHAPUS DATA===\n')
                
                # HAPUS DATA PATROBAS
                elif (pilihan == 2):
                    if (patrobas):
                        for index, jual in enumerate (patrobas):
                            print (f'\t{index+1}|Serial: {jual [0]} \t|Harga: {jual [1]} \t|Jumlah: {jual [2]} \t|')
                    hapus = int(input("Masukkan nama data yang akan dihapus: "))
                    del patrobas[hapus-1]
                    print ('\n===BERHASIL MENGHAPUS DATA===\n')
                
                # HAPUS DATA VANS
                elif (pilihan == 3):
                    if (vans):
                        for index, jual in enumerate (vans):
                            print (f'\t{index+1}|Serial: {jual [0]} \t|Harga: {jual [1]} \t|Jumlah: {jual [2]} \t|')
                    hapus = int(input("Masukkan nama data yang akan dihapus: "))
                    del vans[hapus-1]
                    print ('\n===BERHASIL MENGHAPUS DATA===\n')
                
                # LOOPING BACK
                else:
                    print ('')
                    
            else:
                admin = 'M'
                print ('===== BERHASIL KELUAR APLIKASI =====')
    
    # CUSTOMER
    elif (pilihan == 2):
        while (customer == 'C'):
            print ('==== SELAMAT DATANG ====')
            print ('1. Lihat barang\n2. Beli barang\n3. Keluar')
            pilihan = int (input ('silahkan pilih yang mana: '))
            if (pilihan == 1):
                print ('=====MASUK MENU LIHAT BARANG=====\n')
                pilihan = int (input ('1. VENTELA\n2. PATROBAS \n3. VANS\n4. KEMBALI\nPILIH SALAH SATU: '))
                
                if (pilihan == 1):
                    # LIHAT DATA VENTELA
                    if (pilihan == 1):
                        if (ventela):
                            for index, jual in enumerate (ventela):
                                print (f'\t|{index+1}|\tSerial: {jual [0]}\t\t\t|Harga: Rp {jual [1]} \t|') 
                    
                    # LIHAT DATA PATROBAS
                    elif (pilihan == 2):
                        if (patrobas):
                            for index, jual in enumerate (patrobas):
                                print (f'\t|{index+1}|\tSerial: {jual [0]}\t\t\t|Harga: Rp {jual [1]} \t|') 
                    
                    # LIHAT DATA VANS
                    elif (pilihan == 3):
                        if (vans):
                            for index, jual in enumerate (vans):
                                print (f'\t|{index+1}|\tSerial: {jual [0]}\t\t\t|Harga: Rp {jual [1]} \t|')   
                    
                    # LOOPING BACK
                    else: 
                        print ('')     
                
            elif (pilihan == 2):
                print ('=====MASUK MENU BELI BARANG=====\n')
                pembelian = 'P'
                while (pembelian == 'P'):
                    pilihan = int (input ('1. VENTELA\n2. PATROBAS \n3. VANS\n4. KEMBALI\nPILIH SALAH SATU: '))
                    
                    # LIHAT DATA VENTELA
                    if (pilihan == 1):
                        if (ventela):
                            for index, jual in enumerate (ventela):
                                print (f'\t|{index+1}|\tSerial: {jual [0]}\t\t\t|Harga: Rp {jual [1]} \t|') 
                        
                        pilihan = int (input ('barang mana yang mau dibeli: '))
                        jumlah = int (input ('beli berapa banyak: '))
                        beli1 = ventela [pilihan -1]
                        beli.append(beli1)
                        
                    # LIHAT DATA PATROBAS
                    elif (pilihan == 2):
                        if (patrobas):
                            for index, jual in enumerate (patrobas):
                                print (f'\t|{index+1}|\tSerial: {jual [0]}\t\t\t|Harga: Rp {jual [1]} \t|') 
                        
                        pilihan = int (input ('barang mana yang mau dibeli: '))
                        jumlah = int (input ('beli berapa banyak: '))
                        beli1 = patrobas [pilihan -1]
                        beli.append(beli1)
                        
                    # LIHAT DATA VANS
                    elif (pilihan == 3):
                        if (vans):
                            for index, jual in enumerate (vans):
                                print (f'\t|{index+1}|\tSerial: {jual [0]}\t\t\t|Harga: Rp {jual [1]} \t|') 
                        
                        pilihan = int (input ('barang mana yang mau dibeli: '))
                        jumlah = int (input ('beli berapa banyak: '))
                        beli1 = vans [pilihan -1]
                        beli.append(beli1)
                    
                    # beli.append(beli1)
                    beli2 = beli1 [1]
                    total += (beli2*jumlah)
                            
                    print (f'serial: {beli1[0]}\t harga: {beli1[1]}\t Banyaknya: {jumlah}')    
                    tambahan = input ('ada tambahan? (y/n)')
                    if (tambahan == 'n'):
                        pembelian = customer
                        print ('\n=====================================\n')
                        for jual in (beli):
                            print (f'pembelian barang\t:\nserial:\t{jual[0]}\nharga:\t{jual[1]}')
                        print (f'\njadi totalnya adalah: \tRp.{total}\n')