import sympy
from sympy import *
q = sympy.symbols('x')
    
def left(f):
    a,b,n = integ(f)
    z = 0
    h = (b-a)/n
    x0 = a
    print("LEFT:")
    for i in range(n):
        z1 = f.subs(q,x0).evalf()
        print(f"x={x0} {f}={z1}")
        z += z1
        x0+=h
    return h*z

def right(f):
    a,b,n = integ(f)
    z = 0
    h = (b-a)/n
    x0 = a+h
    for i in range(1,n+1):
        z1 = f.subs(q,x0).evalf()
        print(f"x={x0} {f}={z1}")
        z += z1
        x0+=h
    return h*z

def center(f):
    a,b,n = integ(f)
    z = 0
    h = (b-a)/n
    x0 = a
    for i in range(n):
        z1 = f.subs(q,(x0+x0+h)/2).evalf()
        print(f"x={x0} {f}={z1}")
        z += z1
        x0+=h
    return h*z

def integ(f):
    print(f)
    p1 = plot(f,line_color='blue',show=False)
    p1.show()
    a = float(input("Введите a: "))
    b = float(input("Введите b: "))
    n = int(input("Введите n: "))
    return a,b,n