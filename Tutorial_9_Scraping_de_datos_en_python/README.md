##Scraping de datos con python

que es el scraping de datos?
el scraping de datos busca extraer informacion de las paginas webs y guardalo en una base de datos, en este tutorial trabajaremos con la pagina web de diario el ranco <https://www.diariodevaldivia.cl/noticias/actualidad>

entonces comenzamos
1.- necesitamos importar las librerias necesarias
>   1.1.- import urllib.request
> 2.2.- from bs4 import BeautifulSoup
con bs4 podremos extraer las partes que nos interesan de la pagina
2.- luego utilizamos `urllib.request.urlopen(pagina).read().decode()` para abri la pagina y guardarla
esta parte quedaria asi
```
pagina = 'https://www.diariodevaldivia.cl/noticias/actualidad'
#con esto tenemos los datos en bruto de la pagina
datos = urllib.request.urlopen(pagina).read().decode()
```
3.- luego usamos `BeautifulSoup` para optimizar los datos en brutos y poder utilizar la libreria bs4
4.- utilizamos `tags = soup('a')` para obtener todas las tags de la pagina web
5.- finalmente las imprimimos especificando que solo se impriman los links que posean las noticias de actualidad
```
for link in tags:
    if ("/noticia/actualidad/2021/" in link.get('href')):
        print(link.get('href'))
```