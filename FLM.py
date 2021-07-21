import numpy as np
n=9
b=[1]*n
An = np.random.randint(10,20,size=(n,n))
A = np.dot(An,An.T)
def f(A, b):
    x = np.zeros(len(b))
    k = 0
    while np.sum((np.dot(A, x) - b) ** 2)>10**-6:
        res = b - np.dot(A, x)
        x = x + res * np.sum(res**2)/(np.sum(res*np.dot(A, res)))
        k+=1
    return x, k
re=f(A,b)
x1=np.linalg.solve(A,b)
print(A,'\n\nСпуск:',re[0],'\nИтерации:',re[1],'\nВстроенные средства:',x1, "\n\nРазница: ",re[0]-x1)