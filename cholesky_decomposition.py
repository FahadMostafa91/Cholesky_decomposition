# -*- Cholesky decomposition-*-
"""
Created on Wed Jan 26 16:10:55 2022

@author: gmostafa
"""

# cholesky decomposition 

import numpy as np
import math

A = np.array([[1.,2,3,4],[2,5,6,7],[3,6,10,1],[4,7,1,200]])

N = A.shape[0]
print(N)

for j in range(0,N):
    A[j,j] = np.sqrt(A[j,j])
    
    for i in range (j+1, N):
        A[i,j] = A[i,j]/A[j,j]
        
    for k in range (j+1,N):
        
        for i in range (0,N):
            
            A[i,k]=A[i,k]-A[i,j]*A[k,j]
        
for i in range (0,N-1):
    
    for j in range (i+1,N):
        A[i,j] = 0

print(A)
print(np.matmul(A,A.T))