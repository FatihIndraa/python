# cara 1 (while statis)
x = 1
y = 5
z = x

while (x<y):
    i = 1
    print (' ')
    while (i <= x):
        print (x, end = " ")
        i+=1
    x += 1
while (z<=y):
    print (' ')
    i = 1
    while (i <= y):
        print (y, end = " ")
        i+=1
    y-=1
print (' ')   
# cara 2 (while dinamis)
x = int(input('masukkan angka pertama: '))
y = int (input('masukkan angka tertinggi: '))
z = x

while (x<y):
    i = 1
    print (' ')
    while (i <= x):
        print (x, end = " ")
        i+=1
    x += 1
while (z<=y):
    print (' ')
    i = 1
    while (i <= y):
        print (y, end = " ")
        i+=1
    y-=1    
    
# cara 3 (for statis)
