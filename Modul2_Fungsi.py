import numpy as np

matrix = [[2,1,-2,3],[1,-1,-1,0],[1,1,3,12]]
matrix_np = np.mat(matrix)
row,col = matrix_np.shape
solution=[None for i in range(row)]
determinant = None

def eliminate(matrix):
    for k in range(row-1):
        if abs(matrix[k][k])<10**-15:
            print("NotValidValue",(k,k))
            raise Exception("Proses Gagal")
        for i in range(k+1,row):
            p = matrix[i][k]/matrix[k][k]
            for j in range(k+1,col):
                matrix[i][j]= matrix[i][j] -p*matrix[k][j]
            matrix[i][k]=0
    
    matrix_np = np.mat(matrix)
    return matrix_np


def eliminate_pivot(matrix):
    for k in range(row-1):#Iterate from first row to the second last row
        #Begin pivoting
        m=k
        for i in range(k+1,row):#Iterate from next kth row to the last row
            
            if abs(matrix[i][k]) > abs(matrix[m][k]):
                m=i

        if m != k:
            for j in range(k,col):#Iterate from kth collumn to the last collumn
                s=matrix[k][j]
                matrix[k][j]= matrix[m][j]
                matrix[m][j] = s
            
        if abs(matrix[k][k]) < 10**-15:
            print("NotValidValue",(k,k))
            raise Exception("Proses Gagal")
            
        #Gauss Elimination    
        for i in range(k+1,row):#Iterate from first row to the second last row
            
            p=matrix[i][k]/matrix[k][k]
            
            for j in range(k+1,col):#Iterate from next to kth collumn to the last collumn
                matrix[i][j]= matrix[i][j] - p*matrix[k][j]
            matrix[i][k]=0    
    matrix_np = np.mat(matrix)
    return matrix_np


def backwards(matrix):
    dim = row -1 # n kalau di buku
    if abs(matrix[dim][dim]) < 10**-15:
        print("NotValidValue",(dim,dim))
        raise Exception("Proses Gagal")
    
    solution[dim] = matrix[dim][dim+1]/matrix[dim][dim]
    
    for k in range(dim-1,-1,-1):
        s=0
        for i in range(k+1,dim):
            s += matrix[k][i]*solution[i]
        
        solution[k]=matrix[k][dim+1]/matrix[k][k]
    
    if None in solution:
        raise Exception("Tidak ada Solusi")
    return solution


def solve(matrix,pivot=False):
    if pivot:
        eliminate_pivot(matrix)
    else:
        eliminate(matrix)
    return backwards(matrix)

print(solve(matrix))

for i in range(len(solution)):
    print(f"x{i}=",solution[i])
