import matplotlib.pyplot as plt
path = '~/Documents/work/git_work/mplstyle/'
plt.style.use(path + 'timesnromanstyle.mplstyle')
import numpy as np

# What we want to plot
xvalues = np.linspace(0, 1, 5, endpoint=True)
def linear(x, a):
    return a*x
vec_linear = np.vectorize(linear)

# Minimal set-up
f, ax = plt.subplots()

ax.set_ylabel(r'A nice function $\alpha\beta\gamma\delta$')
ax.set_xlabel(r'Some variable $\epsilon\sigma\rho\tau\iota$')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1.5)

ax.plot(xvalues, vec_linear(xvalues, 1))
ax.plot(xvalues, vec_linear(xvalues, 1.2))
ax.plot(xvalues, vec_linear(xvalues, 1.4))
ax.plot(xvalues, vec_linear(xvalues, 1.5))

ax.legend(['Curve 1', 'Curve 2', 'Curve 3', 'Curve 4'])

plt.savefig('example_tnrstyle.jpg')