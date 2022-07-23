import sympy
import matplotlib.pyplot as plt
import matplotlib

# matplotlib.use('GTK4Agg')

primes = sympy.primerange(0, 10000000)
primes = list(primes)

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.scatter(primes, primes, s=0.5)
plt.show()