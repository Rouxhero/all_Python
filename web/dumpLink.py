from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from os import system
# url = input("=> ")
url="https://python.doctor/"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
print('connection')
web_byte = urlopen(req).read()
open('pageK.html','wb').write(web_byte)
print('uncoding')
webpage = web_byte.decode('utf-8')
print('reading')
soup = BeautifulSoup(webpage ,features="html.parser")
lists = []

for a in soup.find_all('a'):
	if len(a.get('href'))>2:
		if a.get('href')[:2]=='./':
			lists.append(a.get('href'))


print(lists)