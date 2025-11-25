def roots(a,b,c):
    r1=(-b+(((b**2)-(4*a*c))**0.5))/(2*a)
    r2=(-b-(((b**2)-(4*a*c))**0.5))/(2*a)
    return r1,r2
a=int(input("enter value of a:"))
b=int(input("enter value of b:"))
c=int(input("enter value of c:"))
print(roots(a,b,c))