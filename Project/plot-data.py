import matplotlib.pyplot as plt
import pandas as pd
import math
import numpy as np
def main():
    pop_countries = [37773215,331187544,1439858499,23820964]
    cummulative_data = pd.read_csv('cleaned-data.csv',parse_dates=['date'])
    countries = ['Canada','US','China','Taiwan*']
    # plot cumulative cases
    for country in countries:
        plt.plot(cummulative_data['date'],cummulative_data[country])
    plt.legend(countries)
    plt.title("Cumulative Cases over Time")
    plt.xlabel('Date')
    plt.ylabel('Cases')
    plt.yscale('log')
    plt.show()
    plt.clf()
    # plot cumulative cases as percentage of population
    i = 0
    for country in countries:
        plt.plot(cummulative_data['date'],cummulative_data[country]/pop_countries[i])
        i += 1
    plt.legend(countries)
    plt.title("Percentage Cumulative Cases over Time")
    plt.xlabel('Date')
    plt.ylabel('Percentage Population Cases')
    #plt.yscale('log')
    plt.show()
    plt.clf()
    plt.plot(cummulative_data['date'],cummulative_data['China'])
    plt.show()

    #plt.savefig('Cumulative-Cases-over-Time.png')
if __name__ == '__main__':
    main()