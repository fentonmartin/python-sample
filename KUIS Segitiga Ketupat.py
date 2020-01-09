n=int(input('Masukan jumlah baris :'))
a=1
b=1
x=n/2
y=n/2
z=n/2

print ''

while a<=z :
    print ' - '*x + ' # '*((a*2)-1) + ' - '*x 
    x=x-1
    a=a+1

print ' # '*((z*2)+1)

while b<=z:
    print ' - '*b + ' # '*((y*2)-1) + ' - '*b 
    b=b+1
    y=y-1


print ''

a=1
b=1
x=n/2
y=n/2
z=n/2

while a<=z :
    print ' # '*x + '   '*((a*2)-1) + ' # '*x
    x=x-1
    a=a+1

print '   '*((z*2)+1)

while b<=z :
    print ' # '*b + '   '*((y*2)-1) + ' # '*b
    b=b+1
    y=y-1

print ''
print ' '*(n*3/2-2) + '- FEN -'
print '[040615]'













