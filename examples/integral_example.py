import sympy
from sympy import *
import m_integral
q = Symbol('x')

f = sin(5*q)*exp(-(q**2))
print(m_integral.center(f))
