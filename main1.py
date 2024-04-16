# Mon fichier python

import glob
x = glob.glob("*")
print(x)

def fib(n):
    x = []
    a,b=0,1
    while a <n:
        x.append(a)
        a,b= b, a+b
    return x
fib(100)
