try:
    f=open('d:/#/coba.txt','r')
    print 'File yang akan dibaca :', f.name
    print 'Modus file            :', f.mode
    print 'Apakah file sudah ditutup :', f.closed
    print ''
    print 'Isi file \n', f.read()
    print 'Posisi pointer pada file  :', f.tell()
    f.close()
    print 'Apakah file sudah ditutup :', f.closed
except IOError, e:
    print 'Gagal memproses karena ',e
