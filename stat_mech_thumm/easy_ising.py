import numpy as np
import random
import pylab
import sys
sys.setrecursionlimit(10000)


def func(k, j, L, lattice, visited):
    v_temp = 1
    if k - 1 >= 0:
        if not visited[k-1, j] and lattice[k-1, j]:
            visited[k-1, j] = True
            v_temp += func(k-1, j, L, lattice, visited)
    if k + 1 < L:
        if not visited[k+1, j] and lattice[k+1, j]:
            visited[k+1, j] = True
            v_temp += func(k+1, j, L, lattice, visited)
    if j - 1 >= 0:
        if not visited[k, j-1] and lattice[k, j-1]:
            visited[k, j-1] = True
            v_temp += func(k, j-1, L, lattice, visited)
    if j + 1 < L:
        if not visited[k, j+1] and lattice[k, j+1]:
            visited[k, j+1] = True
            v_temp += func(k, j+1, L, lattice, visited)
    return v_temp


def one_run(L, p):
    lattice = np.zeros((L, L), dtype=np.bool)
    visited = np.zeros((L, L), dtype=np.bool)

    for k in range(L):
        for j in range(L):
            if random.uniform(0.0, 1.0) < p:
                lattice[k][j] = True

    v_max = 0
    for k in range(L):
        for j in range(L):
            if not visited[k, j] and lattice[k, j]:
                visited[k, j] = True
                v_temp = func(k, j, L, lattice, visited)
                if v_max < v_temp:
                    v_max = v_temp

    return v_max


Ls = [10, 20, 50]
#Ls = [10, 10, 10, 10]
probs = np.linspace(0.0, 1.0, num=20)
n_trials = 10 ** 3
volumes = np.zeros((len(Ls), len(probs)))
volumes[:, len(probs)-1] += 1

for k in range(len(Ls)):
    for j in range(1, len(probs)):
        print(Ls[k], probs[j])
        if probs[j] != 1.0:
            for _ in range(n_trials):
                volumes[k, j] += one_run(Ls[k], probs[j])
            volumes[k, j] /= n_trials * Ls[k] ** 2


pylab.plot(probs, volumes[0, :], 'r', linewidth=2.0, label='L = 10')
pylab.plot(probs, volumes[1, :], 'b', linewidth=2.0, label='L = 20')
pylab.plot(probs, volumes[2, :], 'g', linewidth=2.0, label='L = 50')
#pylab.plot(probs, volumes[3, :], 'y', linewidth=2.0, label='L = 100')
pylab.legend(loc='upper left')
pylab.show()





