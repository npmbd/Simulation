import random

# l = 4
# m = 7
# n = 9


def toss_coins():
    A = random.randint(0, 1)
    B = random.randint(0, 1)
    C = random.randint(0, 1)
    return A, B, C

number_of_experiments = 1000
round = 0

for i in range(number_of_experiments):
    l = 4
    m = 7
    n = 9
    while l != 0 and m != 0 and n != 0:
        tossed_coins = toss_coins()
        if tossed_coins[0] == tossed_coins[1]:
            l -= 1
            m -= 1
            n += 2
        if tossed_coins[0] == tossed_coins[2]:
            l -= 1
            n -= 1
            m += 2
        if tossed_coins[1] == tossed_coins[2]:
            m -= 1
            n -= 1
            l += 2
        round += 1

print(round/number_of_experiments)