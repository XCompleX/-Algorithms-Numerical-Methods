import math
from sympy import *
func = 0
q = 0
e = 0

def f(x):
    return func.subs(q,x)
def f_(x):
    return diff(func).subs(q,x)

def x(x,n):
    fx=f(x)
    fx_=f_(x)
    xn=x-fx/fx_
    print(f"X{n}={x}-{fx}/{fx_}={xn}")
    print(f"X{n}-X{n-1}={xn}-{x}={xn-x}")
    return xn
    
def casat(fu, qq, ee):
    global func,q,e
    func = fu
    q = qq
    e = ee
    
    plot(func,(q,-10,10),line_color='red')
    a = float(input("Введите a: "))
    b = float(input("Введите b: "))
    xn_1 =(a+b)/2 #X0
    n = 1
    print(f'X0=({a+b})/2={xn_1}')
    print(f'f(a)={str(func).replace("x",str(a))}={f(a)}')
    print(f'f(b)={str(func).replace("x",str(b))}={f(b)}')
    print(f'f(x)={str(func).replace("x",str(xn_1))}={f(xn_1)}')
    print()
    xn = x(xn_1,n)#X1
    while(abs(xn-xn_1) > e):
        n+=1
        xn_1 = xn
        xn = x(xn,n)
    print(f'Ответ:{xn}')
