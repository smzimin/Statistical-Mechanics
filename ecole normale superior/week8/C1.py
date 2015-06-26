import random, math


def mainC1():
    nbr = {i : ((i // L) * L + (i + 1) % L, (i + L) % N,
                (i // L) * L + (i - 1) % L, (i - L) % N) \
                                        for i in range(N)}
    beta = 1.0 / T
    S = [random.choice([-1, 1]) for site in range(N)]
    E = -0.5 * sum(S[k] * sum(S[nn] for nn in nbr[k]) \
                                    for k in range(N))
    Energies = []
    for step in range(nsteps):
        if step % 10000 == 0:
            print(step)
        k = random.randint(0, N - 1)
        Upsilon = random.uniform(0.0, 1.0)
        h = sum(S[nn] for nn in nbr[k])
        Sk_old = S[k]
        S[k] = -1
        if Upsilon < 1.0 / (1.0 + math.exp(-2.0 * beta * h)):
            S[k] = 1
        if S[k] != Sk_old:
            E -= 2.0 * h * S[k]
        Energies.append(E)
    print('mean energy per spin:', sum(Energies) / float(len(Energies) * N))


L = 6
N = L * L
nsteps =  N * 10 ** 5
T = 2.0
mainC1()
