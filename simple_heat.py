## Aula de CFD
## Exemplo de Transferëncia de calor 1D
## 29/08/2018

# Bibliotecas
import numpy as np
import matplotlib.pyplot as plt

# Dados de entrada
q = 800.0  # [W] Fluxo de calor na esquerda
h = 140.0  # [W/m2K] Coef. na face direita
Ta = 25+273.15 # [K] Temperatura (direita)

k = [480.0, 120.0, 313.0] # [W/mK]
L = [0.02, 0.01, 0.1]   # [m]

N = len(k) + 1 # Numero de elementos plus one

A = np.matrix(np.zeros((N,N)))

for i in range(N-1):
    C = k[i]/L[i]
    A[i:i+2:,i:i+2:] = A[i:i+2:,i:i+2:] + C

# Multiplicar por -1
for i in range(N-1):
    A[i,i+1] *= -1
    A[i+1,i] *= -1

# Subtraindo h
A[N-1,N-1] -= h

# Source vector
B = np.zeros(N)
B[0] = q
B[N-1] = -h*Ta

# Resolvendo
T = np.linalg.solve(A,B)

fig, ax = plt.subplots()
plt.plot([0,L[0],L[0]+L[1],L[0]+L[1]+L[2]], T, 'b', lw=1)
plt.xlabel('$x[m]$')
plt.ylabel('$T[K]$')
plt.show()

print(x)
