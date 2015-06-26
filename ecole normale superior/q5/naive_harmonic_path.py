import math, random, pylab

x0_all = []
x1_all = []
x8_all = []

def rho_free(x, y, beta):    # free off-diagonal density matrix
    return math.exp(-(x - y) ** 2 / (2.0 * beta))

def read_file(filename):
    list_x = []
    list_y = []
    with open(filename) as f:
        for line in f:
            x, y = line.split()
            list_x.append(float(x))
            list_y.append(float(y))
    f.close()
    return list_x, list_y

def mainB2(beta, N, n_steps):                                          # number of slices
    dtau = beta / N
    delta = 1.0                                       # maximum displacement on one slice
    x = [0.0] * N                                     # initial path
    for step in range(n_steps):
        k = random.randint(0, N - 1)                  # random slice
        knext, kprev = (k + 1) % N, (k - 1) % N       # next/previous slices
        x_new = x[k] + random.uniform(-delta, delta)  # new position at slice k
        old_weight  = (rho_free(x[knext], x[k], dtau) *
                       rho_free(x[k], x[kprev], dtau) *
                       math.exp(-0.5 * dtau * x[k] ** 2))
        new_weight  = (rho_free(x[knext], x_new, dtau) *
                       rho_free(x_new, x[kprev], dtau) *
                       math.exp(-0.5 * dtau * x_new ** 2))
        if random.uniform(0.0, 1.0) < new_weight / old_weight:
            x[k] = x_new
        if step % 10 == 0:
            for t in range(N):
                x0_all.append(x[t])
            #x1_all.append(x[1])
            #x8_all.append(x[8])

beta = 4.0
N = 10
n_steps = 10 ** 6
mainB2(beta, N, n_steps)
list_x, list_y = read_file('data_harm_matrixsquaring_beta4.0.dat')

pylab.figure(1)
pylab.hist(x0_all, normed=True, bins=41)
pylab.plot(list_x, list_y, 'r', linewidth=4.0)

pylab.xlabel('$x$', fontsize=16)
pylab.ylabel('$pi(x)$', fontsize=16)
pylab.title('$\\beta$=%s' % beta)
pylab.legend(('rho(x, x, beta) / Z', 'Simulation of x[0]'), loc = 'upper right')
pylab.xlim(-3.0, 3.0)
pylab.show()