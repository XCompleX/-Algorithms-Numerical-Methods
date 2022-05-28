import m_jacobi

e = 10**(-6)

a = [[3,1,1],
     [3,5,1],
     [1,5,9]]
     
b = [4,7,5]

m_jacobi.jacobi(a,b,e)
