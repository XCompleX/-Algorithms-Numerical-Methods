import sympy
from sympy import *
import m_eilerDiff

y = Symbol('y')
t = Symbol('t')
f = y-2*t/y
m_eilerDiff.eiler(f)