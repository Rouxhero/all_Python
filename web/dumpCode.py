from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from os import system
url="https://www.kartable.fr/ressources/mathematiques/cours/les-suites-6/4176"
class bot():
	def __init__(self):
		name = input('enter name :')
	def get_code1(self):
		url = input('url : ')
		req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
		print('connection')
		web_byte = urlopen(req).read()
		print('uncoding')
		webpage = web_byte.decode('utf-8')
		print('Done')
		self.page = webpage
	def write_page(self):
		name = input('File name : ')
		open(name+'.html','wt',encoding="utf-8").write(self.page)
		print('page saved at : ',name+'.html')
	def check_href(self):
		soup = BeautifulSoup(self.page ,features="html.parser")
		for a in soup.find_all('a'):
			print(a.get("href"))
bote = bot()
bote.get_code1()
bote.check_href()
bote.write_page()

