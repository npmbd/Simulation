import random
experiments = 10

N = 19
x = 19
y = 1
z = 0

n = x*y+y*(y-1)/2 + (N + 1 - x - y)*y
p1 = x*y/n
#print(p1)

p2 = y*(y-1)/(2*n)
#print(p2)

p3 = (N + 1 - x - y)*y/n
#print(p3)
while x != 0 or y != 0:
    random_num = random.random
    if  < p1:
        x -= 1
        y += 1
    elif


