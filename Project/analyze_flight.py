import glob, seaborn
import pandas as pd, matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from scipy import stats


def get_flight_date():
    # flightList = pd.read_csv("Test.csv.gz",parse_dates=["firstseen", "lastseen", "day"])
    myGroupedData = [pd.read_csv(filename, parse_dates=["firstseen", "lastseen", "day"])
                     for filename in glob.glob("./flight_status/*.csv.gz")]
    flightList = pd.concat(myGroupedData, axis=0, ignore_index=True)
    country_code = pd.read_csv("airport-codes.csv")

    print(flightList.shape)
    country_code = country_code[['ident', 'iso_country']]
    flightList = flightList[['callsign', 'origin', 'destination', 'day']]
    flightList = flightList.dropna(subset=['destination']) # get rid of rows where destination is null value
    flightList['day'] = flightList['day'].dt.strftime('%Y-%m-%d')
    print(flightList.shape)
    # Join two tables so we can know the country of destination
    flightList = flightList.merge(country_code, left_on=['destination'],
                                  right_on=['ident']).drop(columns=['ident'])

    # separate the table into 4 different countries
    flightListUS = flightList.loc[(flightList['iso_country'] == 'US')]\
        .sort_values(by=['day'], ascending=True)

    # get number of flight a country has for each day
    flightListUS = flightListUS.groupby('day').count().rename(
        columns={'iso_country': 'count'})[['count']].reset_index()
    flightListCN = flightList.loc[(flightList['iso_country'] == 'CN')]\
        .sort_values(by=['day'], ascending=True)
    flightListCN = flightListCN.groupby('day').count().rename(
        columns={'iso_country': 'count'})[['count']].reset_index()
    flightListTW = flightList.loc[(flightList['iso_country'] == 'TW')]\
        .sort_values(by=['day'], ascending=True)
    flightListTW = flightListTW.groupby('day').count().rename(
        columns={'iso_country': 'count'})[['count']].reset_index()
    flightListCA = flightList.loc[(flightList['iso_country'] == 'CA')]\
        .sort_values(by=['day'], ascending=True)
    flightListCA = flightListCA.groupby('day').count().rename(
        columns={'iso_country': 'count'})[['count']].reset_index()

    flightListUS.to_csv('./cleaned_flight_data/US_flight_info.csv')
    flightListCA.to_csv('./cleaned_flight_data/CA_flight_info.csv')
    flightListTW.to_csv('./cleaned_flight_data/TW_flight_info.csv')
    flightListCN.to_csv('./cleaned_flight_data/CN_flight_info.csv')
    ax = plt.subplot(1, 1, 1)
    plt.plot(flightListUS['day'], flightListUS['count'])
    plt.plot(flightListCA['day'], flightListCA['count'])
    plt.plot(flightListTW['day'], flightListTW['count'])
    plt.plot(flightListCN['day'], flightListCN['count'])
    plt.legend(['US','CA','TW','CN'])
    # plt.legend(['CA','TW','CN'])
    # locator = ticker.MaxNLocator(nbins=10) # with 3 bins you will have 4 ticks
    # ax.xaxis.set_major_locator(locator)
    # plt.xticks(rotation=10)
    ax.set_xticks(['2020-01-01', '2020-02-01', '2020-03-01', '2020-04-01', '2020-05-01'])
    plt.xlabel('Date')
    plt.ylabel('# flights arrived')
    plt.title('# flights arrived at each day from January to May')
    plt.show()

