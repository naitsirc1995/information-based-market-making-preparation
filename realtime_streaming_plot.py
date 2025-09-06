# real-time streaming plot (matplotlib)
import numpy as np
import matplotlib.pyplot as plt

fps = 5

plt.ion()
fig, ax = plt.subplots()
(line,) = ax.plot([], [], linewidth=2)
ax.set_xlabel("t")
ax.set_ylabel("value")

x, y = [], []
for t in range(300):                         # simulate incoming data
    x.append(t)
    y.append(np.sin(0.1 * t) + 0.2*np.random.randn())

    line.set_data(x, y)
    ax.relim()                               # recompute limits
    ax.autoscale_view()                      # rescale to new data
    plt.pause(1/fps)                          # small delay to show the update

plt.ioff()
plt.show()
