import sympy
from sympy import *
q = 0
func = 0
e = 0

def fx(x):
    f = str(func).replace('exp','e').replace('x',str(x))
    df = str(diff(func)).replace('exp','e').replace('x',str(x))
    print(f"xn = {x}-1/{df}*{f} = {x-1/fx_(x)*(func.subs(q,x))}")
    return x-1/fx_(x)*(func.subs(q,x))
def fx_(x):
    return diff(func).subs(q,x)

def iter(xn_1, i=1):
    xn = fx(xn_1)
    print(f"xn-xn_1 = |{xn}-{xn_1}| = {abs(xn-xn_1)}")
    if abs(xn-xn_1)> e:
        print(f'{i}: xn={xn}')
        iter(xn,i+1)
    else:
        print(f'Ответ: {xn}')
        return
        
def miter(fu, qq, ee):
    global func, q, e
    func = fu
    q = qq
    e = ee
    
    print(func)
    print(diff(func))
    plot(func,(q,-10,10), line_color='red')
    a = float(input("Введите a: "))
    b = float(input("Введите b: "))
    xn_1 =(a+b)/2 #X0
    print(f'X0=({a+b})/2={xn_1}')
    iter(xn_1)
