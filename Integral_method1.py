import random
import numpy as np

m = 0
N = 1000

# # first method
def get_value_y(x):
    y = 1/(x**2 + 1)
    return y

# for i in range(N):
#     coordinates_m = (random.uniform(0, 2), random.uniform(0, 1))
#     if (coordinates_m[1] < get_value_y(coordinates_m[0])):
#         m += 1
# answer = 2*m/N
# print(answer)
#
# # second method

# y = np.array([])
# for i in range(N):
#     y = np.append(y, get_value_y(random.uniform(0,2)))
# sum = 0
# for i in y:
#     sum += i
# answer1 = sum*2/N
# print(answer1)

# # integral (x**2)/(np.sin(x))**3

def func_2(x):
    return (x**2)/(np.sin(x))**3

for i in range(N):
    coordinates_m = (random.uniform(0, 2), random.uniform(0, 2))
    if (coordinates_m[1] < func_2(coordinates_m[0])):
        m += 1
answer = 2*m/N
print(m)
print(answer)

y = np.array([])
for i in range(N):
    y = np.append(y, func_2(random.uniform(0, 2)))
sum = 0
for i in y:
    sum += i
answer1 = sum*2/N
print(answer1)

