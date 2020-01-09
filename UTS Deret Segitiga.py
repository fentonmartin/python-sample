n=input('Masukkan jumlah baris :')
b=1
m=n

while b<=m :
    a=0
    for i in range(b):
        a=a+2
        if i==(b-1) :
            print a
        else :
            print a , ',',
    b=b+1

while b>=1 :
    a=0
    for j in range(b) :
        a=a+2
        if j==(b-1) :
            print a
        else :
            print a, ',',
    b=b-1    
    