def get_infection_data():
    infection = pd.read_csv('time_series_covid19_confirmed_global.csv')
    infection = infection.loc[(infection['Country/Region'] == 'China') |
                              (infection['Country/Region'] == 'Canada') |
                              (infection['Country/Region'] == 'US') |
                              (infection['Country/Region'] == 'Taiwan*')]\
        .drop(columns=['Province/State', 'Lat', 'Long'])
    infection = infection.groupby('Country/Region').sum()
    infection = infection.T
    infection['CanadaS'] = infection['Canada'].shift(1)
    infection['ChinaS'] = infection['China'].shift(1)
    infection['USS'] = infection['US'].shift(1)
    infection['TaiwanS'] = infection['Taiwan*'].shift(1)
    infection = infection.fillna(0)
    infection['Canada'] = infection['Canada'] - infection['CanadaS']
    infection['China'] = infection['China'] - infection['ChinaS']
    infection['Taiwan'] = infection['Taiwan*'] - infection['TaiwanS']
    infection['US'] = infection['US'] - infection['USS']
    infection = infection[['China', 'Taiwan', 'US', 'Canada']]
    infection.index.names = ['Date']
    infection = infection.reset_index()
    infection['Date'] = pd.to_datetime(infection['Date'])
    infection = infection.sort_values(by=['Date'], ascending=True)
    infection = infection.loc[infection['Date'] <= pd.to_datetime('2020-05-31')]

    CNmean = infection['China'].mean()
    infection.loc[infection.China > 10000, 'China'] = CNmean
    infection.to_csv('./newly_added_infection.csv')

    ax = plt.subplot(1, 1, 1)
    # plt.plot(infection['Date'], infection['US'])
    plt.plot(infection['Date'], infection['Canada'])
    plt.plot(infection['Date'], infection['Taiwan'])
    plt.plot(infection['Date'], infection['China'])
    # plt.legend(['US','CA','TW','CN'])
    plt.legend(['CA', 'TW', 'CN'])
    # ax.set_xticks(['2020-02-01', '2020-03-01', '2020-04-01', '2020-05-01'])
    locator = ticker.MaxNLocator(nbins=10) # with 3 bins you will have 4 ticks
    ax.xaxis.set_major_locator(locator)
    plt.xticks(rotation=25)
    plt.xlabel('Date')
    plt.ylabel('New infections detected')
    plt.title('New infections detected at each day')
    # plt.show()

def analyze_data():
    myFlightData = []
    myValues = ['US', 'Canada', 'China', 'Taiwan']
    infectionData = pd.read_csv('newly_added_infection.csv', parse_dates=['Date'], index_col=0)
    myFlightData.append(pd.read_csv('./cleaned_flight_data/US_flight_info.csv', parse_dates=['day'], index_col=0))
    myFlightData.append(pd.read_csv('./cleaned_flight_data/CA_flight_info.csv', parse_dates=['day'], index_col=0))
    myFlightData.append(pd.read_csv('./cleaned_flight_data/CN_flight_info.csv', parse_dates=['day'], index_col=0))
    myFlightData.append(pd.read_csv('./cleaned_flight_data/TW_flight_info.csv', parse_dates=['day'], index_col=0))

    plt.figure(figsize=(12, 12))

    for n in range(len(myFlightData)):
        singleData = myFlightData[n]
        singleData = singleData.loc[
            (singleData['day'] >= pd.to_datetime('2020-01-22'))
            & (singleData['day'] <= pd.to_datetime('2020-05-31'))
        ].reset_index()
        reg = stats.linregress(singleData['count'], infectionData[myValues[n]])
        print('pvalue for %s is:' %(myValues[n]), end='')
        print(reg.pvalue)

        # residual
        # plt.subplot(2,2,n+1)
        # residuals = infectionData[myValues[n]] - (singleData['count']*reg.slope+reg.intercept)
        # plt.hist(residuals)
        # plt.xlabel('Residual')
        # plt.ylabel('# Data Points')
        # plt.title(myValues[n], fontdict={'fontsize':30})

        # graph with data points and best fit line
        plt.subplot(2,2,n+1)
        plt.plot(singleData['count'], infectionData[myValues[n]], '.', alpha=0.7)
        plt.plot(singleData['count'],
                 singleData['count']*reg.slope+reg.intercept, 'r-', linewidth=3)
        plt.xlabel('# flights arrived')
        plt.ylabel('# newly added infections')
        plt.legend(['Data Points', 'Best Fit Line'])
        plt.title(myValues[n])
        plt.title(myValues[n], fontdict={'fontsize': 30})

    # plt.show()
    plt.savefig('./flight_and_infection_picture/analyzed_picture.png')
    # plt.savefig('./flight_and_infection_picture/analyzed_picture_residuals.png')

def main():
    seaborn.set()
    get_flight_date()
    get_infection_data()
    analyze_data()

if __name__ == '__main__':
    main()