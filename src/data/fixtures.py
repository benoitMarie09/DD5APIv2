import requests
from bs4 import BeautifulSoup
from collections import OrderedDict
from pprint import pprint

url = "https://www.aidedd.org/dnd/sorts.php?vf=projection-astrale"

result = requests.get(url)

soup = BeautifulSoup(result.text, 'html.parser')

nom = soup.find("h1").string.strip()
niveau = int(soup.find("div", class_='ecole').string.split('-')[0].replace('niveau',''))
ecole = soup.find("div", class_='ecole').string.split('-')[1].strip()
incantation = soup.find(string ="Temps d'incantation").next_element.string.replace(':','').strip()
portee = soup.find(string ="Portée").next_element.string.replace(':','').strip()
duree = soup.find(string ="Durée").next_element.string.replace(':','').strip()


composante = soup.find(string ="Composantes").next_element.string.replace(':','').strip()
composante_desc = composante.split('(')[1].replace(')','')
consomme =  'consomme' in composante_desc.split(' ')
compos = composante.split('(')[0].split(',')
compos = [item.strip() for item in compos]
compo_V = 'V' in compos
compo_S = 'S' in compos
compo_M = 'M' in compos

desc = soup.find("div", class_='description')
print(desc.text)