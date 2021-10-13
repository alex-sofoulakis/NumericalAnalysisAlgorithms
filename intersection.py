import math as m

def f(x):
    y = m.exp(m.sin(x) ** 3) + x**6 - 2*x**4 - x**3 - 1
    return y

def fder(x):
    y = 3*m.exp(m.sin(x) ** 3)*m.cos(x)*m.sin(x)**2 + 6*x**5 -8*x**3-3*x**2
    return y
'''
def f(x):
    y = 54*x**6 + 45*x**5 - 102*x**4 - 69*x**3 + 35*x**2 + 16*x - 4
    return y
def fder(x):
    y = 54*6*x**5 + 45*5*x**4 - 102*4*x**3 - 69*3*x**2 + 35*2*x + 16
    return y'''


def temnousa(a,b):
    xn_1 = a
    xn = b
    temp = f(xn)*(xn - xn_1)
    temp2 = f(xn)-f(xn_1)
    count = 1
    xn1 = xn - temp/temp2
    while abs(xn1-xn)>= 0.5*10**-5:
        xn_1 = xn
        xn = xn1
        temp = f(xn) * (xn - xn_1)
        temp2 = f(xn) - f(xn_1)
        xn1 = xn - temp/temp2
        count += 1
    return xn1,count


x1,count1 = temnousa(-2,-1.05)
print(x1,count1)
x2,count2  =temnousa (-0.5,0.5)
print(x2,count2)
x3,count3 = temnousa(1.3,2)
print(x3,count3)

'''x1,count1 = temnousa(-2,-1.5)
print(x1,count1)
x2,count2  =temnousa (-1.3,-0.7)
print(x2,count2)
x3,count3 = temnousa(-0.5,0.4)
print(x3,count3)
x4,count4 = temnousa(0.4,1.8)
print(x4,count4)
x5,count5 = temnousa(1.3,2)
print(x5,count5)'''