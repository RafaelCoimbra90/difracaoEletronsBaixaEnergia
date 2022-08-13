import pandas as pd
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
df = pd.read_csv(url,on_bad_lines=False)
df['date'] = pd.to_datetime(df['date'])

countries = ['Albania', 'Belarus', 'Bosnia and Herzegovina', 'Bulgaria', 'Croatia', 'Hungary', 'Kosovo', 'Moldova', 'Montenegro', 'North Macedonia', 'Poland', 'Romania', 'Russia', 'Serbia', 'Turkey', 'Ukraine']


for country in countries:
    df_country = df[df.location == country].groupby(pd.Grouper(freq='W', key='date'))['new_deaths_per_million'].mean().reset_index()
    assert len(df_country) > 0
    plt.plot(df_country.date, df_country.new_deaths_per_million)

df_countries = df[df.location.isin(countries)].groupby(pd.Grouper(freq='W', key='date'))['new_deaths_per_million'].mean().reset_index()

plt.plot(df_countries['date'], df_countries['new_deaths_per_million'], linewidth=4)
plt.legend([*countries, 'average'])

plt.show()