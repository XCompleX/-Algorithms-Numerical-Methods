import sympy
from sympy import *
import m_eilerModDiff

y = Symbol('y')
t = Symbol('t')
f= sympy.sin(5*y+t**2)
m_eilerModDiff.eiler(f)