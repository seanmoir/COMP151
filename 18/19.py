import pandas as pd
import matplotlib.pyplot as plt

#input file
in_file = pd.read_csv('renewable-energy-stock-account-2007-18.csv')

energy_types = in_file[(in_file['resource'] != "Total generation") & (in_file['resource'] != "Renewable")]["resource"].unique()
years = in_file['year'].unique()

#for e in energy_types:
#    print(e + " -- " + str(in_file[(in_file["resource"] == e) & (in_file["variable"] == "Generation")]["data_value"].sum()))
#
#print("\n")
#
#for y in years:
#    print(str(y) + " -- " + str(in_file[(in_file["year"] == y) & (in_file["variable"] == "Generation")]["data_value"].sum()))
#
#print("\n")
#
#for e in energy_types:
#    print(e + " -- " + str(in_file[(in_file["resource"] == e) & (in_file["variable"] == "Generation")]["data_value"].mean()))
#
energy_types_df = pd.DataFrame(index=years, columns=energy_types)
for e in energy_types:
    energy_types_df[e] = in_file[(in_file["resource"] == e) & (in_file["variable"] == "Generation")]['data_value'].values
    #print(energy_types_df[e])
energy_types_df.plot(kind='bar', figsize=(10,6), ylim=(0,30000))
# this fixes problems with the legend
plt.legend(ncol=4)
plt.show()

energy_types_df.plot(kind='box', figsize=(10,6), ylim=(0,30000))
plt.show()