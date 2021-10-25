from faker import Faker
from random import randint as r
from random import choice
faker = Faker("Fr_fr")

for i in range(42) :
	profile1 = faker.simple_profile()
	name = profile1['name']
	firstName = name.split(' ')[0]
	lastName = name.split(' ')[1]
	mail = profile1['mail']
	print('(\'{}\',\'{}\',\'{}\',{}),'.format(firstName,lastName,mail,r(1,4)))




# festival1 = lambda x: '2021-7-'+str(x)
# festival2 = lambda x: '2021-6-'+str(x)

# data = {1:festival1,2:festival2}
# for i in range(30):
# 	fest = r(1,2)
# 	if fest == 1 :
# 		daydebut = r(4,6)
# 		dayfin = r(daydebut,6)
# 	else : 
# 		daydebut = r(21,24)
# 		dayfin = r(daydebut,24)
# 	dif = dayfin - daydebut
# 	debut = data[fest](daydebut)
# 	fin = data[fest](dayfin)
# 	prix = r(31,38)+dif*10
# 	print('(\'{}\',\'{}\',{}),'.format(debut,fin,prix))


# parti = []
# for i in range (30):
# 	nb = r(1,42)
# 	while nb in parti :
# 		nb = r(1,42)
# 	parti.append(nb)

# for nb in parti :
# 	print('({}),'.format(nb))

# billets = list(range(1,30))
# parti = list(range(1,30))
# for i in range(29):
# 	bille = choice(billets)
# 	part = choice(parti)
# 	billets.remove(bille)
# 	parti.remove(part)
# 	print('({},{},{}),'.format(bille,part,r(1,2)))