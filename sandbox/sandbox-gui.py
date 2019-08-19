import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox
import random
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)
t = np.arange(-2.0, 2.0, 0.001)
s = t ** 2
initial_text = "t ** 2"
l, = plt.plot(t, s, lw=2)

# Default parameters

sample_size = 10000  # number of trades
winrate = 0.50  # strategy win rate

# Risk:Reward Ratio, one or the other must be 1 for best practice. its relative ;)
risk = 1
reward = 1


def run_sim(winrate=winrate, risk=risk, reward=reward, sample_size=sample_size):
    equity = 0
    equity_curve = []
    for i in range(0, sample_size):
        if random.uniform(0.0, 1.0) <= winrate:
            equity += (reward)
        else:
            equity -= (risk)

        equity_curve.append(equity)
    return equity_curve

def submit(bip):
    ydata = eval(bip)
    l.set_ydata(ydata)
    ax.set_ylim(np.min(ydata), np.max(ydata))
    plt.draw()

axbox = plt.axes([0.1, 0.05, 0.8, 0.075])
text_box = TextBox(axbox, 'Evaluate', initial=initial_text)
text_box.on_submit(submit)

plt.show()