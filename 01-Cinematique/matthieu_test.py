# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.widgets import Cursor

def update_plot(i, fig, scat):
    scat.set_offsets(([0, i], [50, i], [100, i]))
    print("Frame: %d" %i)
    return scat
"""
fig = plt.figure()
r = np.arange(1, 5, 0.5)
theta = 2 * np.pi * r

#x = [0, 50, 100]
#y = [0, 0, 0]
x = r * np.cos(theta)
y = r * np.sin(theta)


ax = fig.add_subplot(111)
ax.grid(True, linestyle="-", color="b")
ax.set_xlim([-100, 200])
ax.set_ylim([-100, 200])

scat = plt.scatter(x, y, c=x)
scat.set_alpha(0.8)

anim = animation.FuncAnimation(fig, update_plot, fargs = (fig, scat), frames= 100, interval=100)

plt.show()
"""
r = np.arange(0, 2, 0.01)
theta = 2 * np.pi * r

fig = plt.figure()

ax = fig.add_subplot(111, projection='polar')
#ax.plot(theta, r)
ax.set_rmax(2)
ax.set_rticks([0.5, 1, 1.5, 2])  # less radial ticks
ax.set_rlabel_position(-22.5)  # get radial labels away from plotted line
ax.grid(True)

ax.set_title("A line plot on a polar axis", va='bottom')

scat = plt.plot(theta, r)

anim = animation.FuncAnimation(fig, update_plot, fargs = (fig, scat), frames= 100, interval=100)
#HTML(anim.to_html5_video())

plt.show()