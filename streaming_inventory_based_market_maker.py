import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- Figure 1 ---
fig, ax = plt.subplots()
xdata, ydata = [], []
(ln,) = ax.plot([], [], 'ro')
ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1, 1)

ax.set_title("Mid Price")

def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    ln.set_data(xdata, ydata)
    return ln,

ani0 = FuncAnimation(fig, update,
                     frames=np.linspace(0, 2*np.pi, 128),
                     blit=False, interval=30)

# --- Figure 2 ---
fig1, ax1 = plt.subplots()
xdata1, ydata1 = [], []
(ln1,) = ax1.plot([], [], 'ro')
ax1.set_xlim(0, 2*np.pi)
ax1.set_ylim(-1, 1)

ax1.set_title("Inventory")

def update1(frame):
    xdata1.append(frame)
    ydata1.append(np.sin(frame))
    ln1.set_data(xdata1, ydata1)
    return ln1,

ani1 = FuncAnimation(fig1, update1,
                     frames=np.linspace(0, 2*np.pi, 128),
                     blit=False, interval=30)

# keep references alive
anims = [ani0, ani1]

plt.show()