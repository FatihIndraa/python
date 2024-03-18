# fungction

# sintaks menggunakan def ()


'''
# Statis
def sapa(nama, alamat):
    print ('selamat pagi,', nama, 'alamatnya di,', alamat)
# Pemanggilan function
sapa('Agus', 'kudus')         #Harus digunakan untuk memanggil fungsi
                              #Pakai 1 fungsi pemanggilan

#dinamis
def sapa (nama, alamat, umur):
    print ('\nselamt pagi', nama, '. Bertempat tinggal di,', alamat)
    if (umur >=17 ):
        print (f'\n{nama}, alamat di {alamat}, SUDAH MEMILIKI SIM')
    else:
        print (f'\n{nama}, alamat di {alamat}, BELOM MEMILIKI SIM')
        
nama = input ('masukkan nama: ')
alamat = input ('masukkan alamat: ')
umur = int (input('masukkan umurnya: '))
sapa(nama,alamat,umur)


# ===== FUNCTION GANJIL GENAP ====== #
def bilangan (angka):
    if (angka % 2 == 1):
        print (f'Angka {angka} adalah GANJIL')
    else:
        print (f'Angka {angka} adalah GENAP')
# angka = int (input('Masukkan angka yang mau di cek: '))
bilangan (int(input('masuk: ')))
'''

'''
# FUNCTION LUAS SEGITIGA

def luasSegitiga (alas, tinggi):
    luas = 1/2 * alas*tinggi
    return luas
    
a = int (input('masukkan alas segitiga: '))
t = int (input ('masukkan tinggi segitiga: '))
L = luasSegitiga (a, t)
print (f'jadi luas segitiga dengan alas {a}, dan tinggi {t}, Adalah {L}')
'''

# # FUNCTION MENGETAHUI PERSEGI DAN PERSEGI PANJANG BIASA

# def jenis (alas,tinggi):
#     if (a == t):
#         print ('ini adalah bangun PERSEGI')
#     else:
#         print ('ini adalah bangu PERSEGI PANJANG')

# a = int (input ('masukkan alas: '))
# t = int (input ('masukkan tinggi: '))
# jenis (a,t)

# # FUNCTION MENGETAHUI PERSEGI DAN PERSEGI PANJANG RETURN

# def jenis (alas,tinggi):
#     if (a == t):
#         hasil = 'PERSEGI'
#     else:
#         hasil = 'PERSEGI PANJANG'
#     return hasil

# a = int (input ('masukkan alas: '))
# t = int (input ('masukkan tinggi: '))
# JENIS = jenis (a,t)
# print (f'ini adalah bangun datar {JENIS}')


def jenis (alas, tinggi):
    luas = 1/2 * a * t
    return luas

a = int (input ('masukkan alas: '))
t = int (input ('masukkan tinggi: '))
hasil = jenis (a, t)
print (hasil)

