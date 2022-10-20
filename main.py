from bs4 import BeautifulSoup
import requests
import csv
data = []
datas = []
html_text = requests.get("http://www.nepalstock.com/todaysprice").text
soup = BeautifulSoup(html_text, 'lxml')
stocks = soup.find_all('tr')


for stock in stocks:
    x = stock.text
    data.append(x)
# print(data)

for i in data:
    datas.append(i.split('\n'))

del datas[0] #filtered unwanted info
del datas[-4] #filered unwanted info


file = open("NEPSE.csv",'w')
write = csv.writer(file)
for i in datas:
    write.writerow(i)
file.close()
