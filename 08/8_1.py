import pandas as pd

in_file = pd.read_csv('greenhouse-gas-emissions.csv')
#in_file.to_excel('greenhouse-gas-emissions.xlsx', sheet_name="By region")
#print(in_file["anzsic_descriptor"].unique())
#print(in_file[in_file["anzsic_descriptor"] == "Households"])
data = in_file[(in_file["anzsic_descriptor"] == "Households") & (in_file["year"] >= 2007) & (in_file["year"] <= 2018)]
print(sum(data['data_val']))

data = in_file[(in_file["anzsic_descriptor"] == "Households") & (in_file["year"] == 2007)]
print(data['data_val'].sum())