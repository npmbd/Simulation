import random
import numpy as np

N = 10000
p = 0.05
n = 1000
lambda1 = 1/80000
success = 0
for i in range(N):
    total = 0
    for j in range(n):
        if random.random() < p:
            claim = 1
        else:
            claim = 0
        total = total + claim * (-(1/lambda1) * np.log(1 - random.random()))
    if total < 5000000:
        success += 1

print(success/N)