import random, math, pylab

samples_x = []
samples_y = []


def gauss_cut():
    while True:
        x = random.gauss(0.0, 1.0)
        if abs(x) <= 1.0:
            return x

def mainA1(nsamples, alpha):
    for sample in range(nsamples):
        while True:
            #x = random.uniform(-1.0, 1.0)
            x = gauss_cut()
            #y = random.uniform(-1.0, 1.0)
            y = gauss_cut()
            #p = math.exp(-0.5 * (x ** 2 + y ** 2) - alpha * (x ** 4 + y ** 4))
            p = math.exp(- alpha * (x ** 4 + y ** 4))
            if random.uniform(0.0, 1.0) < p:
                break
        samples_x.append(x)
        samples_y.append(y)

alpha = -100
nsamples = 1000000

mainA1(nsamples, alpha)

pylab.hexbin(samples_x, samples_y, gridsize=50, bins=1000)
pylab.axis([-1.0, 1.0, -1.0, 1.0])
cb = pylab.colorbar()
pylab.xlabel('x')
pylab.ylabel('y')
pylab.title('A1_1')
pylab.savefig('plot_A1_1.png')
pylab.show()