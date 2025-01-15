from bs4 import BeautifulSoup 
import requests  

res = requests.get('https://en.wikipedia.org/wiki/Machine_learning')
print(type(res))

soup = BeautifulSoup(res.text, 'lxml')
print(type(soup))


headline = soup.select('.mw-headline')
#print(toctext)

for i in headline:
    print(i.text)

print("\nThis is from Overview")
toctext = soup.select('.toctext')
for i in toctext:
    print(i.text)