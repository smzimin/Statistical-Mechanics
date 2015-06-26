import math, random

def V(x, y):
    pot  = -4.0 * x ** 2 - x ** 3 + 4.0 * x ** 4
    pot += -4.0 * y ** 2 - y ** 3 + 4.0 * y ** 4
    return pot

def mainA2():
    n_success = 0
    for run in range(n_runs):
        T = 4.0
        x, y = 0.0, 0.0
        delta = 0.1
        step = 0
        acc = 0
        while T > 0.00001:
            step += 1
            if step == 100:
                T *= (1.0 - gamma)
                if acc < 30:
                   delta /= 1.2
                elif acc > 70:
                   delta *= 1.2
                step = 0
                acc = 0
            xnew = x + random.uniform(-delta, delta)
            ynew = y + random.uniform(-delta, delta)
            if abs(xnew) < 1.0 and abs(ynew) < 1.0 and \
               random.uniform(0.0, 1.0) < math.exp(- (V(xnew, ynew) - V(x, y)) / T):
                x = xnew
                y = ynew
                acc += 1
        if math.sqrt((x - xmin) ** 2 + (y - ymin) ** 2) < 0.1:
            n_success += 1
    return n_success


xmin, ymin = 0.807044513157, 0.807044513157
gammas = [0.0025, 0.0075, 0.01, 0.05, 0.1, 0.6]
n_runs = 20
for gamma in gammas:
    n_success = mainA2()
    print(gamma, '\t', n_success / float(n_runs))
