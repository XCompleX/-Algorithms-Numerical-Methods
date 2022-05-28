import sympy
from sympy import *
import m_poldel

q = Symbol('x')
func = 5*q**2+2*q-5
e = 10**(-6)

m_poldel.poldel(func,q,e)
