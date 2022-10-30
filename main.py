from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = []
datas = []
html_text = requests.get("http://www.nepalstock.com/todaysprice").text
soup = BeautifulSoup(html_text, 'lxml')
stocks = soup.find_all('tr')

for stock in stocks:
    x = stock.text
    data.append(x)

for i in data:
    datas.append(i.split('\n')[1:-1])

del datas[0]  # filtered unwanted info
del datas[-4:]  # filtered unwanted info
for v in datas[1:-3]:  # filtered unwanted info
    v.pop()
    v.pop(-1)
# csv conversion
file = open("NEPSE.csv", 'w')
write = csv.writer(file)
for i in datas:
    write.writerow(i)
file.close()


# Bar Chart visualization
df = pd.read_csv('/content/NEPSE.csv',on_bad_lines='skip')
df = df.iloc[0:20]

x = list(df['Traded Companies'])
y = list(df['No. Of Transaction'])

font = {'family' : 'monospace',
        'weight' : 'normal',
        'size'   : 10}

plt.rc('font', **font)
plt.xticks(rotation =90)
plt.xlabel("Traded Companies")
plt.ylabel("No. of Transaction")
plt.title("No. of trasactions for top 20 Companies")
plt.bar(x, y, width=.5)
plt.show()



