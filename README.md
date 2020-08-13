# COVID-19 Project

## Library used

    import glob, seaborn
    import pandas as pd, matplotlib.pyplot as plt
    import matplotlib.ticker as ticker
    from scipy import stats

## Code description

1. [analyze_rates.py](./analyze_mask_usage.py)
    
    Description: Analyzes the rates of new cases of COVID-19 in countries Canada, US, China, Taiwan
    
    * Expect output files in [rates_picture](./rates_picture) folder:
        * Cumulative-Cases-over-Time.png
        * Cases-per-day-over-Time.png
    * Expect output:
        * pvalue for Wilcoxon signed-rank test for Canada and US

2. [analyze_flight.py](./analyze_flight.py) 
    
    Description: Analyze relationship between number of flights and COVID-19 Cases
    
    * Expected output files in current folder:
        * newly_added_infection.csv
    * Expected output files in [flight_and_infection_picture](./flight_and_infection_picture) folder:
        * num_flights_arrived_each_day.png
        * new_infections_detected_at_each_day.png
        * analyzed_picture.png
    * Expect output: None
    
3. [analyze_mask_usage.py](./analyze_mask_usage.py)
    
    Description: Analyze relationship between mask usage and number of COVID-19 infections in United States and mask usage in country (with FIPS code) of United States
    
    * Expected output files in [mask_analyze_picture](./mask_analyze_picture) folder:
        * percentage_infected_vs_mask_usage.png
    * Expected output:
        * pvalue for Chi-Square Test
        
## Order of execution

1. [transform_data.py](./transform_data.py)
2. [analyze_rates.py](./analyze_rates.py)
3. [analyze_flight.py](./analyze_flight.py)
4. [analyze_mask_usage.py](./analyze_mask_usage.py)

Note: No need to pass any arguments, just run the code by
    
    python3 file_name.py

## Group member
- Henry

- Piercson

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
