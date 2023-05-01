from random import randint
n = 10
x = []
for i in range(1, n+1):
    x.append(i)
# print(enumerate(random_numbers))

# for i in range(n):
#     rand_num = randint(1, 10)
print(x, len(x))
for k in range(9, 2, -1):
    #print(k)
    j = randint(0, 9)
    temp = x[k]
    x[k] = x[j]
    x[j] = temp

print(x)

#print(range(9, 1, -1))

