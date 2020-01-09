print 'MENU PROGRAM'
def leas():
    P=input('Masukan Panjang= ')
    L=input('Masukan Lebar= ')
    LuasPP= P*L
    print 'Luas Persegi Panjang= ',LuasPP
    print
    print 'ingin menghitung luas lagi [y/t];'
    lagi= input().upper()
    if lagi=='y':
        menu()
    else:
        exit()
def nam():
    print 'Man'


try:
    leas(),nam()
except NameError,a:
    print 'error pada:',a
except SyntaxError,b:
    print b
