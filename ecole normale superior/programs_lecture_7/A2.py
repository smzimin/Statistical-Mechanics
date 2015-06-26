import math, random, pylab



def levy_harmonic_path(k):
    x = [random.gauss(0.0, 1.0 / math.sqrt(2.0 * math.tanh(k * beta / 2.0)))]
    if k == 2:
        Ups1 = 2.0 / math.tanh(beta)
        Ups2 = 2.0 * x[0] / math.sinh(beta)
        x.append(random.gauss(Ups2 / Ups1, 1.0 / math.sqrt(Ups1)))
    return x[:]

def rho_harm_1d(x, xp, beta):
    Upsilon_1 = (x + xp) ** 2 / 4.0 * math.tanh(beta / 2.0)
    Upsilon_2 = (x - xp) ** 2 / 4.0 / math.tanh(beta / 2.0)
    return math.exp(- Upsilon_1 - Upsilon_2)

def z(beta):
    return 1.0 / (1.0 - math.exp(- beta))

def pi_two_bosons(x, beta):
    pi_x_1 = math.sqrt(math.tanh(beta / 2.0)) / math.sqrt(math.pi) *\
             math.exp(-x ** 2 * math.tanh(beta / 2.0))
    pi_x_2 = math.sqrt(math.tanh(beta)) / math.sqrt(math.pi) *\
             math.exp(-x ** 2 * math.tanh(beta))
    weight_1 = z(beta) ** 2 / (z(beta) ** 2 + z(2.0 * beta))
    weight_2 = z(2.0 * beta) / (z(beta) ** 2 + z(2.0 * beta))
    pi_x = pi_x_1 * weight_1 + pi_x_2 * weight_2
    return pi_x

def mainA2(beta, nsteps):
    prob_one_cycle = 0
    data = []
    low = levy_harmonic_path(2)
    high = low[:]
    for step in range(nsteps):
        # move 1
        if low[0] == high[0]:
            k = random.choice([0, 1])
            low[k] = levy_harmonic_path(1)[0]
            high[k] = low[k]
        else:
            low[0], low[1] = levy_harmonic_path(2)
            high[1] = low[0]
            high[0] = low[1]
            prob_one_cycle += 1
        data += low[:]
        # move 2
        weight_old = (rho_harm_1d(low[0], high[0], beta) *
                      rho_harm_1d(low[1], high[1], beta))
        weight_new = (rho_harm_1d(low[0], high[1], beta) *
                      rho_harm_1d(low[1], high[0], beta))
        if random.uniform(0.0, 1.0) < weight_new / weight_old:
            high[0], high[1] = high[1], high[0]

    return prob_one_cycle / nsteps

list_beta = [0.1, 0.3, 0.5, 0.8, 1.0, 2.0, 3.0, 4.0, 5.0]
nsteps = 5000
t = 0
prob_one_cycle = [0] * len(list_beta)
prob_two_cycles = [0] * len(list_beta)
for beta in list_beta:
    prob_one_cycle[t] = mainA2(beta, nsteps)
    prob_two_cycles[t] = 1 - prob_one_cycle[t]
    t += 1


fract_two_cycles = [z(beta) ** 2 / (z(beta) ** 2 + z(2.0 * beta)) for beta in list_beta]
fract_one_cycle = [z(2.0 * beta) / (z(beta) ** 2 + z(2.0 * beta)) for beta in list_beta]
pylab.plot(list_beta, fract_one_cycle, color = 'r', linewidth = 2,  label='exact solution')
pylab.plot(list_beta, prob_one_cycle, 'b--', linewidth = 2,  label='simulations')
pylab.xlabel('beta')
pylab.ylabel('prob_one_cycle')
print(list_beta)
print(prob_two_cycles)

#x = [0.1 * a for a in range (-30, 31)]
#pi_X = [pi_two_bosons(a, beta) for a in x]
#pylab.hist(data, normed=True, bins=100, label='simulation')
#pylab.plot(x, pi_X, color = 'r', linewidth = 2,  label='exact solution')
#pylab.xlabel('$x$')
#pylab.ylabel('$\\pi(x)$ (normalized)')
#pylab.title('levy_anharmonic_path (beta=%s, N=%i)' % (beta, N))
#pylab.xlim(-2, 2)
#pylab.savefig('plot_A1_beta%s.png' % beta)
pylab.legend()
pylab.show()