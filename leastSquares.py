import numpy as np
import math
import matplotlib.pyplot as plt


def function(anna, k):
    return anna[0] + anna[1] * k + anna[2] * (k ** 2) + anna[3]* (k**3)


def errorf(k, x):
    return np.sin(x) - k


def leastsquares(k, x, y):
    #x = np.array([-1,0,1,2])
    #y = np.array([1,0,0,-2])
    A = np.ones((10, 4))
    A[:, 1] = x
    A[:, 2] = np.power(x, 2)
    A[:, 3] = np.power(x, 3)
    d = np.dot(np.transpose(A), y)
    B = np.dot(np.transpose(A), A)
    anna = np.linalg.solve(B, d)
    err = y - np.dot(A, anna)
    return anna[0] + anna[1]*k + anna[2]*(k**2) + anna[3]*(k**3), np.linalg.norm(err), anna


ox = np.array([-2.75, -2.5,  -0.5 * math.pi, -1, (-1/6)*math.pi, 0,  math.pi*(1/3), 1, 3, math.pi])
oy = np.array([-0.382, math.sin(-2.5), -1, math.sin(-1), -1/2, 0, math.sin(math.pi*(1/3)), math.sin(1), math.sin(3), 0])

prediction, error, sint = leastsquares(0, ox, oy)
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
plt.plot(x, function(sint, x), 'm', label='Estimation')
plt.plot(x, np.sin(x), 'c', label='y  = sin(x)')
plt.plot(x, errorf(function(sint, x),x), 'b', label='Error')
plt.legend(loc='upper left')
plt.show()