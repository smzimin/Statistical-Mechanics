import random, math

n_trials = 400000
n_hits = 0
var = 0.0
for iter in range(n_trials):
    x, y = random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)
    Obs = 0.0
    if x**2 + y**2 < 1.0:
        n_hits += 1
        Obs = 4.0
    var += (Obs - math.pi)**2

Eobs = 4.0 * n_hits / float(n_trials)
Eobs2 = 16.0 * n_hits / float(n_trials)
sigm = Eobs2 - Eobs ** 2
print Eobs, Eobs2, sigm, math.sqrt(sigm),  math.sqrt(var / n_trials)

