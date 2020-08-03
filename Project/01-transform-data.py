import pandas as pd
def main():
    og_data = pd.read_csv('time_series_covid19_confirmed_global.csv')
    print(og_data)
    # want countries Canada, US, China, and Taiwan
    countries_data = og_data[(og_data['Country/Region'] == 'Canada')\
                            | (og_data['Country/Region'] == 'US')\
                            | (og_data['Country/Region'] == 'China')\
                            | (og_data['Country/Region'] == 'Taiwan*')]
    print(countries_data)
    # want to transform the df to have rows as dates
    cleaned_country_cases = countries_data.drop(['Lat','Long','Province/State'],axis=1).T
    cleaned_country_cases.to_csv('cleaned-data.csv')
    return 1
if __name__ == '__main__':
    main()