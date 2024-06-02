import pandas as pd
import matplotlib.pyplot as plt


def getGraph():
    name = ['IDLI', 'DOSA', 'WADA', 'VEG \n BIRYANI', 'CHICKEN \n BIRYANI', 'PANEER \n TIKKA', 'CHICKEN \n TIKKA']
    RATE = [30, 40, 40, 120, 160, 150, 190]
    plt.bar(name, RATE , color='b')
    plt.xlabel("DISHES", color='r')
    plt.ylabel("RATE", color='r')
    plt.title("DISH AND RATES")
    plt.figsize=(6,2)
    plt.ylim(0, 200)
    plt.grid()
    ax = plt.gca()
    ax.set_facecolor('xkcd:cyan')
    plt.show()