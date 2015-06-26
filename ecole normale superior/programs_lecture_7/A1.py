import math, random, pylab

def levy_harmonic_path(k):
    x = [random.gauss(0.0, 1.0 / math.sqrt(2.0 * math.tanh(k * beta / 2.0)))]
    if k == 2:
        Ups1 = 2.0 / math.tanh(beta)
        Ups2 = 2.0 * x[0] / math.sinh(beta)
        x.append(random.gauss(Ups2 / Ups1, 1.0 / math.sqrt(Ups1)))
    return x[:]

def pi_x(x, beta):
    sigma = 1.0 / math.sqrt(2.0 * math.tanh(beta / 2.0))
    return math.exp(-x ** 2 / (2.0 * sigma ** 2)) / math.sqrt(2.0 * math.pi) / sigma

beta = 2.0
nsteps = 100000
low = levy_harmonic_path(2)
high = low[:]
data = []
for step in range(nsteps):
    k = random.choice([0, 1])
    low[k] = levy_harmonic_path(1)[0]
    high[k] = low[k]
    data.append(low[k])


x = [0.1 * a for a in range (-30, 31)]
pi_X = [pi_x(a, beta) for a in x]

pylab.hist(data, normed=True, bins=70, label='simulation')
pylab.plot(x, pi_X, color = 'r', linewidth = 2,  label='exact solution')
pylab.xlabel('$x$')
pylab.ylabel('$\\pi(x)$ (normalized)')
#pylab.title('levy_anharmonic_path (beta=%s, N=%i)' % (beta, N))
#pylab.xlim(-2, 2)
#pylab.savefig('plot_A1_beta%s.png' % beta)
pylab.legend()
pylab.show()