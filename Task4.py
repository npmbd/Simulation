import numpy as np
import random

N = 1000
auspicious_events = 0

for i in range(N):
    seats = np.arange(1, 221)
    person_seat = random.sample(range(1, 221), 220) # раздаю случайные номера пассажирам, которые означают номер их места
    chosen_seats = [] # храню номер места пассажира и куда он сел на самом деле (кортеж)
    seat = random.randint(1, 220)
    seats[seat - 1] = 0
    chosen_seats.append((person_seat[0], seat))
    for i in person_seat[1:]: # начинаю со второго, т. к. первый уже занял место
        if seats[i - 1] != 0:
            chosen_seats.append((i, seats[i - 1]))
            seats[i - 1] = 0 # занятые места обозначаем 0
        else:
            seat = random.randint(1, 221)
            while seat not in seats: # генерир. случ. ч., пока не найдем свободное место
                seat = random.randint(1, 221)
            chosen_seats.append((i, seat))
            seats[seat - 1] = 0
    if chosen_seats[-1][0] == chosen_seats[-1][1]: # если номер места пассажира и номер, где он сидит совпадают
        auspicious_events += 1 # то, что нам нужно
answer = auspicious_events / N
print(auspicious_events/N)

