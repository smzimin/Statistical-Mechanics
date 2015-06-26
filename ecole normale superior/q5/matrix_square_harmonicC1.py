import math, numpy, pylab

def pi_quant(x, beta):
    return math.sqrt( math.tanh(beta/2) / math.pi) * math.exp( - x ** 2 * math.tanh(beta/2))

def rho_free(x, xp, beta):
    return (math.exp(-(x - xp) ** 2 / (2.0 * beta)) /
            math.sqrt(2.0 * math.pi * beta))

def V(x, cubic, quartic):
    return x ** 2 / 2.0 + cubic * x ** 3 + quartic * x ** 4

def Energy_pert(n, cubic, quartic):
    return n + 0.5 - 15.0 / 4.0 * cubic **2 * (n ** 2 + n + 11.0 / 30.0) \
         + 3.0 / 2.0 * quartic * (n ** 2 + n + 1.0 / 2.0)

def Z_pert(cubic, quartic, beta, n_max):
    Z = sum(math.exp(-beta * Energy_pert(n, cubic, quartic)) for n in range(n_max + 1))
    return Z

def rho_anharmonic_trotter(grid, beta, cubic, quartic):
    return numpy.array([[rho_free(x, xp, beta) * \
                         numpy.exp(-0.5 * beta * (V(x, cubic, quartic) + V(xp, cubic, quartic))) \
                         for x in grid] for xp in grid])

quartics = [0.001, 0.01, 0.1, 0.2, 0.3, 0.4]
x_max = 5.0                              # the x range is [-x_max,+x_max]
nx = 100
dx = 2.0 * x_max / (nx - 1)
x = [i * dx for i in range(-int(nx / 2), int(nx / 2) + 1)]
beta_tmp = 2.0 ** (-5)                   # initial value of beta (power of 2)
beta     = 2.0 ** 2                      # actual value of beta (power of 2)

zets = [[], []]


for quartic in quartics:
    cubic = - quartic
    rho = rho_anharmonic_trotter(x, beta_tmp, cubic, quartic)  # density matrix at initial beta
    while beta_tmp < beta:
        rho = numpy.dot(rho, rho)
        rho *= dx
        beta_tmp *= 2.0
        #print('beta: %s -> %s' % (beta_tmp / 2.0, beta_tmp))
    Z = sum(rho[j, j] for j in range(nx + 1)) * dx
    Z_p = 0
    try:
        Z_p = Z_pert(cubic, quartic, beta, nx)
    except OverflowError:
        pass
    zets[0].append(Z)
    zets[1].append(Z_p)

#pi_of_x = [rho[j, j] / Z for j in range(nx + 1)]
#f = open('data_anharm_matrixsquaring_beta' + str(beta) + '.dat', 'w')
#for j in range(nx + 1):
#    f.write(str(x[j]) + ' ' + str(rho[j, j] / Z) + '\n')
#f.close()

pylab.plot(quartics, zets[0], 'r', linewidth=4.0)
pylab.plot(quartics, zets[1], 'b', linewidth=3.0)
pylab.plot(quartics, zets[0], 'rs', linewidth=4.0)
pylab.plot(quartics, zets[1], 'b^', linewidth=3.0)

#pylab.plot(x, pi_of_x, 'r', linewidth=4.0)
#t = [x*0.1 for x in range(-50, 50)]
#pylab.plot(t, [pi_quant(x, beta) for x in t], 'b--', linewidth=2.0)
pylab.xlabel('$quartic$', fontsize=16)
pylab.ylabel('$Z$', fontsize=16)
#pylab.title('$\\beta$=%s, quartic=%s' % (beta, quartic))
pylab.legend(('Z', 'Z_pert'), loc='upper right')
#pylab.xlim(-3.0, 3.0)
pylab.show()