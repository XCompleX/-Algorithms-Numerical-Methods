import math
from sympy import *
func = 0
q = 0
e = 0

def countN(a,b,e):
    iterat = math.ceil(math.log2((b-a)*1/e)-1)
    print(f'(b-a)*1/e={(b-a)}*{1/e}')
    print(f"n = log2({(b-a)*1/e})-1")
    print(f"count iter = {iterat+1}")
    return iterat

def xn(a,b,n):
    x = (a+b)/2
    print(f"X{n}=({a+b})/2="+str(x))
    fa = f(a)
    fb = f(b)
    fx = f(x)
    print(f'f(a)={str(func).replace("x",str(a))}={fa}')
    print(f'f(b)={str(func).replace("x",str(b))}={fb}')
    print(f'f(x)={str(func).replace("x",str(x))}={fx}')
    if fx > 0 and fa > 0 and fx < fa:
        a = x
    elif fx < 0 and fa < 0 and fx > fa:
        a = x
    elif fx < 0 and fb < 0 and fx > fb:
        b = x
    elif fx > 0 and fb > 0 and fx < fb:
        b = x
    print()
    print(f"[a,b]=[{a};{b}]")
    return x, a, b

def f(x):
    return func.subs(q,x)
    
def poldel(fu,qq,ee):
    global e,q,func
    e = ee
    q = qq
    func = fu
    plot(func,(q,-10,10),line_color='red')
    a = float(input("Введите a: "))
    b = float(input("Введите b: "))
    n = countN(a,b,e)
    print(f"[a,b]=[{a};{b}]")
    xn_1 = 0
    for i in range(n+1):
        xn_1,a,b = xn(a,b,i)
    print(f'Ответ: {xn_1}')
