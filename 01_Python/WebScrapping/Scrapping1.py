from bs4 import BeautifulSoup 
import requests 
import bs4 

res = requests.get("https://finance.yahoo.com")
print(type(res)) 

#print(res.text)

soup = BeautifulSoup(res.text, 'lxml')
print(type(soup))

ttl = soup.select('title')
print(ttl)
print(ttl[0].getText())

