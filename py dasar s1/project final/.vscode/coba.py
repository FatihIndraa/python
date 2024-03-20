c = 'A'
# a = ['aaa','bbb', 'ccc']
# b = [1,2,3]
# x=0

# if (a):
#     x = 0
#     while (x < len (a)):
#         print (f'\t {x+1} | produk: {a[x]} \t |\t harga: {b [x]} |')
#         x += 1

# pilih = int (input ('pilih: ')) 
# if (pilih == pilih-1):
#     print (f'seri: {a[pilih-1]}')

# # print (f'seri: {a[p-1]}')
# a = int (input ('masuk: '))-1
# print (a)
# list = [[1,2,3],[2,2,2],[3,3,3]]
# while True:
#     pilihan = int(input('1. tambah\n2. ganti\n3. hapus\npilih: '))
#     if (pilihan == 1):
#         a = input("masuk a: ")
#         b = input ("masuk b: ")
#         c = input ('masuk c: ')
#         data = [a,b,c]
#         list.append (data)
#         print (list)
        
#     elif (pilihan ==2):
#         ganti = int(input('data mana yg mnau diganti: '))-1
#         a1 = input ("masuk a: ")
#         b1 = input ("masuk b: ")
#         c1 = input ('masuk c: ')
#         gantiData = [a1,b1,c1]
#         list [ganti] = gantiData
#         print (list)
#     elif (pilihan ==3):
#         hapus = int (input ('hapus mana: '))-1
#         del list [hapus]
#         print (list)
# list1 = list [0]
# print (list1[2]) 
# if (list):
#     for a in (list):
#         print (f'{a[0]} \n {a[1]} \n {a[2]}')
# pilihan = int (input('pilih mana: '))




# list = [[1,2,3],[2,2,2],[3,3,3]]

# pembelian = []
# total = 0
# while (c == 'A'):
    
#     pilih = int (input ('masuk: '))
#     pilih1 = list [pilih - 1] #data yang dipilih
#     pilih2 = pilih1 [2] #harga yagn dipilih
#     pembelian.append (pilih1)
#     total += pilih2

#     print (pembelian)
#     tambahan = int (input ('1 ya  2. tidak: '))

#     if (tambahan == 2):
#         print (total)

a = [[1,1,1], [2,2,2], [3,3,3]]
b = [[4,4,4], [5,5,5], [6,6,6]]
c = [[7,7,7], [8,8,8], [9,9,9]]
ab = []
while True:
    pilihan = input ('pilih a/b/c')
    if ( pilihan == 'a'):
        aaa = int (input ('masuk: '))
        t = a[aaa-1]
        ab.append (t)
    elif (pilihan == 'b'):
        aaa = int (input ('masuk: '))
        t = b[aaa-1]
        ab.append (t)
    elif (pilihan == 'c'):
        aaa = int (input ('masuk: '))
        t = c[aaa-1]
        ab.append (t)
  
    lanjut = input ('y/n  ')
    
    if (lanjut == 'n'):
        c = 'c'
        for q in (ab):
            print (f'pertama {q[0]}\tkedua: {q[1]},\t ketiga: {q[2]}')