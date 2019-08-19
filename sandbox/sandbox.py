import random
import matplotlib.pyplot as plt
import numpy as np
import time

# Default parameters

sample_size = 10000  # number of trades
winrate = 0.5  # strategy win rate

# Risk:Reward Ratio, one or the other must be 1 for best practice. its relative ;)
risk = 1
reward = 1


def run_sim(winrate=winrate, risk=risk, reward=reward, sample_size=sample_size, seed=time.clock()):
    equity = 0
    equity_curve = []
    for i in range(0, sample_size):
        if random.uniform(0.0, 1.0) <= winrate:
            equity += (reward)
        else:
            equity -= (risk)

        equity_curve.append(equity)
    return equity_curve


# Plot the simulation
def plot_sim(sim):
    xaxis = [i for i in range(len(sim))]
    plt.plot(xaxis, sim)
    fig, ax = plt.subplots()
    ax.fill(xaxis, sim)
    ax.grid(True, zorder=5)
    plt.show()


plot_sim(run_sim())


