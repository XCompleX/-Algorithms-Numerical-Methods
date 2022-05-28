from fractions import Fraction

def checkMatrix(a):
    for i in a:
       if len(i) != len(a):
           return False
    return True

def izmStrok(a):
    if(a[0][0] == 0):
        for i in range(1,len(a)):
            if(a[i][0] != 0):
                a[0], a[i] = a[i], a[0]
    else:
        return

    for i in a:
        print(i)
    print()
    print(b)
    print()
           
    
def gaussT(a,b):
    if checkMatrix(a):        
        for i in a:
            print(i)
        print()
        print(b)
        print()

        izmStrok(a)

        countX = 0
        
        for k in range(1, len(a)):
            error=0
            for i in range(k, len(a)):
                if a[i][k-1] == 0:
                    error+=1
            if error >= len(a)-k:
                countX -= 1
                continue
            
            l = []
            for j in range(1, len(a)):
                l.append(Fraction(a[j][k-1])/Fraction(a[k-1][k-1]))
            for i in range(len(a[0])):
                for j in range(k, len(a)):
                    a[j][i] = Fraction(a[j][i]) - Fraction(a[k-1][i])*l[j-1]
            for j in range(k, len(a)):
                b[j] = Fraction(b[j]) - Fraction(b[k-1])*l[j-1]

            for i in a:
                l = []
                for j in i:
                    l.append(str(j))
                print(l)
            print()

            l = []
            for i in b:
                l.append(str(i))
            print(l)
            print()
        
        x = []
        for i in range(len(a)-1,-1-countX,-1):
            z = []
            for k in range(i,len(a)-1):
                z.append(Fraction(a[i][k+1]))
            for k in range(len(x)-1,-1,-1):
                z[abs(k-len(x)+1)] *= Fraction(x[k])
            x.append((Fraction(b[i])-sum(z))/Fraction(a[i][i]))
            
        for i in range(len(x)-1,-1,-1):
            print(f"x{abs(i-len(a))}={x[i]}")
            
    else:
        print("NOT GOOD")
        
def gaussNT(a,b):
    if checkMatrix(a):        
        for i in a:
            print(i)
        print()
        print(b)
        print()

        izmStrok(a)

        countX = 0
        
        for k in range(1, len(a)):
            error=0
            for i in range(k, len(a)):
                if a[i][k-1] == 0:
                    error+=1
            if error >= len(a)-k:
                countX -= 1
                continue
            
            l = []
            for j in range(1, len(a)):
                l.append(a[j][k-1]/a[k-1][k-1])
            for i in range(len(a[0])):
                for j in range(k, len(a)):
                    a[j][i] = a[j][i] - a[k-1][i]*l[j-1]
            for j in range(k, len(a)):
                b[j] = b[j] - b[k-1]*l[j-1]

            for i in a:
                print(i)
            print()
            
            for i in b:
                print(i)
            print()
        
        x = []
        for i in range(len(a)-1,-1-countX,-1):
            z = []
            for k in range(i,len(a)-1):
                z.append(a[i][k+1])
            for k in range(len(x)-1,-1,-1):
                z[abs(k-len(x)+1)] *= x[k]
            x.append((b[i]-sum(z))/a[i][i])
            
        for i in range(len(x)-1,-1,-1):
            print(f"x{abs(i-len(a))}={x[i]}")
            
    else:
        print("NOT GOOD")


