import sympy
from sympy import *
import m_jacobi
import m_zeindel
import m_gauss
import m_poldel
import m_iter
import m_casat
import m_lagrange
import m_integral
import m_eilerDiff
import m_eilerModDiff
import m_range_kutt

q = Symbol('x')
func = 5*q**2+2*q-5
e = 10**(-6)

a = [[3,1,1],
     [3,5,1],
     [1,5,9]]
     
b = [4,7,5]

c = [[1,3,5,7,9],
     [5,9,7,11,13]]
'''
m_jacobi.jacobi(a,b,e)
print("-------------------")
m_zeindel.zeindel(a,b,e)
print("-------------------")
m_gauss.gaussT(a,b)
print("-------------------")
m_gauss.gaussNT(a,b)
print("-------------------")
m_poldel.poldel(func,q,e)
print("-------------------")
m_iter.miter(func,q,e)
print("-------------------")
m_casat.casat(func,q,e)
print("-------------------")
m_lagrange.lagrange(c,6)
print("-------------------")
f = sin(5*q)*exp(-(q**2))
print(m_integral.center(f))
print("-------------------")
y = Symbol('y')
t = Symbol('t')
f = y-2*t/y
m_eilerDiff.eiler(f)
print("-------------------")
y = Symbol('y')
t = Symbol('t')
f= sympy.sin(5*y+t**2)
m_eilerModDiff.eiler(f)
print("-------------------")
y = Symbol('y')
t = Symbol('t')
f = 2*t*y
m_range_kutt.rk(f)
print("-------------------")
'''

