import math, random, pylab

def rho_free(x, y, beta):
    return math.exp(-(x - y) ** 2 / (2.0 * beta))

def V(x, cubic, quartic):
    pot = x ** 2 / 2.0 + cubic * x ** 3 + quartic * x ** 4
    return pot

def levy_harmonic_path(xstart, xend, dtau, N):
    x = [xstart]
    for k in range(1, N):
        dtau_prime = (N - k) * dtau
        Ups1 = 1.0 / math.tanh(dtau) + \
               1.0 / math.tanh(dtau_prime)
        Ups2 = x[k - 1] / math.sinh(dtau) + \
               xend / math.sinh(dtau_prime)
        x.append(random.gauss(Ups2 / Ups1, \
               1.0 / math.sqrt(Ups1)))
    return x

def levy_free_path(xstart, xend, dtau, N):
    x = [xstart]
    for k in range(1, N):
        dtau_prime = (N - k) * dtau
        x_mean = (dtau_prime * x[k - 1] + dtau * xend) / \
                 (dtau + dtau_prime)
        sigma = math.sqrt(1.0 / (1.0 / dtau + 1.0 / dtau_prime))
        x.append(random.gauss(x_mean, sigma))
    return x

def trotter_weight(x, cubic, quartic):
    return sum(-V(a, cubic, quartic) * dtau for a in x)

beta = 0.001
N = 100
dtau = beta / N
delta = 1.0
n_steps = 50000
x = [5.0] * N
#sigma = 1 / math.sqrt( 2 * math.tanh( beta / 2.0))
data = []

Ncut = int(N / 2) + 1
cubic = 0
quartic = -cubic
Trotter_weight_old = math.exp(sum(-V(a, cubic, quartic) * dtau for a in x))
#Trotter_weight_old = trotter_weight(x, cubic, quartic)

for step in range(n_steps):
    x_new = levy_free_path(x[0], x[Ncut], dtau, Ncut) + x[Ncut:]
    Trotter_weight_new = math.exp(sum(-V(a, cubic, quartic) * dtau for a in x_new))
#    Trotter_weight_new = trotter_weight(x, cubic, quartic)
    if random.uniform(0.0, 1.0) < Trotter_weight_new/(Trotter_weight_old + 1e-15):
        x = x_new[:]
        Trotter_weight_old = Trotter_weight_new
        #print(x)
        x = x[Ncut:] + x[:Ncut]
        #print(x)
        #x = x[1:] + x[:1]
    #k = random.randint(0, N - 1)
    data.append(x[0])

pylab.figure(1)
pylab.plot(x, [ i * beta/N for i in range(N)], label='the final path')
pylab.title('The Final Path')
pylab.xlabel('$x$')
pylab.ylabel('imaginary time, $\\tau$')
pylab.show()

pylab.figure(2)
pylab.hist(data, normed=True, bins=70, label='QMC')
pylab.xlabel('$x$')
pylab.ylabel('$\\pi(x)$ (normalized)')
pylab.title('levy_anharmonic_path (beta=%s, N=%i)' % (beta, N))
#pylab.xlim(-2, 2)
pylab.savefig('plot_C1_beta%s.png' % beta)
pylab.show()