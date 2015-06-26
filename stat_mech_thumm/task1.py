import random
import pylab

N = 1000
n = 250
T = 1000
Ex2 = [0] * T
num = [0] * T
number_of_trials = 10 ** 2

for q in range(number_of_trials):
    if q % 10 == 0:
        print(q)
    mass = [0] * N
    for k in range(n):
        mass[4*k] = 1
    indexes = [4*k for k in range(n)]
    distance = [0] * n
    time = [0] * n

    #for t in range(T):
    while T not in time:
        current_number = random.randint(0, n-1)
        current_particle = indexes[current_number]
        move = random.choice([-1, 1])
        if mass[(current_particle+move) % N] == 0:
            mass[(current_particle+move) % N] = 1
           # print(len(mass), current_particle)
            mass[current_particle] = 0
            distance[current_number] += move
            indexes[current_number] = (current_particle + move) % N
        #Ex2[t] += distance[current_number] ** 2
        #num[t] += 1
        Ex2[time[current_number]] += distance[current_number] ** 2
        num[time[current_number]] += 1
        time[current_number] += 1

t = [k for k in range(T)]
Ex2 = [Ex2[k] / num[k] for k in range(T)]
pylab.plot(t, Ex2, linewidth=2.0)
pylab.show()