import os
# ini untuk merubah file coba => cobalagi
try:
    os.rename('d:/#/coba.txt','d:/#/cobalagi.txt')
    print 'Nama file sudah dirubah'
except (IOError,WindowsError), e:
    print 'Gagal memproses karena',e

# ini untuk merubah file cobalagi => coba    
try:
    os.rename('d:/#/cobalagi.txt','d:/#/coba.txt')
    print 'Nama file sudah dirubah lagi'
except (IOError,WindowsError), e:
    print 'Gagal memproses karena',e
