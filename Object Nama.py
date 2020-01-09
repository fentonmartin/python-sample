#template dari objek = class
#objek terdiri dari : atribut, behavior

class orang:
    total=0
    def __init__(self,nama):
        self.nama=nama
        orang.total+=1
    def __del__(self):
        orang.total-=1
    def sayhello(self):
        print 'Hello, my name %s, how are you?' %self.nama
    def totalpopulasi(cls):
        print 'Total populasi : %s' %cls.total
    totalpopulasi=classmethod(totalpopulasi)
    
# org=orang('FEN')
# org.nama()
# org.sayhello()
# org.total()
# org.totalpopulasi()

