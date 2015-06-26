import numpy
from random import randint
import pylab

moves1 = {
0: -1,
1: 1
}

moves2 = {
0: [-1, 0],
1: [1, 0],
2: [0, -1],
3: [0, 1]
}

moves3 = {
0: [-1, 0, 0],
1: [1, 0, 0],
2: [0, -1, 0],
3: [0, 1, 0],
4: [0, 0, -1],
5: [0, 0, 1]
}

def randomWalkOnLatticeD1(n_steps, size):
    w = numpy.zeros(shape=n_steps, dtype=int)
    x = (size - 1) / 2
    lattice = numpy.zeros(shape=size, dtype=bool)
    lattice[x] = True
    counter = 1
    for k in range(n_steps):
        x = numpy.add(x, moves1[randint(0, 1)])
        if not lattice[x]:
            lattice[x] = True
            counter += 1
        w[k] = counter
    return w

def randomWalkOnLatticeD2(n_steps, size):
    w = numpy.zeros(shape=n_steps, dtype=int)
    x = [(size - 1) / 2] * 2
    lattice = numpy.zeros(shape=(size, size), dtype=bool)
    lattice[x[0]][x[1]] = True
    counter = 1
    for k in range(n_steps):
        x = numpy.add(x, moves2[randint(0, 3)])
        if not lattice[x[0]][x[1]]:
            lattice[x[0]][x[1]] = True
            counter += 1
        w[k] = counter
    return w

def randomWalkOnLatticeD3(n_steps, size):
    w = numpy.zeros(shape=n_steps, dtype=int)
    x = [(size - 1) / 2] * 3
    lattice = numpy.zeros(shape=(size, size, size), dtype=bool)
    lattice[x[0]][x[1]][x[2]] = True
    counter = 1
    for k in range(n_steps):
        x = numpy.add(x, moves3[randint(0, 5)])
        if not lattice[x[0]][x[1]][x[2]]:
            lattice[x[0]][x[1]][x[2]] = True
            counter += 1
        w[k] = counter
    return w

n_steps = 1000
size = 2 * n_steps + 1
n_trials = 1000
w = numpy.zeros(shape=n_steps, dtype=int)
for k in range(n_trials):
    if k % 100 == 0:
        print(k)
    w += randomWalkOnLatticeD2(n_steps, size)

w /= n_trials

pylab.plot(w)
pylab.show()