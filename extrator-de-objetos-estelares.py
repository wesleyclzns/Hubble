from bs4 import BeautifulSoup
import requests

url='https://pt.wikipedia.org/wiki/Lista_de_sat%C3%A9lites_naturais_do_Sistema_Solar'

html_content = requests.get(url).text

soup = BeautifulSoup(html_content, "lxml")
print(soup.prettify())

gdp_table = soup.find("table", attrs={"class": "wikitable sortable jquery-tablesorter"})
