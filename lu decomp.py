import numpy as np

def findmaxcol(A,row):
    m, n = A.shape
    max = abs(A[row][row])
    index = 0
    for j in range(row,m):
        if abs(A[j][row])>max:
            max = abs(A[j][row])
            index = j
    return index




def ludecomp(arrayA,arrayB):
    m,n = arrayA.shape#διασταση πινακα Α
    P = np.identity(m,dtype = int)
    L = np.identity(m,dtype = float)
    for j in range(m-1):
        index = findmaxcol(arrayA,j)
        arrayA[[j,index]] = arrayA[[index,j]]
        P[[j,index]] = P[[index,j]]#τωρα εχω μαξ στοιχειο στη 1η γραμμη
        if j!=0 and j!=index:
            i = 0
            while i<j:
                temp = L[j][i]
                L[j][i] = L[index][i]
                L[index][i] = temp
                i+=1
        for i in range(j+1,m):
            toL = arrayA[i][j]/arrayA[j][j]
            arrayA[i,:] += -toL*arrayA[j,:]
            L[i][j] = toL
    U = arrayA
    Temp = P.dot(arrayB)
    C = np.zeros((m,1))
    C[0] = Temp[0]
    for j in range(1,m):
        for i in range (j):
            C[j]+= -L[j][i]*C[i]
        C[j]+= Temp[j]
    X = np.zeros((m,1))
    X[m-1] = C[m-1]/U[m-1][m-1]
    for j in range (m-2,-1,-1):
        for i in range (m-1,j,-1):
            X[j]+= -(U[j][i]/U[j][j])*X[i]
        X[j] += C[j]/U[j][j]
    return X


x = np.array([[2,1,5],[4,4.0,-4], [1,3,1.0]])
b = np.array([5,0,6])
b = b.reshape(3,1)
D = ludecomp(x,b)#παραδειγμα εκτέλεσης με δεδομένα απο άσκηση
print(D)
