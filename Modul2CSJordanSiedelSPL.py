import numpy as np

matrix = [[8,3,-2,1], 
          [4,12,4,3], 
          [2,-2,9,3],
          [1,2,4,8]]
constants = [2,-7,10,-5]
matrix_np = np.mat(matrix)
n = len(matrix)
x = [2,2,6,3] 
determinant = None


def jacobi(matrix=matrix,constants=constants, n=n, max_iter=5,eps=10**-6):
    iter=0
    while True: 
        error=0
        x_new= x.copy()
        for i in range(n):
            s=0
            for j in range(n):
                if j!=i :
                    s += matrix[i][j]*x[i]
            x_new[i]= (constants[i]-s)/matrix[i][i]
            s = abs((x_new[i]-x[i])/x_new[i])
            if s> error :
                error =s 
        for i in range(n):
            x[i]=x_new[i]
        if error < eps:
            return x
        iter =iter+1
        for i in range(n):
            print(f"x{i} iter ke-{iter}: {x[i]}")
        if iter> max_iter:
            break
    return x


def siedel(matrix=matrix,constants=constants, n=n, max_iter=4,eps=10**-6):
    iter=0
    while True: 
        error=0
        x_new= x.copy()
        for i in range(n):
            s=0
            for j in range(n):
                if j!=i :
                    s += matrix[i][j]*x[i]
            x_new[i]= (constants[i]-s)/matrix[i][i]
            s = abs((x_new[i]-x[i])/x_new[i])
            if s> error :
                error =s 
            x[i]=x_new[i]
        if error < eps:
            return x
        iter =iter+1
        for i in range(n):
            print(f"x{i} iter ke-{iter}: {x[i]}")
        if iter> max_iter:
            break
    return x

jacobi()
siedel()