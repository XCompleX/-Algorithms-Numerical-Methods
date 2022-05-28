import sympy
from sympy import *
import matplotlib.pyplot as plt
y = Symbol('y')
t = Symbol('t')

def rk(f):
    x_ = []
    y_ = []
    y_1 = []
    a = int(input("Введите a:"))
    b = int(input("Введите b:"))
    y1 = y0 = int(input("Введите y0:"))
    n = int(input("Введите n:"))
    h = (b-a)/n
    print('i     hi       y0')
    for i in range(0,n+1):
        print(f'{i}     {h*i}      {y0}')
        x_.append(h*i)
        k1 = f.subs(y,y0).subs(t,h*i)
        k2 = f.subs(y,y0+h/2*k1).subs(t,h*i+h/2)
        k3 = f.subs(y,y0+h/2*k2).subs(t,h*i+h/2)
        k4 = f.subs(y,y0+h*k3).subs(t,h*i+h)
        y0 = y0 + 1/6*h*(k1+2*k2+2*k3+k4)
        y_.append(y0)
        i += 1
    plt.plot(x_,y_)
    plt.show()
