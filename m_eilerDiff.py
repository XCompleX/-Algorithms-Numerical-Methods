import sympy
from sympy import *
import matplotlib.pyplot as plt
y = Symbol('y')
t = Symbol('t')

def eiler(f):
    x_ = []
    y_ = []
    a = int(input("Введите a:"))
    b = int(input("Введите b:"))
    y0 = int(input("Введите y0:"))
    n = int(input("Введите n:"))
    h = (b-a)/n
    print('i     ','t     ','y')
    for i in range(n+1):
        print(f'{i}     {h*i}     {y0}')
        x_.append(h*i)
        func = f.subs(y,y0).subs(t,h*i)
        y0 = y0 + h * func
        y_.append(y0)
        i += 1
    plt.plot(x_,y_)
    plt.show()
