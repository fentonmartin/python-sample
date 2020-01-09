n=input ('Masukan Limit Deret Fibonaci :')
fib=[0,1]
for a in range(n):
    if a>1:
        print fib[a-1]+fib[a-2],
        fib.append(fib[a-1]+fib[a-2])
    else:
        print fib[a],
