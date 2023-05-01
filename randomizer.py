import numpy
import numpy as np
num = 0
m = 2**31 - 1
a = 7**5
N = 100
x = np.array([1])
u = np.array([])
#print(x)
for i in range(1, N):
    x = np.append(x, a*x[i-1]%m)
    u = np.append(u, x[i]/m)

for i in range(1, N):
    num = num + np.exp**(np.exp**(u[i]))
print(num/N)
# print(next_element(x, m, a))
