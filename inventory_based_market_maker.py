import numpy as np
import matplotlib.pyplot as plt

def simulate_market_maker(trades=100, seed=None):
    """
    Inventory-based market making per rules:
      - start bid/ask = 99/101 (2-tick spread)
      - trades are unit sized
      - after a BUY (we buy one unit), lower both quotes by 1
      - after a SALE (we sell one unit), raise both quotes by 1

    Returns dict with arrays: bid, ask, mid, inventory, sides (+1 buy, -1 sale).
    """
    rng = np.random.default_rng(seed)
    bid = np.zeros(trades + 1, dtype=int)
    ask = np.zeros(trades + 1, dtype=int)
    mid = np.zeros(trades + 1, dtype=float)
    inv = np.zeros(trades + 1, dtype=int)
    sides = np.zeros(trades, dtype=int)

    # initial quotes 99/101
    bid[0], ask[0] = 99, 101
    mid[0] = 0.5 * (bid[0] + ask[0])

    for t in range(trades):
        side = 1 if rng.random() < 0.5 else -1   # +1 = we buy; -1 = we sell
        sides[t] = side

        if side == 1:
            # we buy one; move both quotes down by 1
            inv[t + 1] = inv[t] + 1
            bid[t + 1] = bid[t] - 1
            ask[t + 1] = ask[t] - 1
        else:
            # we sell one; move both quotes up by 1
            inv[t + 1] = inv[t] - 1
            bid[t + 1] = bid[t] + 1
            ask[t + 1] = ask[t] + 1

        mid[t + 1] = 0.5 * (bid[t + 1] + ask[t + 1])

    return {"bid": bid, "ask": ask, "mid": mid, "inventory": inv, "sides": sides}

if __name__ == "__main__":
    # three sample paths
    for i, s in enumerate([7, 13, 29], start=1):
        res = simulate_market_maker(trades=100, seed=s)
        plt.figure()
        plt.plot(range(len(res["mid"])), res["mid"])
        plt.title(f"Sample Mid-Price Path ({i})")
        plt.xlabel("Trade")
        plt.ylabel("Mid-Price")
        plt.tight_layout()
    plt.show()
