import pandas as pd
import matplotlib.pyplot as plt

# Load the data
gini = pd.read_csv('Data\Gini Coefficient.csv', encoding='cp949')

# Filter selected countries
selected_countries = ['대한민국', '일본', '캐나다', '미국', '프랑스', '독일', '영국']
selected_data = gini[gini['국가별'].isin(selected_countries)]
selected_data.replace('-', 0)
print(selected_data)
#print(selected_data)
# Remove rows with "-" values
#selected_data = selected_data.replace('-', pd.NA).dropna()

# Set up the figure and plot
plt.figure(figsize=(10, 5))
years = ['2017', '2018', '2019', '2020', '2021']

for country in selected_countries:
    country_data = selected_data[selected_data['국가별'] == country]
    print(type(country_data['2021']))
    plt.plot(years, country_data[years], marker='o', label=country)

plt.xlabel('Years')
plt.ylabel('Gini Coefficient')
plt.title('Gini Coefficient Trends for Selected Countries')
plt.legend()
plt.grid(True)
plt.show()