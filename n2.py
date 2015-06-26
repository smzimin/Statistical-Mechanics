import numpy
from random import randint
import pylab

moves = {0: -1,
         1: 1}

p = numpy.zeros(shape=101, dtype=float)
pTheoretical = numpy.zeros(shape=101, dtype=float)
p[0] = 1
pTheoretical[0] = 1
n_trials = 1000
for k in range(1, 101):
    print(k)
    for i in range(n_trials):
        pos = k
        while pos > 0 and pos < 100:
            pos += moves[randint(0, 1)]
        if pos == 0:
            p[k] += 1
    p[k] /= n_trials
    pTheoretical[k] = 1 - k / 100

pylab.plot(p, 'b', linewidth=2.0)
pylab.plot(p, 'bs', linewidth=2.0)
pylab.plot(pTheoretical, 'r', linewidth=2.0)
pylab.show()