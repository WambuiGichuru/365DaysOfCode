# builidng the beauty in randomness

# importing necessary pac
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.font_manager import FontProperties
import numpy as np

# class
class Attractor:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.sigma = 10
        self.beta = 8/3
        self.rho = 28

    def step(self, dt=0.005):
        dx = self.sigma * (self.y - self.x)
        dy = self.x * (self.rho - self.z) - self.y
        dz = self.x * self.y - self.beta - self.z

        self.x += dx * dt
        self.y += dy * dt
        self.z = dz * dt

butterfly = Attractor(1,1,1)
N = 15000
x, y, z = [], [], []
for i in range (N):
    x.append(butterfly.x)
    y.append(butterfly.y)
    z.append(butterfly.z)
    butterfly.step()

x, y, z = np.array(x), np.array(y), np.array(z)

points = np.array([x, z]).T.reshape(-1,1,2)
segments = np.concatenate([points[:-1], points[1:]], axis = 1)

lc =LineCollection(segments, cmap = 'cool')
lc.set_array(y)
lc.set_linewidth(2)

fig, ax= plt.subplots(figsize =(16,9))
ax.plot(x,z, lw=0.4, color='lightseagreen')
ax.spines[['right','top','bottom','left']].set_visible(False)
ax.set_xticks([])
ax.set_yticks([])
ax.set_facecolor('black')
#ax.text(-21, 2, 'Lorenz Attractor', fontproperties=font_prop, fontsize=25)
ax.patch.set_alpha(0.7)
plt.savefig("Lorenztrial1.png")