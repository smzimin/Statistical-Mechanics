import random, math, pylab, os, cmath

def my_markov_disks(N = 64, eta = 0.42, n_steps = 100):
    sigma = math.sqrt(eta / (math.pi * N))
    L = []
    filename = 'disk_configuration_N%i_eta%.2f.txt' % (N, eta)
    if os.path.isfile(filename):
        f = open(filename, 'r')
        for line in f:
            a, b = line.split()
            L.append([float(a), float(b)])
        f.close()
        print ('starting from file', filename)
    else:
        N_sqrt = int(math.sqrt(N))
        delxy = 0.5 / N_sqrt
        two_delxy = 2 * delxy
        L = [[delxy + i * two_delxy, delxy + j * two_delxy] for i in range(N_sqrt) for j in range(N_sqrt)]
        print ('starting from a new random configuration')
        f = open(filename, 'w')
        for a in L:
           f.write(str(a[0]) + ' ' + str(a[1]) + '\n')
        f.close()

    L = generate_markovs_disks(L, eta, sigma, n_steps)
    plot_circles(L, N, eta, sigma)

def delx_dely(x, y):
    d_x = (x[0] - y[0]) % 1.0
    if d_x > 0.5: d_x -= 1.0
    d_y = (x[1] - y[1]) % 1.0
    if d_y > 0.5: d_y -= 1.0
    return d_x, d_y

def Psi_6(L, sigma):
    sum_vector = 0j
    for i in range(N):
        vector  = 0j
        n_neighbor = 0
        for j in range(N):
            if dist(L[i], L[j]) < 2.8 * sigma and i != j:
                n_neighbor += 1
                dx, dy = delx_dely(L[j], L[i])
                angle = cmath.phase(complex(dx, dy))
                vector += cmath.exp(6.0j * angle)
        if n_neighbor > 0:
            vector /= n_neighbor
        sum_vector += vector
    return sum_vector / float(N)

def dist(x,y):
    d_x = abs(x[0] - y[0]) % 1.0
    d_x = min(d_x, 1.0 - d_x)
    d_y = abs(x[1] - y[1]) % 1.0
    d_y = min(d_y, 1.0 - d_y)
    return  math.sqrt(d_x**2 + d_y**2)

def generate_markovs_disks(L, eta, sigma, n_steps):
    sigma_sq = sigma ** 2
    delta = 0.1
    for steps in range(n_steps):
        a = random.choice(L)
        b = [a[0] + random.uniform(-delta, delta), a[1] + random.uniform(-delta, delta)]
        min_dist = min(dist(b,c) for c in L if c != a)
        b[0], b[1] = b[0] % 1, b[1] % 1
        if not min_dist < 2.0 * sigma:
            a[:] = b
    return L

def plot_circles(L, N, eta, sigma):
    for [x, y] in L:
        color = random.choice(['g', 'b', 'r', 'y', 'm'])
        for ix in range(-1, 2):
            for iy in range(-1, 2):
                cir = pylab.Circle((x + ix, y + iy), radius=sigma,  fc=color)
                pylab.gca().add_patch(cir)

    pylab.axis('scaled')
    pylab.title('N = ' + str(N) + ', \eta = ' + str(eta))
    pylab.axis([0.0, 1.0, 0.0, 1.0])
    pylab.show()
    pylab.close()

#my_markov_disks(N = 256, eta = 0.72, n_steps = 0)



N = 64
N_sqrt = int(math.sqrt(N))
delxy = 0.5 / N_sqrt
two_delxy = 2 * delxy
etas = [x * 0.01 for x in range(0,72, 1)]
etas.append(0.72)
psi6 = [0 for x in range(len(etas))]

for index in range(len(etas)):
    print(etas[index])
    sigma = math.sqrt(etas[index] / (math.pi * N))
    L = [[delxy + i * two_delxy, delxy + j * two_delxy] for i in range(N_sqrt) for j in range(N_sqrt)]
    for k in range(2000):
        L = generate_markovs_disks(L, etas[index], sigma, 100)
        psi6[index] += abs(Psi_6(L, sigma))
    psi6[index] /= 2000

pylab.plot(etas, psi6,'r', linewidth =2.0)
pylab.title('<|Psi6|> vs Eta')
pylab.show()