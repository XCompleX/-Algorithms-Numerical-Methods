import sympy
from sympy import *
import m_range_kutt

y = Symbol('y')
t = Symbol('t')
f = 2*t*y
m_range_kutt.rk(f)
