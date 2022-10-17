from bs4 import BeautifulSoup
import requests
data=[]
datas=[]
html_text = requests.get("http://www.nepalstock.com/todaysprice").text
soup = BeautifulSoup(html_text, 'lxml')
stocks = soup.find_all('tr')

for stock in stocks:
    x = stock.text.replace(' ','')
    data.append(x)
for i in data:
    datas.append(i.split('\n')[1:-1])

del datas[0]
del datas[-4]
blank= ''
clean_data = [[ele for ele in spaces if ele != blank] for spaces in datas]
print(clean_data)