import sympy
from sympy import *
import matplotlib.pyplot as plt
y = Symbol('y')
t = Symbol('t')

def eiler(f):
    x_ = []
    y_ = []
    y_1 = []
    a = int(input("Введите a:"))
    b = int(input("Введите b:"))
    y1 = y0 = int(input("Введите y0:"))
    n = int(input("Введите n:"))
    h = (b-a)/n
    print('i     hi       y0       y1')
    for i in range(0,n+1):
        print(f'{i}     {h*i}      {y1}     {y0}')
        x_.append(h*i)
        func = f.subs(y,y0).subs(t,h*i)
        y1 = y0 + h * func
        y_.append(y1)
        func1 = f.subs(y,y1).subs(t,h*i*2)
        y0 = y0 + h * (func+func1)/2
        y_1.append(y0)
        i += 1
    plt.plot(x_,y_)
    plt.show()
    plt.plot(x_,y_1)
    plt.show()
