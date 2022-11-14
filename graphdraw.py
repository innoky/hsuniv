
from numpy import sqrt, sin, cos, pi
import matplotlib.pyplot as plt
import os.path
import numpy as np
x = np.linspace(-5,5,100)
y=tan(x)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# plot the function
plt.plot(x,y, 'r')

# show the plot
plt.savefig('/home/innoky/Documents/hsbot/hsuniv/graphs/graphdraw.png')
