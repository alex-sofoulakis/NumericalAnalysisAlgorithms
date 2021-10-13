import math as m


def f(x):
    y = m.exp(m.sin(x) ** 3) + x**6 - 2*x**4 - x**3 - 1
    return y

'''def f(x):
    y = 54*x**6 + 45*x**5 - 102*x**4 - 69*x**3 + 35*x**2 + 16*x - 4
    return y'''



def dixotomisi(a,b):
    con = True
    count = 0
    while con:
        count += 1
        mes = (a + b) / 2
        if f(mes) == 0:
            return mes,count
        elif f(mes) * f(a) < 0:
            b = mes
        else:
            a = mes
        con = (b - a) >= 10 ** -5
    return mes,count


x0,count0 = dixotomisi(-2,2)
print(x0,count0)
x1,count1 = dixotomisi(-2,-0.1)
print(x1,count1)
x2,count2 = dixotomisi(0.1,2)
print(x2,count2)
'''x0,count0 = dixotomisi(-2,-1.1)
x1,count1 = dixotomisi(0,0.5)
x2,count2 = dixotomisi(0.25,0.7)
x3,count3 = dixotomisi(1,2)
print(x0,count0)
print(x1,count1)
print(x2,count2)
print(x3,count3)'''















