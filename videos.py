import requests
from bs4 import BeautifulSoup # clear


encabezado ={
     "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36",
}

url = "https://www.xvideos.com/?k=panochas"

respuesta = requests.get(url , headers=encabezado)

# PARSEO DEL ARBOL CON BEAUTIFUL SOUP
soup = BeautifulSoup(respuesta.text)


contenedor = soup.find(class_="mozaique")
contenerdor2 = contenedor.find_all('div' , class_="thumb-block")

for cont in contenerdor2:
    resultado=cont.find(class_="title").text
    resultado=cont.find(class_="title").text
    print(resultado)