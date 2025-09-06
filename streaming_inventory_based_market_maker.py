import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

num_trades = 100
int_btw_frm = 400

def simulate_market_maker(trades=100, seed=None):
    rng = np.random.default_rng(seed)
    bid = np.zeros(trades + 1, dtype=int)
    ask = np.zeros(trades + 1, dtype=int)
    mid = np.zeros(trades + 1, dtype=float)
    inv = np.zeros(trades + 1, dtype=int)
    sides = np.zeros(trades, dtype=int)
    pnl = np.zeros(trades+1,dtype=float)
    cash = 0.0

    bid[0], ask[0] = 99, 101
    mid[0] = 0.5 * (bid[0] + ask[0])
    pnl[0] = cash + inv[0]*mid[0]

    for t in range(trades):
        side = 1 if rng.random() < 0.5 else -1
        sides[t] = side
        if side == 1:
            trade_px = bid[t]
            cash -= trade_px
            inv[t + 1] = inv[t] + 1
            bid[t + 1] = bid[t] - 1
            ask[t + 1] = ask[t] - 1
            pnl[t+1] = cash + (-1)*side*mid[t]
        else:
            trade_px = ask[t]
            cash += trade_px
            inv[t + 1] = inv[t] - 1
            bid[t + 1] = bid[t] + 1
            ask[t + 1] = ask[t] + 1
            pnl[t+1] = cash + (-1)*side*mid[t]

        mid[t + 1] = 0.5 * (bid[t + 1] + ask[t + 1])

        pnl[t+1] = cash + inv[t+1]*mid[t+1]

    return {"bid": bid, "ask": ask, "mid": mid, "inventory": inv, "sides": sides,"pnl":pnl}

res = simulate_market_maker(num_trades)
mid = res["mid"]
inv = res["inventory"]
pnl = res["pnl"]

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


# --- Figure 3: PnL ---
fig2, ax2 = plt.subplots()
(ln2,) = ax2.plot([], [], 'k-')
ax2.set_title("pnl")
ax2.set_xlim(0, num_trades)
ax2.set_ylim(pnl.min(), pnl.max())

def init_pnl():
    ln2.set_data([], [])
    return ln2,

def update_pnl(i):
    ln2.set_data(frames[:i+1], pnl[:i+1])
    return ln2,

ani2 = FuncAnimation(
    fig2, update_pnl, frames=frames, init_func=init_pnl,
    blit=True, interval=int_btw_frm, repeat=False, cache_frame_data=False
)


anims = [ani0, ani1,ani2]  # keep refs alive
plt.show()