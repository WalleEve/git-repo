from bs4 import BeautifulSoup   
import requests  

res = requests.get('https://en.wikipedia.org/wiki/Machine_learning') 

soup = BeautifulSoup(res.text, 'lxml')

links_ = soup.select('a', href=True)  

for i in links_:
    #print(i.text)
    #print(i.text[0:5])
    if  i.text[0:5] == 'https':
        print(i.text)

# https://en.wikipedia.org/w/index.php?title=Machine_learning&oldid=989639744
# https://duckduckgo.com/?q=machine+learning&ia=web

res1 = requests.get('https://duckduckgo.com/?q=machine+learning&ia=web')
soup2 = BeautifulSoup(res1.text, 'lxml')

links_2 = soup2.select('a', href=True) 
for j in links_2:
    print(j.text)
    if j.text[0:5] == 'https':
        print(j.text)
