from random import randint

n = 34
experiments = 100000
success = 0
x = []
for i in range(1, n+1):
    x.append(i)
#print(x)
for r in range(experiments):
    for k in range(33, 28, -1):
        #print(k)
        j = randint(0, 33)
        temp = x[k]
        x[k] = x[j]
        x[j] = temp
    commission = x[:6]
    #print(commission)
    poffessors = 0
    PhD = 0
    teachers = 0
    assistents = 0
    for i in commission:
        if i > 0 and i < 7:
            poffessors += 1
        if i > 6 and i < 13:
            PhD += 1
        if i > 12 and i < 23:
            teachers += 1
        if i > 22 and i < 35:
            assistents += 1
    if poffessors > 0 and PhD > 0 and teachers > 0 and assistents > 0:
        success += 1
answer = success/experiments
print(answer)
