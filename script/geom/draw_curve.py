



'''
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)
ax.plot(x, y, z, label='parametric curve')
ax.legend()

plt.show()


'''




import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')

t = np.linspace(-2, 2, 100)

def t2xyz(t, a,b,c):
    x = a*t
    y = b*t**2
    z = c*t**3
    return x, y, z
x, y, z = t2xyz(t, 1, 1, 1)

ax.plot(x, y, z, label='三次挠曲线　r=(a t, b t**2, c t**3)')
ax.legend()

plt.show()







