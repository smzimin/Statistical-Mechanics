import random, math, pylab

samples_x = []
samples_y = []

def gauss_cut():
    while True:
        x = random.gauss(0.0, 1.0)
        if abs(x) <= 1.0:
            return x

def mainA2(nsteps, alpha):
    x, y = 0.0, 0.0
    for step in range(nsteps):
        if step % 2 == 0:
            while True:
                #x = random.uniform(-1.0, 1.0)
                #p = math.exp(-0.5 * x ** 2 - alpha * x ** 4 )
                x = gauss_cut()
                p = math.exp(- alpha * x ** 4 )
                if random.uniform(0.0, 1.0) < p:
                    break
        else:
            while True:
                #y = random.uniform(-1.0, 1.0)
                #p = math.exp(-0.5 * y ** 2 - alpha * y ** 4 )
                y = gauss_cut()
                p = math.exp(- alpha * y ** 4 )
                if random.uniform(0.0, 1.0) < p:
                    break
        samples_x.append(x)
        samples_y.append(y)

alpha = 0.5
nsteps = 1000000
mainA2(nsteps, alpha)

pylab.hexbin(samples_x, samples_y, gridsize=50, bins=1000)
pylab.axis([-1.0, 1.0, -1.0, 1.0])
cb = pylab.colorbar()
pylab.xlabel('x')
pylab.ylabel('y')
pylab.title('A2_1')
pylab.savefig('plot_A2_1.png')
pylab.show()