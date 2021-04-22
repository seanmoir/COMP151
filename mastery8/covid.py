import doctest
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('effects-of-covid-19-on-trade.csv')

years = data['Year'].unique()
directions = data['Direction'].unique()
days = data['Weekday'].unique()

for d in directions:
    for y in years:
        print(str(d) + " " + str(y) + " " + str(data[(data['Year'] == y) & (data['Direction'] == d)]["Value"].mean()))

print("\n\n")

for y in years:
    for d in days:
        print(str(y) + " " + str(d) + " " + str(data[(data['Year'] == y) & (data['Weekday'] == d)]["Value"].mean()))

print("\n\n")

for y in years:
    for d in days:
        print(str(y) + " " + str(d) + " " + str(data[(data['Year'] == y) & (data['Weekday'] == d)]["Value"].mean()))
    
total_trade_df = pd.DataFrame(index=years, columns=["Sum"])
for y in years:
    total_trade_df.loc[y] = data[data["Year"] == y]['Value'].sum()
total_trade_df.plot(kind='bar', figsize=(10,6), ylim=(0,600000000000))
plt.show()

total_trade_df = pd.DataFrame(index=years, columns=directions)
for d in directions:
    for y in years:
        total_trade_df[d].loc[y] = data[(data['Year'] == y) & (data["Direction"] == d)]['Value'].sum()
total_trade_df.plot(kind='bar', figsize=(10,6), ylim=(0,300000000000))
plt.show()

total_trade_df = pd.DataFrame(index=years, columns=days)
for d in days:
    for y in years:
        total_trade_df[d].loc[y] = data[(data['Year'] == y) & (data['Weekday'] == d)]['Value'].sum()
total_trade_df.plot(kind='bar', figsize=(10,6), ylim=(0,100000000000))
plt.show()

