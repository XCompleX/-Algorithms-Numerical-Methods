import math
from sympy import *
import m_casat

q = Symbol('x')
func = 5*q**2+2*q-5
e = 10**(-6)
m_casat.casat(func,q,e)
