import random, math, pylab

def prob(x):
    s1 = math.exp(-(x + 1.2) ** 2 / 0.72)
    s2 = math.exp(-(x - 1.5) ** 2 / 0.08)
    return (s1 + 2.0 * s2) / math.sqrt(2.0 * math.pi)

delta = 10
nsteps = 10 ** 6
acc_tot = 0
x = 0.0
x_av = 0.0
acc_tmp = 0
data = []
for step in range(nsteps):
    if step % 100 == 0:
        if acc_tmp > 60:
            delta = delta * 1.1
        elif acc_tmp < 40:
            delta = delta / 1.1
        acc_tmp = 0
    xnew = x + random.uniform(-delta, delta)
    if random.uniform(0.0, 1.0) < prob(xnew) / prob(x):
        x = xnew
        acc_tot += 1
        acc_tmp += 1
    x_av += x
    data.append(x)

print('global acceptance ratio:', acc_tot / float(nsteps))
print('<x> =', x_av / float(nsteps))

t = [ i * 0.01 for i in range(-300, 300)]
pi_x = [ prob(i) for i in t]
pylab.hist(data, normed=True, bins=100, label='MC Simulation')
pylab.plot(t, pi_x, 'r', linewidth = 2.5, label='the exact distribution')
pylab.legend()
pylab.show()
