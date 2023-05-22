import random
import numpy as np

S = 1000
s = 200
x = S
y = 0
#days
lambda1 = 1/3
r = 50 # per 1 kg
for y in range (S - s+1, S+1):
    c = y*30

h = 3
L = 1.5

t = 0
tF = 10000000000
tA = -(1/lambda1) * np.log(1 - random.random())
T = 365*10000
R  = 0
H = 0
C = 0
while t < T:
    if tA < tF:
        H = H + (tA - t)*x*h
        t = tA
        G = random.randint(25, 30)
        w = min(G, x)
        R = R + w*r
        x = x - w
        if x < s and y == 0:
            y = S - x
            tF = t + L
            #tA = t + (-(1/lambda1) * np.log(1 - random.random()))
        tA = t + (-(1 / lambda1) * np.log(1 - random.random()))
    else:
        H = H + (tF - t) * x * h
        t = tF
        C = C + c
        x = x + y
        y = 0
        tF = 10000000000


print((R-H-C)/T)

