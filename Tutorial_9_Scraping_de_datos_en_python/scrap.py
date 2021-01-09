import urllib.request
from bs4 import BeautifulSoup



pagina = 'https://www.diariodevaldivia.cl/noticias/actualidad'
#con esto tenemos los datos en bruto de la pagina
datos = urllib.request.urlopen(pagina).read().decode()
#aplicamos BeautifulSoup a los datos en bruto
soup =  BeautifulSoup(datos)
tags = soup('a')
#imprimimos todos las noticias que contengan /noticia/actualidad/2021/
for link in tags:
    if ("/noticia/actualidad/2021/" in link.get('href')):
        print(link.get('href'))
