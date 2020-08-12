# COVID-19 Project

## Library used

    import glob, seaborn
    import pandas as pd, matplotlib.pyplot as plt
    import matplotlib.ticker as ticker
    from scipy import stats

## Code description

1. [analyze_flight.py](./analyze_flight.py) 
    
    Description: Analyze relationship between number of flights and COVID-19 Cases
    
    * Expect output files in current folder:
        * newly_added_infection.csv
    * Expect output files in [flight_and_infection_picture](./flight_and_infection_picture) folder:
        * num_flights_arrived_each_day.png
        * new_infections_detected_at_each_day.png
        * analyzed_picture.png
    * Expect output: None
    
2. [analyze_mask_usage.py](./analyze_mask_usage.py)
    
    Description: Analyze relationship between mask usage and number of COVID-19 infections in United States and mask usage in country (with FIPS code) of United States
    
    * Expect output files in [mask_analyze_picture](./mask_analyze_picture) folder:
        * percentage_infected_vs_mask_usage.png
    * Expect output:
        * pvalue for Chi-Square Test

3. [analyze_rates.py](./analyze_mask_usage.py)
    Description: Analyzes the rates of new cases of COVID-19 in countries Canada, US, China, Taiwan
    * Expect output files in [rates_picture](./rates_picture) folder:
        * Cumulative-Cases-over-Time.png
        * Cases-per-day-over-Time.png
    * Expect output:
        * pvalue for Wilcoxon signed-rank test for Canada and US
    ## Order of execution
1. [transform_data.py](./transform_data.py)
2. [analyze_flight.py](./analyze_flight.py)
3. [analyze_mask_usage.py](./analyze_mask_usage.py)
4. [analyze_rates.py](./analyze_rates.py)

Note: No need to pass any arguments, just run the code by
    
    python3 fileName.py

## Group member
Henry

Piercson

## Source of our datasets
1. Novel Coronavirus (COVID-19) Cases Data (Jan 22 to August 10):
    
    https://data.humdata.org/dataset/novel-coronavirus-2019-ncov-cases
    
2. Flights Data across the world:
    
    https://opensky-network.org/datasets/covid-19/

3. Country Codes ALPHA-2 & ALPHA-3:

    https://www.iban.com/country-codes

4. Airport Codes:
    
    https://github.com/datasets/airport-codes/blob/master/data/airport-codes.csv

5. Mask-Wearing Survey Data:
    
    https://github.com/nytimes/covid-19-data/tree/master/mask-use

6. 2019 Population Estimates from the US Census Bureau
    
    https://github.com/kingaa/covid-19-data/blob/master/pop_est_2019.csv

## Other references

=======
###CANADA
* https://www.fasken.com/en/knowledge/2020/04/1-covid-19-government-orders-closing-businesses/
Ontario, Québec, Alberta, Manitoba and Saskatchewan
closing non-essential or non-priority businesses March 30th

* https://www.dentons.com/en/insights/alerts/2020/march/30/closure-of-non-essential-businesses-in-british-columbia-alberta-ontario-and-quebec
BC anounces list of essential services as of March 26th

* https://biv.com/article/2020/04/bc-courts-suspend-non-essential-operations
BC court susends non-essential operations on April 1st
* https://www.retailcouncil.org/coronavirus-info-for-retailers/can-my-business-open/
Lasest reopen date is May 25th
###US
* https://abcnews.go.com/Health/states-shut-essential-businesses-map/story?id=69770806
US 46 states with non-essential closures at April 3rd
* https://www.usnews.com/news/articles/2020-05-18/the-statistical-support-for-closing-non-essential-businesses-during-the-coronavirus-pandemic
"Between March 17 and April 3, amid rising fears and coronavirus case counts, governors of 34 states mandated statewide closures of non-essential businesses"
* https://www.nbcnews.com/news/us-news/reopening-america-see-what-states-across-u-s-are-starting-n1195676
June 17th latest parial reopening
###TAIWAN
* https://www.worldaware.com/covid-19-alert-taiwan-begins-reopening-nonessential-businesses-major-cities-amid-entry-ban-social
REOPENS on May 20
* https://healthpolicy.fsi.stanford.edu/news/how-taiwan-used-big-data-transparency-central-command-protect-its-people-coronavirus
interesting read, Taiwan used BIG DATA to solve cases
* https://www.taiwannews.com.tw/en/news/3913133
Says not reached the stage that city lockdowns are necessary 

###China 
* http://www.mnw.cn/news/shehui/2244783.html
Januaray 6th
* http://www.chinanews.com/gn/2020/03-24/9136252.shtml
REOPENS Cities other than WuHan reopend at Mar 25
    Wuhan reopened after April 8th



