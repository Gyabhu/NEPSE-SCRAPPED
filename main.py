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
del datas[-4]  # filtered unwanted info
for v in datas[1:-3]:  # filtered unwanted info
    v.pop()
    v.pop(-1)

# csv conversion
file = open("NEPSE.csv", 'w')
write = csv.writer(file)
for i in datas:
    write.writerow(i)
file.close()

# pandas visualization
df = pd.read_csv('NEPSE.csv', encoding='iso-8859-1')
print(df)
