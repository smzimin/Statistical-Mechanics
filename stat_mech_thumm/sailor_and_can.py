import random
import pylab

T = 1
t = [k for k in range(T)]
Ex2 = [0] * T

number_of_trials = 10 ** 5
for _ in range(number_of_trials):
    sailor = 0
    can = 0
    for i in range(T):
        move = random.choice([-1, 1])
        if sailor == can:
            sailor += move
            can += move
        else:
            sailor += move
        Ex2[i] += can ** 2

Ex2 = [Ex2[k] / number_of_trials for k in range(T)]

pylab.plot(t, Ex2, linewidth=2.0)
pylab.show()