import random, math, os

def energy(S, N, nbr):
    E = 0.0
    for k in range(N):
        E -=  S[k] * sum(S[nn] for nn in nbr[k])
    return 0.5 * E

def reading():
    if os.path.isfile(filename):
        f = open(filename, 'r')
        S = []
        for line in f:
            S.append(int(line))
        f.close()
        #print('Starting from file', filename)
    else:
        S = [random.choice([1, -1]) for k in range(N)]
        #print('Starting from a random configuration')
    return S

def writing():
    f = open(filename, 'w')
    for a in S:
       f.write(str(a) + '\n')
    f.close()

def mainB1():
    nbr = {i : ((i // L) * L + (i + 1) % L, (i + L) % N,
                (i // L) * L + (i - 1) % L, (i - L) % N)
                                        for i in range(N)}

    p  = 1.0 - math.exp(-2.0 / T)

    S = [random.choice([1, -1]) for k in range(N)]
    E = [energy(S, N, nbr)]
    for step in range(nsteps):
        k = random.randint(0, N - 1)
        Pocket, Cluster = [k], [k]
        while Pocket != []:
            j = Pocket.pop()
            #j = random.choice(Pocket)
            for l in nbr[j]:
                if S[l] == S[j] and l not in Cluster \
                       and random.uniform(0.0, 1.0) < p:
                    Pocket.append(l)
                    Cluster.append(l)
            #Pocket.remove(j)
        for j in Cluster:
            S[j] *= -1
        E.append(energy(S, N, nbr))
    #print('mean energy per spin:', sum(E) / float(len(E) * N))
    return E


T = 2.27
L = 6

nsteps = 10 ** 3

for L in [32]:
    N = L * L
    filename = 'data_local_'+ str(L) + '_' + str(T) + '.txt'
    for _ in range(3):
        S = reading()
        E = mainB1()
        writing()

    E_mean = sum(E) / len(E)
    E2_mean = sum(a ** 2 for a in E) / len(E)
    cv = (E2_mean - E_mean ** 2 ) / N / T ** 2

    print(L, E_mean, E2_mean, cv)