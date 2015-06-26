import random, math, os, pylab

def energy(S, N, nbr):
    E = 0.0
    for k in range(N):
        E -=  S[k] * sum(S[nn] for nn in nbr[k])
    return 0.5 * E

def x_y(k, L):
    y = k // L
    x = k - y * L
    return x, y

def reading():
    if os.path.isfile(filename):
        f = open(filename, 'r')
        S = []
        for line in f:
            S.append(int(line))
        f.close()
        print('Starting from file', filename)
    else:
        S = [random.choice([1, -1]) for k in range(N)]
        print('Starting from a random configuration')
    return S

def writing():
    f = open(filename, 'w')
    for a in S:
       f.write(str(a) + '\n')
    f.close()

def plotting():
    conf = [[0 for x in range(L)] for y in range(L)]
    for k in range(N):
        x, y = x_y(k, L)
        conf[x][y] = S[k]
    pylab.imshow(conf, extent=[0, L, 0, L], interpolation='nearest')
    pylab.set_cmap('hot')
    pylab.title('Local_'+ str(T) + '_' + str(L))
    pylab.savefig('plot_A2_local_'+ str(T) + '_' + str(L)+ '.png')
    pylab.show()

def mainA1():
    nbr = {i : ((i // L) * L + (i + 1) % L, (i + L) % N,
                (i // L) * L + (i - 1) % L, (i - L) % N) \
                                        for i in range(N)}
    beta = 1.0 / T
    Energy = energy(S, N, nbr)
    E = []
    for step in range(nsteps):
        if step % 10000 == 0:
            print(step)
        k = random.randint(0, N - 1)
        delta_E = 2.0 * S[k] * sum(S[nn] for nn in nbr[k])
        if random.uniform(0.0, 1.0) < math.exp(-beta * delta_E):
            S[k] *= -1
            Energy += delta_E
        E.append(Energy)
    print('mean energy per spin:', sum(E) / float(len(E) * N))


L = 126
T = 3
N = L * L
filename = 'data_local_'+ str(L) + '_' + str(T) + '.txt'
nsteps = N * 10 ** 2

for _ in range(2):
    S = reading()
    mainA1()
    writing()

plotting()
