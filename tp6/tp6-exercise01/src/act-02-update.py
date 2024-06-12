from urllib.request import Request, urlopen 
from bs4 import BeautifulSoup 
import scraper

url = 'https://www.infobae.com/economia/'
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'}) 
htlm = urlopen(req).read()
soup = BeautifulSoup(htlm, 'lxml')
anchor = soup.find_all("a", class_="headline-link")


links = []
for link in anchor[0:10]:
    link_noticia= link.get('href')
    links.append('https://www.infobae.com/'+link_noticia)


notices = []
#Obtencion de los datos pedidos
for link in links:
    data_extract = scraper.extractData(link)  
    notices.append(data_extract)

text = ''
index=1
for notice in notices:
    text += notice['title'] + " "
    text += notice['summary'] + " "
    text += notice['body'] + " "
    
    # Nombre del archivo
    file_name = "news-"+str(index)+ ".txt"
    index+=1
    # Abrir el archivo en modo de escritura (se crea si no existe)
    with open(file_name, 'w', encoding='utf-8') as archivo:
        # Escribir el contenido del string en el archivo
        archivo.write(text)
    text = ''