import numpy as np
import math


def Bart():
    len = math.pi*0.5/10
    x = np.array([0, len, 2*len, 3*len, 4*len, 5*len, 6*len, 7*len, 8*len, 9*len, math.pi*0.5])
    y = np.array([0,math.sin(len), math.sin(2*len), math.sin(3*len), math.sin(4*len), math.sin(5*len), math.sin(6*len), math.sin(7*len), math.sin(8*len), math.sin(9*len), 1])

    s1 = sum(y[2*i] for i in range(1, 5))
    s2 = sum(y[2*i-1] for i in range(1, 6))
    error = (math.pi*0.5)**5/(180*10**4)
    return len/3*(y[0] + y[10] + 2*s1 + 4*s2), error


print(Bart())
