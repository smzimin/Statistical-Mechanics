import random, math, pylab

def Q(d, n_trials):
    radiuses = [0]
    x = [0] * (d - 1)
    delta = 1
    n_hits = 0
    old_radius_square = 0
    counter = 0
    for i in range(n_trials):
        k = random.randint(0, d - 2)
        x_old_k = x[k]
        x_new_k = x_old_k + random.uniform(-delta, delta)
        new_radius_square = old_radius_square + x_new_k ** 2 - x_old_k ** 2
        if new_radius_square < 1.0:
            counter += 1
            x[k] = x_new_k
            old_radius_square = new_radius_square
        z = random.uniform(-delta, delta)
        if old_radius_square + z ** 2 < 1.0:
            n_hits += 1
            radiuses.append(math.sqrt(old_radius_square + z ** 2))
    q = 2.0 * n_hits / float(n_trials)
    #print(d, q)
    return q


def V_sph(dim):
    return math.pi ** (dim / 2.0) / math.gamma(dim / 2.0 + 1.0)


d = 20
vs20exact = V_sph(d)
for i in range(7):
    n_trials = 10 ** i
    vs20 = 0
    vs20sq = 0
    for _ in range(10):
        tempV = 2
        for dtemp in range(2, d+1):
            tempV *= Q(dtemp, n_trials)
        vs20 += tempV
        vs20sq += vs20 ** 2
    vs20 /= 10
    vs20sq /= 10
    error = (vs20sq - vs20 ** 2) / math.sqrt(n_trials)
    print(n_trials, vs20, vs20exact, error, vs20 - vs20exact)