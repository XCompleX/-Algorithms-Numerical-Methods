import sympy
from sympy import *

def createPolinom(a):
    funcT = f"L{len(a[0])-1}(X)="
    func = ""
    for i in range(len(a[0])):
        func += f"{a[1][i]}*"
        func2 = ""
        func3 = ""
        for j in range(len(a[0])):
            if(j != i):
                func2 +=f"(x-{a[0][j]})*"
            if(j != i):
                func3 +=f"({a[0][i]}-{a[0][j]})*"
        func2 = func2.rstrip(func2[-1])
        func3 = func3.rstrip(func3[-1])
        func+=f"({func2})/({func3})+"
    func = func.rstrip(func[-1])
    print(funcT+func+"=")
    return func

def lagrange(a,x):
    func = createPolinom(a)
    c = parse_expr(func, evaluate=True)
    print(str(c)+"=")
    c = expand(c)
    print(c)
    plot(c,(Symbol('x'),-10,10), line_color='red')
    print(c.subs(Symbol('x'),x))
