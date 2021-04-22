import doctest
import pandas as pd
import matplotlib.pyplot as plt

months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']

def mean_temp(filename, start_year, end_year):
    """
    >>> mean_temp('Tara_Hills_temp.csv', 1950, 1960)
    JAN mean = 15.895555555555555
    FEB mean = 15.559999999999999
    MAR mean = 13.391111111111112
    APR mean = 9.724444444444446
    MAY mean = 5.267777777777777
    JUN mean = 2.6755555555555555
    JUL mean = 1.2999999999999998
    AUG mean = 3.8075000000000006
    SEP mean = 7.501111111111111
    OCT mean = 9.7
    NOV mean = 12.155555555555557
    DEC mean = 14.190000000000001
    >>> mean_temp('Tara_Hills_temp.csv', 1990, 1999)
    JAN mean = 16.15857142857143
    FEB mean = 15.89375
    MAR mean = 12.185714285714287
    APR mean = 9.087142857142856
    MAY mean = 6.2
    JUN mean = 2.9957142857142856
    JUL mean = 2.588
    AUG mean = 4.202500000000001
    SEP mean = 6.9087499999999995
    OCT mean = 9.867142857142857
    NOV mean = 11.46375
    DEC mean = 14.168571428571429
    """
    in_file = pd.read_csv('Tara_Hills_Temp.csv')
    data = in_file[(in_file['YEAR'] > start_year) & (in_file['YEAR'] < end_year)]
    for month in months:
        print(month + " mean = " + str(data[month].mean()))


def mean_temp2(filename, year, start_month, end_month):
    """
    >>> mean_temp2('Tara_Hills_temp.csv', 1950, 'FEB', 'JUN')
    8.97
    >>> mean_temp2('Tara_Hills_temp.csv', 1973, 'SEP', 'DEC')
    11.5175
    """
    in_file = pd.read_csv('Tara_Hills_Temp.csv')
    data = in_file[in_file['YEAR'] == year]
    months_mod = []
    for i in range(len(months)):
        if(i >= months.index(start_month) and i <= months.index(end_month)):
            months_mod.append(months[i])
    print(data[months_mod].mean(axis = 1).values[0])

    
if __name__ == '__main__':
    doctest.testmod(verbose=True)