# Making the soup 
"""
To parse a document, pass it into the BeautifulSoup constructor.
we can pass in a string or an open filehandle.
"""

from bs4 import BeautifulSoup 

with open ("D:\\Class\\WebScrapping\\sample.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser') 

soup = BeautifulSoup("<html>a web page</html>", 'html.parser')

print(BeautifulSoup("<html><head></head><body>Sacr&eacute; bleu!</body></html>", "html.parser"))

soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')
tag = soup.b 
print(type(tag))
print(tag.name)

tag.name = "blockquote"
print(tag)

# Attributes:
"""
A tag may have any number of attributes. The tag <b id="boldset">
has an attribute "id" whose value is "boldset". 
We can access a tag's attribute by treating the tag like a dictionary:
"""

tag = BeautifulSoup('<b id="boldset"> bold </b>', 'html.parser')
print(tag.attrs)

tag = BeautifulSoup('<b id="boldest">bold</b>', 'html.parser').b
print(tag['id'])
#print(id)

# We can access that dictionary directly as .attrs:
print(tag.attrs)

# We can add, remove, and modify a tag's attrubutes.
# This is done by treating the tag as a dictonary 

tag['id'] = 'verybold'
tag['another-attribute'] = 1 
print(tag)

del tag['id']
del tag['another-attribute']
print(tag)
print(tag.get('id'))

