import requests
import pandas as pd
import matplotlib.pyplot as plt

url = 'http://www.tsetmc.com/tsev2/chart/data/Index.aspx?i=32097828799138957&t=value'

shakes_kol = requests.get(url).text
shakes_kol = shakes_kol.replace(";", "\n")
# print(shakes_kol)

with open('./data.csv', 'w') as file:
    file.write(shakes_kol)

df = pd.read_csv("./data.csv")
df.columns = ['date', 'shakes']
print(df)

df.plot(figsize=(12,3))
plt.show()

df_new = df[3090:]
df_new

plt.figure(figsize=(20, 8))
plt.grid()
plt.plot(df_new['date'], df_new['shakes'])
plt.xticks(rotation=90)
plt.show()

df.to_csv("index_total.csv")

df_new.to_csv("index_1400.csv")