# Practice:
from bs4 import BeautifulSoup
import requests 

res = requests.get('https://en.wikipedia.org/wiki/Machine_learning')
res2 = requests.get("https://en.wikipedia.org/wiki/Python_%28programming_language%29")
res3 = requests.get("https://www.tutorialspoint.com/python/index.htm")

soup = BeautifulSoup(res.text, 'lxml')
soup2 = BeautifulSoup(res2.text, 'lxml')
soup3 = BeautifulSoup(res3.text, 'lxml')

print(soup.title)
print(soup2.title)
print(soup3.title)

for i in soup3.b:
    print(i.name)

