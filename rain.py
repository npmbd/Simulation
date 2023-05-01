import random
import matplotlib.pyplot as plt

n = 100000
p = 0.2
s = 0
for i in range(n):
    x = 1
    y = 1
    location = -1
    wet = 0
    trips = 0
    while wet < 1:
        if random.random() > p:
            location = location*(-1)
            trips = trips +1
        else:
            if location == -1:
                if x == 0:
                    wet = 1
                else:
                    x -= 1
                    trips += 1
                    y += 1
                    location = location*(-1)
            else:
                if y == 0:
                    wet = 1
                else:
                    trips += 1
                    y = y + 1
                    location = location*(-1)
    s = s + trips
answer = s/n
print(answer)





