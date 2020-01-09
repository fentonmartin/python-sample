a=0
b=1
c=3
tot=0
n=input('Masukan jumlah suku :')

print ''    
print 'SUKU TAMBAH'
print ''   


for i in range(n):
    tot=tot+a
    if i<(n-1) :
        print a, '+',
    else :
        print a, '=', tot
    a=a+c
    c=c+2

print ''
print ''
print 'SUKU (-2)'

for x in range(n):
    b=b*(-2)
    print b,

#print '0 + 3 + 8 + 15 + 24 + 35 + 48 = 133'
#suku[i]=(i*a)+a
    
print ''
