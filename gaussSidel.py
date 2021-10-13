import numpy as np


def getnorm(xn,xold):
    m = len(xn)
    temp = np.zeros(m)
    temp = np.transpose(temp)
    for i in range(m):
        temp[i] = abs(xn[i]-xold[i])
    return np.amax(temp)


def gaussSidel(A,B):
    m,l = A.shape
    xold = np.zeros(m)
    xn = np.zeros(m)
    count = 0
    con = True
    while con:
        for i in range(m):
            xn[i] = 1/A[i][i]*(B[i] - sum(A[i][j]*xn[j] for j in range(i)) - sum(A[i][j]*xold[j] for j in range(i+1,m)))
        y = getnorm(xn,xold)
        con = y >= 0.5*10**-4
        for i in range(m):
            xold[i] = xn[i]
        count+=1
        print(count)

    return xn

def run(n):
    A = np.zeros((n,n))
    for i in range(n):
        A[i][i] = 5
    for i in range(n-1):
        A[i+1,i] = -2
        A[i,i+1] = -2
    B = np.zeros((n,1))
    B[0] = 3
    B[n-1] = 3
    for i in range (1,n-1):
        B[i] = 1
    x = gaussSidel(A,B)
    print(x)

run(10)
run(10000)
