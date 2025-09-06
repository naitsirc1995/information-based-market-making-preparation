import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Market_depth_table.csv")

plt.scatter(df["bid_price"],df["total_demand"],label='demand',marker='x')

plt.scatter(df["ask_price"],df["total_supply"],label='supply',marker='^')

plt.legend()

plt.show()