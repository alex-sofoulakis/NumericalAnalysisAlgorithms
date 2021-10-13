import math as m


def f(x):
    y = m.exp(m.sin(x) ** 3) + x**6 - 2*x**4 - x**3 - 1
    return y

def fder(x):
    y = 3*m.exp(m.sin(x) ** 3)*m.cos(x)*m.sin(x)**2 + 6*x**5 -8*x**3-3*x**2
    return y
'''def f(x):
    y = 54*x**6 + 45*x**5 - 102*x**4 - 69*x**3 + 35*x**2 + 16*x - 4
    return y
def fder(x):
    y = 54*6*x**5 + 45*5*x**4 - 102*4*x**3 - 69*3*x**2 + 35*2*x + 16
    return y'''




def newton_raphson(starting):
    xprev = starting
    count = 1
    xnext = xprev - f(xprev) / fder(xprev)
    while abs(xnext - xprev) >= 0.5 * 10 ** -5:
        xprev = xnext
        xnext = xprev - f(xprev) / fder(xprev)
        count += 1
    return xnext,count


x1,count1 = newton_raphson(-2)
print(x1,count1)
x2,count2 = newton_raphson(2)
print(x2,count2)
x3,count3 = newton_raphson(0.3)
print(x3,count3)
'''x1,count1 = newton_raphson(-2)
print(x1,count1)
x2,count2 = newton_raphson(-1)
print(x2,count2)
x3,count3 = newton_raphson(0)
print(x3,count3)
x4,count4 = newton_raphson(0.75)
print(x4,count4)
x5,count5 = newton_raphson(1)
print(x5,count5)'''
