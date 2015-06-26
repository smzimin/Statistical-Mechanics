import numpy
from random import randint
import pylab

moves = {
0: -1,
1: 1
}


n_steps = 100

f = numpy.zeros(shape=n_steps, dtype=float)
p = numpy.zeros(shape=n_steps, dtype=float)
n_trials = 10000
for i in range(n_trials):
    pos = 0
    wasAtZero = False
    if i % 100 == 0:
        print(i)
    for k in range(n_steps):
        pos += moves[randint(0, 1)]
        pos += moves[randint(0, 1)]
        if pos != 0 and not wasAtZero:
            f[k] += 1
        elif pos == 0 and not wasAtZero:
            p[k] += 1
            wasAtZero = True
p /= n_trials
f /= n_trials


pylab.plot(f, 'b', linewidth=2.0)
pylab.plot(f, 'bs', linewidth=2.0)
pylab.plot(p, 'r', linewidth=2.0)
pylab.plot(p, 'r^', linewidth=2.0)
pylab.show()