
try:
    print 'Zero Division Error (Masukan Y=0 ERROR)'
    x=input('Masukan Nilai X =')
    y=input('Masukan Nilai Y =')
    z=x/y
    print 'Hasil Pembagian =',z
except ZeroDivisionError,a:
    print 'Zero Division Error (WORKED)',a


try:
    print 'IO Error'
    f=open('d:/My Documents/zNote/#.txt')
    baris=f.read()
    print baris,
except IOError,b:
    print 'IO Error',b

import time
try :
    print 'Keyboard Interrupt'
    f=open('d:/My Documents/zNote/#.txt')
    while True:
        baris=f.readline()
        if len(baris)==0:
            break
        print baris,
        time.sleep(2)
except KeyboardInterrupt,c:
        print 'KeyboardInterrupt karena',c

      
print 'Index Error'
x=[4,5,6,7,8]
print 'Nilai X =',x[5]
