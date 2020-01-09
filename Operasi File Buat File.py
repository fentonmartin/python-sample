try:
    f=open('d:/#/coba.txt','w')
    print 'File yang akan dibuat :', f.name
    print 'Modus file            :', f.mode
    print 'Apakah file sudah ditutup :', f.closed
    f.close()
    print 'Apakah file sudah ditutup :', f.closed
except IOError, e:
    print 'Gagal memproses karena ',e
