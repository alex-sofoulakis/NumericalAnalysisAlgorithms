import numpy as np
import math


def table():
    len = math.pi*0.5/10
    x = np.array([0, len, 2*len, 3*len, 4*len, 5*len, 6*len, 7*len, 8*len, 9*len, math.pi*0.5])
    y = np.array([0,math.sin(len), math.sin(2*len), math.sin(3*len), math.sin(4*len), math.sin(5*len), math.sin(6*len), math.sin(7*len), math.sin(8*len), math.sin(9*len), 1])
    s1 = sum(y[i] for i in range(1, 10))
    error = (math.pi*0.5)**3/(12*10**3)
    return (y[0] + y[10] + 2*s1)*len/2, error


print(table())