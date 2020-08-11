import glob, seaborn
import pandas as pd, matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from scipy import stats

def get_mask_data():
    maskData = pd.read_csv('mask-use-by-county.csv')
    infectionData = pd.read_csv('us-counties_July_9th.csv')
    populationData = pd.read_csv('pop_est_2019.csv')

    populationData = populationData.loc[populationData['fips'].str.isdigit() == True]
    populationData = populationData.astype({'fips': 'int64'})
    infectionData = infectionData[['fips','confirmed_cases']]
    infectionData = infectionData.dropna(subset=['confirmed_cases', 'fips'])
    infectionData = infectionData.astype({'fips': 'int64', 'confirmed_cases': 'int64'})
    maskData['total'] = maskData['FREQUENTLY'] + maskData['ALWAYS']
    maskData = maskData[['COUNTYFP','total']]

    infectionData = infectionData.merge(populationData, left_on=['fips'],
                                        right_on=['fips'])
    infectionData['populationRate'] = infectionData['confirmed_cases'] / infectionData['population']
    infectionData = infectionData.merge(maskData, left_on=['fips'],
                                        right_on=['COUNTYFP']).drop(columns=['COUNTYFP'])

    plt.plot(infectionData['populationRate'], infectionData['total'], '.')
    plt.xlabel('Percentage people infected')
    plt.ylabel('Percentage people wearing mask')
    plt.title('Relationship between percentage of infected people \n and percentage of people who wear mask')
    plt.show()

def chi_square_on_mask_usage():
    maskData = pd.read_csv('mask-use-by-county.csv')
    populationData = pd.read_csv('pop_est_2019.csv')

    populationData = populationData.loc[populationData['fips'].str.isdigit() == True]
    populationData = populationData.astype({'fips': 'int64'})
    maskData = maskData.merge(populationData, left_on=['COUNTYFP'], right_on=['fips'])
    maskData = maskData.dropna(subset=['population'])
    maskData = maskData.mul(maskData['population'], axis=0)
    maskData = maskData[['NEVER', 'RARELY', 'SOMETIMES', 'FREQUENTLY', 'ALWAYS']]
    maskData = maskData.astype('int64')

    chi2, p, dof, expected = stats.chi2_contingency(maskData)

    print('pvalue is: ', p)

def main():
    seaborn.set()
    get_mask_data()
    chi_square_on_mask_usage()

if __name__ == '__main__':
    main()