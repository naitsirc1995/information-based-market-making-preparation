import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

num_trades = 100
int_btw_frm = 200

def simulate_market_maker(trades=100, seed=None):
    rng = np.random.default_rng(seed)
    bid = np.zeros(trades + 1, dtype=int)
    ask = np.zeros(trades + 1, dtype=int)
    mid = np.zeros(trades + 1, dtype=float)
    inv = np.zeros(trades + 1, dtype=int)
    sides = np.zeros(trades, dtype=int)

    bid[0], ask[0] = 99, 101
    mid[0] = 0.5 * (bid[0] + ask[0])

    for t in range(trades):
        side = 1 if rng.random() < 0.5 else -1
        sides[t] = side
        if side == 1:
            inv[t + 1] = inv[t] + 1
            bid[t + 1] = bid[t] - 1
            ask[t + 1] = ask[t] - 1
        else:
            inv[t + 1] = inv[t] - 1
            bid[t + 1] = bid[t] + 1
            ask[t + 1] = ask[t] + 1
        mid[t + 1] = 0.5 * (bid[t + 1] + ask[t + 1])

    return {"bid": bid, "ask": ask, "mid": mid, "inventory": inv, "sides": sides}

res = simulate_market_maker(num_trades, seed=0)
mid = res["mid"]
inv = res["inventory"]
frames = np.arange(num_trades + 1)

# --- Figure 1: Asset Price ---
fig, ax = plt.subplots()
(ln,) = ax.plot([], [], 'g-')
ax.set_title("Asset Price")
ax.set_xlim(0, num_trades)
ax.set_ylim(mid.min(), mid.max())

def init_asset():
    ln.set_data([], [])
    return ln,

def update_asset(i):
    ln.set_data(frames[:i+1], mid[:i+1])
    return ln,

ani0 = FuncAnimation(
    fig, update_asset, frames=frames, init_func=init_asset,
    blit=True, interval=int_btw_frm, repeat=False, cache_frame_data=False
)

# --- Figure 2: Inventory ---
fig1, ax1 = plt.subplots()
(ln1,) = ax1.plot([], [], 'b-')
ax1.set_title("Inventory")
ax1.set_xlim(0, num_trades)
ax1.set_ylim(inv.min(), inv.max())

def init_inv():
    ln1.set_data([], [])
    return ln1,

def update_inv(i):
    ln1.set_data(frames[:i+1], inv[:i+1])
    return ln1,

ani1 = FuncAnimation(
    fig1, update_inv, frames=frames, init_func=init_inv,
    blit=True, interval=int_btw_frm, repeat=False, cache_frame_data=False
)

anims = [ani0, ani1]  # keep refs alive
plt.show()