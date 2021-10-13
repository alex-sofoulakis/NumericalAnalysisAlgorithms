from random import uniform

def f(x):
    y = 54*x**6 + 45*x**5 - 102*x**4 - 69*x**3 + 35*x**2 + 16*x - 4
    return y

def randomdix(a,b):
    count = 0
    meso = uniform(a,b)
    con = True
    while con:
        count += 1
        if f(meso) == 0:
            return meso,count
        elif f(meso)*f(a) < 0:
            b = meso
        elif f(meso)*f(b)< 0:
            a = meso
        meso = uniform(a,b)
        con = (b-a)/2 >= 0.5*10**-5
    return meso,count

x1,count1 = randomdix(-2,-1)
print(x1,count1)
x3,count3 = randomdix(0,0.5)#η 2η ριζα -0.667 δεν μπορει να βρεθει
print(x3,count3)
x4,count4 = randomdix(0.25,0.7)
print(x4,count4)
x5,count5 = randomdix(1,2)
print(x5,count5)
