from sandbox import run_sim
import matplotlib.pyplot as plt
import time


def run_race(winrate, risk, reward, sample_size, racers):
    results = []
    for i in range(0, racers):
        sim = run_sim(winrate, risk, reward, sample_size)
        results.append(sim)
        print(sim[-1])

    print(results)
    return results


def stdev(data):
    plt.hist(data)
    plt.show()

stdev(run_race(0.5, 1,1, 100, 250))