import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import math
import numpy as np
import datetime
from scipy import stats
def plot_cases_per_country(cummulative_data):
    countries = ['Canada', 'US', 'China', 'Taiwan*']
    # plot cumulative cases
    for country in countries:
        plt.plot(cummulative_data['date'], cummulative_data[country])
    plt.legend(countries)
    plt.title("Cumulative Cases over Time")
    plt.xlabel('Date')
    plt.ylabel('Cases')
    plt.yscale('log')
    plt.show()
    plt.savefig('Cumulative-Cases-over-Time.png')
    plt.clf()
def plot_cases_perday_country(cummulative_data):
    countries = ['Canada per day', 'US per day', 'China per day', 'Taiwan* per day']
    # plot cumulative cases
    for country in countries:
        if country == 'US per day':
            continue
        plt.plot(cummulative_data['date'], cummulative_data[country])
    plt.legend(countries)
    plt.title("Cumulative Cases over Time")
    plt.xlabel('Date')
    plt.ylabel('Cases')
    plt.show()
    # plt.savefig('Cumulative-Cases-over-Time.png')
    plt.clf()
def conv_datetime(list):
    lst = []
    for date in list:
        date_lst = []
        date_lst.append(datetime.datetime.strptime(date[0],'%Y-%m-%d'))
        date_lst.append(datetime.datetime.strptime(date[1], '%Y-%m-%d'))
        lst.append(date_lst)
    return lst
def four_bargraphs_range(c_data):
    #countries = ['Canada per day', 'US per day', 'China per day', 'Taiwan* per day']
    countries = ['Canada', 'US', 'China', 'Taiwan*']
    latest_date = ['2020-08-10','2020-08-10']
    range_openings = [['2020-04-1','2020-05-25'],['2020-04-3','2020-06-17'],['2020-01-06','2020-04-08']]
    range_date = conv_datetime(range_openings)
    fig, axs = plt.subplots(nrows=2, ncols=2, constrained_layout=True)
    i = 0
    # Plot Cases per day
    for ax in axs.flat:
        try:
            c_str = countries[i] + ' per day'
            ax.plot(c_data['date'],c_data[c_str])
            ax.set_title(countries[i] + " New Cases per Day")
            ax.set_ylabel("New Cases")
            max = c_data[c_str].max()
            ax.vlines(range_date[i][0], 0, max, colors='r')
            ax.vlines(range_date[i][1], 0, max, colors='r')
        except IndexError:
            break
        i += 1
    plt.show()
    #plt.savefig('Cases-per-day-over-Time.png')
    plt.clf()

    # Find instataneous slope per day
    c_data['Canada_slope'] = c_data['Canada per day'].shift(1,fill_value=0)
    c_data['Canada_slope'] = (c_data['Canada per day']-c_data['Canada_slope'])/c_data['Canada_slope']
    c_data.loc[(c_data.Canada_slope.isnull()) | (c_data.Canada_slope == np.inf), 'Canada_slope']=0
    c_data['US_slope'] = c_data['US per day'].shift(1, fill_value=0)
    c_data['US_slope'] = (c_data['US per day'] - c_data['US_slope']) / c_data['US_slope']
    c_data.loc[(c_data.US_slope.isnull()) | (c_data.US_slope == np.inf), 'US_slope'] = 0
    c_data['China_slope'] = c_data['China per day'].shift(1, fill_value=0)
    c_data['China_slope'] = (c_data['China per day'] - c_data['China_slope']) / c_data['China_slope']
    c_data.loc[(c_data.China_slope.isnull()) | (c_data.China_slope == np.inf), 'China_slope'] = 0
    c_data['Taiwan_slope'] = c_data['Taiwan* per day'].shift(1, fill_value=0)
    c_data['Taiwan_slope'] = (c_data['Taiwan* per day'] - c_data['Taiwan_slope']) / c_data['Taiwan_slope']
    c_data.loc[(c_data.Taiwan_slope.isnull()) | (c_data.Taiwan_slope == np.inf), 'Taiwan_slope'] = 0
    c_data.drop(c_data.head(1).index, inplace=True)

    #create 4 barplots
    fig, axs = plt.subplots(nrows=2, ncols=2, constrained_layout=True)
    i = 0
    for ax in axs.flat:
        try:
            c_str = countries[i] + "_slope"
            rename_str_c = countries[i]+"_slope_closed"
            rename_str_o = countries[i] + "_slope_opened"
            country_iso = c_data[(c_data['date'] > range_date[i][0]) & (c_data['date'] < range_date[i][1])][['date',c_str]].rename(columns={c_str:rename_str_c})
            country_not_iso = c_data[c_data['date'] < range_date[i][0]][['date', c_str]].rename(columns={c_str: rename_str_o})
            c_iso = country_iso[rename_str_c].to_list()
            n_iso = country_not_iso[rename_str_o].to_list()

            tot_size_c = len(c_iso)
            tot_size_o = len(n_iso)
            if tot_size_c > tot_size_o:
                c_iso = c_iso[:tot_size_o]
            else:
                n_iso = n_iso[:tot_size_c]
            print("p-value ",countries[i],stats.wilcoxon(c_iso,n_iso).pvalue)
            country_iso = pd.melt(country_iso)
            country_not_iso = pd.melt(country_not_iso)
            country_data = pd.concat([country_iso, country_not_iso])
            country_data = country_data[country_data['variable'] != 'date']
            ax = sns.boxplot(x="value", y="variable", data=country_data,ax=ax)
        except IndexError:
            break
        except ValueError:
            break
        i += 1
    plt.clf()
def main():
    sns.set()
    cummulative_data = pd.read_csv('cleaned-data.csv',parse_dates=['date'])
    #plot_cases_per_country(cummulative_data)
    plot_cases_perday_country(cummulative_data)
    #four_bargraphs_range(cummulative_data)
if __name__ == '__main__':
    main()