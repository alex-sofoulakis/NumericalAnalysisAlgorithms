import numpy as np
import math as ma

def cholesky(A):
    m,n = A.shape
    s = (m,m)
    L = np.zeros(s)
    for i in range(m):
        for j in range(i):
            L[i][j] = (A[i][j] - sum(L[i][k]*L[j][k] for k in range(j)))/L[j][j]
        L[i][i] = ma.sqrt(A[i][i] - sum(L[i][k]**2 for k in range(i)))
    print(L)
    return L


A = np.array([[1,1,3],[1,5,5],[3,5,19]])
L = cholesky(A)
print(L.dot(np.transpose(L)))
