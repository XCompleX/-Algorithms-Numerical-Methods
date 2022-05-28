import math
import copy
 
def checkMatrix(a):
    check1 = abs(a[0][0]) > abs(a[0][1]) + abs(a[0][2])
    check2 = abs(a[1][1]) > abs(a[1][0]) + abs(a[1][2])
    check3 = abs(a[2][2]) > abs(a[2][0]) + abs(a[2][1])
    return check1 and check2 and check3

def x0(a,b):
    x01 = b[0]/a[0][0]
    x02 = b[1]/a[1][1]
    x03 = b[2]/a[2][2]
    return x01,x02,x03

def zeindel(a,b,e):
    if checkMatrix(a):
        xn_11,xn_12,xn_13 = x0(a,b)
        k=0
        d1 = d2 = d3 = e*10
        while(d1 > e and d2 > e and d3 > e):
            x1 = (b[0]-a[0][1]*xn_12-a[0][2]*xn_13)/a[0][0]
            x2 = (b[1]-a[1][0]*x1-a[1][2]*xn_13)/a[1][1]
            x3 = (b[2]-a[2][0]*x1-a[2][1]*x2)/a[2][2]
            d1 = abs(x1-xn_11)/abs(x1)
            d2 = abs(x2-xn_12)/abs(x2)
            d3 = abs(x3-xn_13)/abs(x3)
            xn_11 = x1
            xn_12 = x2
            xn_13 = x3
            print(k,x1,x2,x3,d1,d2,d3)
            k+=1
        print(f'\n x1={x1},x2={x2},x3={x3}')
    else:
        print("NOT GOOD")
