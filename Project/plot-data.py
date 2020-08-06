import matplotlib.pyplot as plt
import pandas as pd
import math
import numpy as np
def main():
    cummulative_data = pd.read_csv('cleaned-data.csv',parse_dates=['date'])
    countries = ['Canada','US','China','Taiwan*']
    for country in countries:
        plt.plot(cummulative_data['date'],cummulative_data[country])
    plt.legend(countries)
    plt.title("Cumulative Cases over Time")
    plt.xlabel('Date')
    plt.ylabel('Cumulative Cases')
    plt.yscale('symlog')
    plt.savefig('Cumulative-Cases-over-Time.png')
if __name__ == '__main__':
    main()