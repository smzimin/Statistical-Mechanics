import random, math, pylab

x_all = []

def psi_n_square(x, n):
    if n == -1:
        return 0.0
    else:
        psi = [math.exp(-x ** 2 / 2.0) / math.pi ** 0.25]
        psi.append(math.sqrt(2.0) * x * psi[0])
        for k in range(2, n + 1):
            psi.append(math.sqrt(2.0 / k) * x * psi[k - 1] -
                       math.sqrt((k - 1.0) / k) * psi[k - 2])
        return psi[n] ** 2

def pi_quant(x, beta):
    return math.sqrt( math.tanh(beta/2) / math.pi) * math.exp( - x ** 2 * math.tanh(beta/2))

def pi_class(x, beta):
    return math.sqrt(beta/ (2*math.pi)) * math.exp(- beta * x ** 2 / 2)

def mainA2(beta, n_trials):
    x = 0.0
    n = 0
    delta = 0.5
    for k in range(n_trials):
        if k % 2 == 0:
            x_new = x + random.uniform(-delta, delta)
            if random.uniform(0.0, 1.0) <  \
                psi_n_square(x_new, n) / psi_n_square(x,n):
                x = x_new
        else:
            m = n + random.choice([-1, 1])
            if random.uniform(0.0, 1.0) <  \
                            (psi_n_square(x,m)/psi_n_square(x,n)) * math.exp(-beta*(m - n)):
                n = m
        x_all.append(x)


betas = [0.2, 1, 5]
n_trials = 10 ** 6
l = 100
#pylab.figure(1)

for beta in betas:
    mainA2(beta, n_trials)
    if beta == 0.2:
        pylab.figure(1)
    elif beta == 1:
        l = 80
        pylab.figure(2)
    else:
        l = 60
        pylab.figure(3)
    t = [x*0.1 for x in range(-l, l)]
    pylab.plot(t, [pi_quant(x, beta) for x in t], 'r', linewidth=4.0)
    pylab.plot(t, [pi_class(x, beta) for x in t], 'g--', linewidth=2.0)
    pylab.hist(x_all, normed=True, bins=121)
    pylab.xlabel('$x$', fontsize=16)
    pylab.ylabel('$pi_{quant}(x)$', fontsize=16)
    pylab.title('$\\beta$=%s' % beta)
    pylab.legend(('Exact pi_quant(x)', 'pi_class(x)', 'MK Simulation'), loc = 'upper right')
    pylab.savefig('fig_beta_%s.png'% beta)
    x_all = []