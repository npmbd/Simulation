import numpy as np
import random

N = 14
rand_numbers = []
for i in range(N):
    if i == 0:
        rand_numbers.append(np.random.random())
    rand_numbers.append(np.random.random())
    while rand_numbers[-1] < rand_numbers[-2]:
        rand_numbers[-1] = random.random()
print(rand_numbers)
product = 1
for i in rand_numbers:
    product *= i
print(product/N)