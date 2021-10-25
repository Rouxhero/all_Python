from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from os import system
import psycopg2 as db_api


class Final :
	def __init__(self):
		self.txt = ""
	def add(self,txt):
		self.txt += txt+"\n"
	def write(self):
		open("insert.sql","w").write(self.txt)
data = Final()

config = "host=<host> user=<user> password=<password> dbname=<dbname>"
try :
	conn=db_api.connect(config)
	conn.autocommit=True
	conn.cursor().execute('set search_path = TP5')

except IOError as e:
   	print("[DataBase][Connection Error]  {} ".format(e))
   	exit()
cursor = conn.cursor()
cursor.execute("""SELECT * FROM  ustensile ;""")
ustensile = cursor.fetchall()
cursor.execute("""SELECT * FROM  produit ;""")
produit = cursor.fetchall()
cursor.execute("""SELECT * FROM  categorie ;""")
categorie = cursor.fetchall()

EQUIV_NON_ACCENTUE = {
    # 'a' : ('à', 'ã', 'á', 'â'),
    # 'e' : ('é', 'è', 'ê', 'ë'),
    # 'i' : ('î', 'ï'),
    # 'u' : ('ù', 'ü', 'û'),
    # 'o' : ('ô', 'ö'),
    # 'c' : ('ç')
    ' ' : ('\'')
}


def checkProd(etape):
	datas = etape.split(' ')
	for word in datas:
		if word in indexedProd:
			print(word)
def bas_casse_sans_accent(ch):
    """
    :param: ch (str)
    :return: (str)
    :CU: None    
    :Exemples:
    >>> bas_casse_sans_accent('Orangé')
    'orange'
    """
    d2 = {}
    e = ''
    ch=ch.lower()
    for l, a in EQUIV_NON_ACCENTUE.items():
      for i in a:
        d2[i] = l
    for o in ch:
      e += d2.get(o, o)
    return e



categori = "Pizza"
nameRec = "margherita"
listeCateg = []
print(categorie)
print(produit)
print(ustensile)
for line in categorie:
	listeCateg.append(line[1])
indexedProd = []
allreadyProduit = []
for line in produit:
	txt = ""
	ll = line[1].split(" ")
	indexedProd.append(ll[0])
	allreadyProduit.append(line[1])

allreadyUstentil = []
indexUstensil = 1
for line in ustensile:
	allreadyUstentil.append(line[1])
	indexUstensil +=1
produit = []
ustensile = []
class count :
	def __init__(self):
		self.nb = 0
	def add(self):
		self.nb+=1
aa = count()
def addProduit(produitName):
	if not produitName in allreadyProduit:
		allreadyProduit.append(produitName)
		txt = ""
		ll = produitName.split(" ")
		indexedProd.append(ll[0])
		produit.append(produitName)
	aa.add()

def addUstensil(ustName):
	if not ustName in allreadyUstentil:
		allreadyUstentil.append(ustName)
		ustensile.append(ustName)
if not categori in listeCateg :
	listeCateg.append(categori)
	numCateg = listeCateg.index(categori)
	data.add("""INSERT INTO TP5.categorie (numCategRec,nomCat) VALUES ({},'{}');\n """.format(numCateg,categori))
else :
	numCateg = listeCateg.index(categori)

url="https://www.marmiton.org/recettes/recette_la-pizza-margherita-recette-realisable-a-la-maison_335446.aspx"
#url="https://www.marmiton.org/recettes/recette_mojito_14615.aspx"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
print('[connection] : ',end='')
web_byte = urlopen(req).read()
print('Done\n[uncoding] : ',end='')
# webpage = web_byte.decode('UTF-8')
print('Done\n[reading] : ',end='')
soup = BeautifulSoup(web_byte ,features="html.parser")
print('Done')
lists = []
time = ""
etape = {}

ingredient = []
## Recuperation du temps et des etapes
for a in soup.find_all('div'):
	if a.get('class') != None:
		# print(a.get('class'))
		if a.get('class') ==  ['recipe-primary__item']:
			child = a.findChildren()
			if child[0].get('class') == ['icon', 'icon-timer1']:
				time = child[1].get_text()
		elif a.get('class') == ['recipe-step-list__container']:
			child = a.findChildren()
			etape[bas_casse_sans_accent(child[0].get_text()[1:-1])] =  bas_casse_sans_accent(child[2].get_text())
#Produit et Ustensile
for ul in soup.find_all('ul'):
		if ul.get('class') == ['item-list']:
			all_Li = ul.findChildren()
			tempProduit = []
			for li in all_Li:
				if li.get('class') == ['utensil--bold']:
					addUstensil(bas_casse_sans_accent(li.findChildren()[1].get_text()))
				if li.get('class') == ['quantity-data']:
					tempProduit.append(bas_casse_sans_accent(li.get_text()))
				if li.get('class') == ['unit-data']:
					tempProduit.append(bas_casse_sans_accent(li.get('data-plural')))
				if li.get('class') ==['ingredient-data']:
					tempProduit.append(bas_casse_sans_accent(li.get('data-singular')))
				if len(tempProduit) == 3:
					ingredient.append(tempProduit)
					addProduit(tempProduit[2])
					tempProduit = []
			# ustensile.append(a.get_text())
print(time) 
# print(etape)

if len(ustensile)!=0:
	data.add("INSERT INTO TP5.Ustensile (nomUst) VALUES")
	if len(ustensile)>1 :
		for ust in ustensile[:-1] :
			data.add('(\''+ust+'\'),')
	if len(ustensile)>0:
		data.add('(\''+ustensile[-1]+'\');\n')


if len(produit)!=0:
	data.add("INSERT INTO TP5.Produit (nomProd) VALUES")
	if len(produit)>1 :
		for ust in produit[:-1] :
			data.add('(\''+ust+'\'),')
	if len(produit)>0:
		data.add('(\''+produit[-1]+'\');')
times = "5:00:00"
data.add("""
INSERT INTO TP5.Recette(nomRec, nbProd, temps,numCategRec) VALUES
('{}', {}, '{}', {});\n""".format(nameRec,aa.nb,times,numCateg))

cursor.execute("""SELECT numRecette FROM Recette""")
datas = cursor.fetchall()
if len(ustensile)!=0:
	data.add("""INSERT INTO TP5.Utiliser(numUst,numRecette)VALUES """)
	if len(ustensile)>1 :
		for ust in ustensile[:-1] :
			nb = allreadyUstentil.index(ust)
			data.add('('+str(nb)+','+str(datas[0][0]+1)+'),')
	if len(ustensile)>0:
		nb = allreadyUstentil.index(ust)
		data.add('('+str(nb)+','+str(datas[0][0]+1)+');\n')

if len(etape)!=0:
	nb = 1
	data.add("INSERT INTO TP5.Etape(numEtape,numRecette,description)VALUES")
	if len(etape)>1 :
		for key in list(etape.keys())[:-1]:
			data.add('('+str(nb)+','+str(datas[0][0]+1)+',\''+etape[key]+'\'),')
			nb += 1
	if len(etape)>0:
		key =  list(etape.keys())[-1]
		data.add('('+str(nb)+','+str(datas[0][0]+1)+',\''+etape[key]+'\');\n')
data.write()

print(indexedProd)
if len(etape)!=0:
	nb = 1
	# data.add("INSERT INTO TP5.Etape(numEtape,numRecette,description)VALUES")
	if len(etape)>1 :
		for key in list(etape.keys())[:-1]:
			checkProd(etape[key])
			print(nb)
			nb += 1
	if len(etape)>0:
		key =  list(etape.keys())[-1]
		checkProd(etape[key])
		print(nb)