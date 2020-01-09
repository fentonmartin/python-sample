x=raw_input('Karakter yang akan dipakai :')
y=int(raw_input('Jumlah baris yang diinginkan :'))

n=y/2
m=y/2
a=1
b=1
while a<=(y/2):
    print ' '*n + x*((2*a)-1)
    a=a+1
    n=n-1
while b<=y:
    print ' '*b + x*((m*2)-1)
    b=b+1
    m=m-1


'''
n=m
y=1
z=2

while y<=m:
    print ' '*n + x*((2*y)-1)
    y+=1
    n-1

for i in range(m):
    if i<=(m/2):
        print ' '*((m/2)-(i-1)) + x*i + x*(i-1)
    else :
        print ' '*(1*z) + ' '*(m-1) + x*(m-(i+1))
        z=z+1
'''
