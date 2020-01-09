try:
    f=open('d:/#/coba.txt','r')
    print 'File yang akan dibaca :', f.name
    print 'Modus file            :', f.mode
    print 'Apakah file sudah ditutup :', f.closed
    print ''
    print 'Isi file \n'
    for line in f :
        print line
    print 'Posisi pointer pada file sebelumnya  :', f.tell()
    print 'Kembalikan posisi pointer ke 0,0     :', f.seek(0,0)
    print 'Posisi pointer pada file sesudahnya  :', f.tell()
    for line in f :
        print line
    print 'Posisi pointer pada file sesudahnya  :', f.tell()
    f.close()
    print 'Apakah file sudah ditutup :', f.closed
except IOError, e:
    print 'Gagal memproses karena ',e
