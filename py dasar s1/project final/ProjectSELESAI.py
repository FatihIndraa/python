# STATUS
menu = 'M'

# LIST PENJUALAN
penjualan = [['ventela', 200000],['patrobas',250000],['vans',500000]]

# LIST PEMBELIAN
pembelian = []
total = 0

while (menu == 'M'):
    pilihan = int(input ('\nMASUK SEBAGAI :\n\n1. PENJUAL \n2. PEMBELI\n3. KELUAR PROGRAM \n\npilih salah satu: '))
    
    # Penjual
    if (pilihan == 1):
        admin = "Y"
        while (admin == "Y"):
            print ('\n===== SELAMAT DATANG =====\n')
            print ("Input Menu\n1. Tambah Data\n2. Tampilkan Data\n3. Edit Data\n4. Hapus Data\n5. Keluar Aplikasi\n")
            pilihan = int(input("Masukkan nomor pilihan anda: "))
            
            #========== tambah data ===================
            if (pilihan == 1):
                merk = input("Masukkan merk sepatu: ")
                harga = int(input("Masukkan harga sepatu: "))
                dataProduk = [merk, harga]
                penjualan.append(dataProduk)
                print (f'serial: {dataProduk [0]}\tharga: {dataProduk[1]}')
            #========== lihat data ====================
            elif (pilihan == 2):
                if (penjualan):
                    for index, jual in enumerate (penjualan):
                        print (f'{index+1}|Serial: {jual [0]}\n\tHarga: Rp {jual [1]}')            
            #========== edit data ====================
            elif (pilihan == 3):
                for index, jual in enumerate (penjualan):
                        print (f'{index+1}|Serial: {jual [0]}\n\tHarga: Rp {jual [1]}')
                
                newData= int(input("data mana yang mau dirubah: "))
                
                merkBaru = input ('masukkan serial baru: ')
                hargaBaru = int (input ('masukkan harga baru: '))
                dataBaru = [merkBaru,hargaBaru]
                
                penjualan [newData-1] = dataBaru
                
            #========== hapus data ====================        
            elif (pilihan == 4):
                if (penjualan):
                    for index, jual in enumerate (penjualan):
                        print (f'{index+1}|Serial: {jual [0]}\n\tHarga: Rp {jual [1]}')
                hapus = int(input("Masukkan nama data yang akan dihapus: "))
                del penjualan[hapus-1]
                print ('\n===BERHASIL MENGHAPUS DATA===\n')
                
            elif (pilihan == 5):
                admin = "M"
                print ("Anda berhasil keluar dari aplikasi")

            else:
                print ("Pilihan yang anda masukkan salah")
        
    # CUSTOMER
    elif (pilihan == 2):
        customer = 'C'
        while (customer == 'C'):
            print ('==== SELAMAT DATANG ====\n')
            print ('1. Lihat barang\n2. Beli barang\n3. Keluar\n')
            pilihan = int (input ('silahkan pilih yang mana: '))
            if (pilihan == 1):
                if (penjualan):
                    for index, jual in enumerate (penjualan):
                        print (f'{index+1}|Serial: {jual [0]}\n\tHarga: Rp.{jual [1]}')
            elif (pilihan == 2):
               
                beli = 'p'
                while (beli == 'p'):
                     # tampilan produk
                    if (penjualan):
                        for index, jual in enumerate (penjualan):
                            print (f'{index+1}|Serial: {jual [0]}\n\tHarga: Rp.{jual [1]}')
                    pilihan = int (input ('barang mana yang mau dibeli: '))
                    size = float (input ('mau beli ukuran berapa: '))
                    pembelian1 = penjualan [pilihan - 1]
                    pembelian.append (pembelian1)
                    pembelian1.append (size)
                    pembelian2 = pembelian1 [1]
                    total += pembelian2 
                
                    print (f'Serial: {pembelian1 [0]}\tHarga: {pembelian1[1]}\tSize: {pembelian1[2]}')
                    tambahan = input ('ada tambahan? (y/n): ')
                    if (tambahan == 'n'):
                        beli = customer
                        print ('\n===== BARANG PEMBELIAN =====\n')
                        for index, jual in enumerate (pembelian):
                            print (f'\n|Serial: {jual [0]}\n\tHarga: Rp.{jual [1]} \tSize: {jual[2]}\n')
                        print (f'jadi totalnya adalah: Rp.{total}\n')
                

            else:
                customer = 'M'
                print ("Anda berhasil keluar dari aplikasi")
    else:
        menu = 'a'
        print ('\n\n===== berhasil keluar =====\n\n')