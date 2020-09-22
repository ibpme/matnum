import numpy as np

class NotValidMatrixError(Exception):
    print("Matrix is not valid")

class NoSolutionError(Exception):
    print("Matrix Has No solution")


class SolveSPL(object):

    def __init__(self,matrix):
        self.origin = matrix
        self.origin_np = np.mat(matrix)
        self.matrix = matrix
        self.matrix_np = np.mat(matrix)
        self.row,self.collumn = self.matrix_np.shape
        self.solution=[None for i in range(self.row)]
        self.determinant = None
        
    def set_np(self):
        self.matrix_np = np.mat(self.matrix)
    
    def eliminate(self):
        row= self.row
        col=self.collumn
        for k in range(row-1):
            if abs(self.matrix[k][k]) < 10**-15:
                print("NotValidValue",(k,k))
                raise NotValidMatrixError
            for i in range(k+1,row):
                p = self.matrix[i][k]/self.matrix[k][k]
                for j in range(k+1,col):
                    self.matrix[i][j]= self.matrix[i][j] -p*self.matrix[k][j]
                self.matrix[i][k]=0
        self.set_np()
        
        return self.matrix
    
    def eliminate_parsial(self):
        row= self.row
        col=self.collumn
        
        for k in range(row-1):#Iterate from first row to the second last row
            
            #Begin pivoting
            m=k
            for i in range(k+1,row):#Iterate from next kth row to the last row
                
                if abs(self.matrix[i][k]) > abs(self.matrix[m][k]):
                    m=i
                    
            if m != k:
                for j in range(k,col):#Iterate from kth collumn to the last collumn
                    s=self.matrix[k][j]
                    self.matrix[k][j]=self.matrix[m][j]
                    self.matrix[m][j] =s
                
            if abs(self.matrix[k][k]) < 10**-15:
                print("NotValidValue",(k,k))
                raise NotValidMatrixError
                
            #Gauss Elimination    
            for i in range(k+1,row-1):#Iterate from first row to the second last row
                
                p=self.matrix[i][k]/self.matrix[k][k]
                
                for j in range(k+1,col):#Iterate from next to kth collumn to the last collumn
                    self.matrix[i][j]= self.matrix[i][j] -p*self.matrix[k][j]
                self.matrix[i][k]=0
        
        self.set_np()
        
        return self.matrix
    
    def backwards(self):
        row= self.row
        col=self.collumn
        dim= row -1
        if abs(self.matrix[dim][dim]) < 10**-15:
            print("NotValidValue",(dim,dim))
            raise NotValidMatrixError
        
        self.solution[dim] = self.matrix[dim][dim+1]/self.matrix[dim][dim]
        
        for k in range(dim-1,-1,-1):
            s=0
            for i in range(k+1,dim):
                s += self.matrix[k][i]*self.solution[i]
            
            self.solution[k]=self.matrix[k][dim+1]/self.matrix[k][k]
        
        if None in self.solution:
            raise NoSolutionError
        
        self.set_np()
        return self.matrix
    
    def find_determinant(self,pivot=False):
        row = self.row
        if self.matrix == self.origin :
            if pivot:
                self.eliminate()
            else:
                self.eliminate_parsial()
        
        det = 1
        for i in range(row):
            det = det*self.matrix[i][i]
        
        self.determinant = det
        
        return det
        
        
    def solve(self,pivot=False):
        
        if pivot:
            self.eliminate_parsial()
        else:
            self.eliminate()
        self.backwards()
        
        return self.solution   