#soma de matrizes
print('Soma de matrizes')
import numpy as np
A = np.array([[1, -2, 3],
              [0, 4, 5]])
B = np.array([[6, 7, -1],
              [2, 3, 0]])
C = A + B
print(C)
print('----------------')
#multiplicação de matriz por um escalar (n° real)
print('Multiplicação de matriz por escalar')
A = np.array([[1, -2, 3],
              [0, 4, 5]])
k = 3
B = A + k
print(B)
print('----------------')
#Multiplicação de matrizes
print('Multiplicação de matrizes')
A = np.array([[1, -2, 3],
              [0, 4, 5]])
B = np.array([[6, 7, -1],
              [2, 3, 0],
              [5, 6, 7]])
C = np.dot(A, B)
print(C)

