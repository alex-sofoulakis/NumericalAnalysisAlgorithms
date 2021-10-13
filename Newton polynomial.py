import numpy as np
import math
import matplotlib.pyplot as plt


def function(a, k, x):
    temp = a[0]
    for i in range(1, 10):
        prod = a[i]
        for j in range(i):
            prod*= k-x[j]
        temp += prod
    return temp


def errorf(k, x):
    return np.sin(x) - k


def p(k, x, y):
    a = np.zeros(10)
    d = np.zeros(10)
    a[0] = y[0]

    for i in range(1, 10):
        for j in range(1, 10):
            d[j] = (y[j] - y[j - 1]) / (x[j] - x[j - i])
        a[i] = d[i]
        y = np.copy(d)
    temp = a[0]
    maxProd = -1
    for i in range(1, 10):
        prod = a[i]
        for j in range(i):
            prod *= k-x[j]
        temp += prod
        if abs(prod/a[i]) >= maxProd:
            maxProd = prod/a[i]
    maxError = maxProd/math.factorial(11)
    return temp, maxError, a


ox = np.array([-2.75, -2.5,  -0.5 * math.pi, -1, (-1/6)*math.pi, 0,  math.pi*(1/3), 1, 3, math.pi])
oy = np.array([-0.382, math.sin(-2.5), -1, math.sin(-1), -1/2, 0, math.sin(math.pi*(1/3)), math.sin(1), math.sin(3), 0])
prediction, error, sint = p(math.pi/2, ox, oy)
print(prediction, error)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')


x = np.linspace(-math.pi, math.pi, 200)
plt.plot(x, function(sint, x, ox), 'm', label='Estimation')
plt.plot(x, np.sin(x), 'c', label='y  = sin(x)')
plt.plot(x, errorf(function(sint, x,ox),x), 'b', label='Error')
plt.legend(loc='upper left')
plt.show()
