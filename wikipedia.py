import requests
from lxml import html # pip install lxml

## Enviar encabezado para que no sea robot y bloquen el ip. 

encabezado ={
     "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36",
}

url = "https://www.wikipedia.org/"

respuesta = requests.get(url , headers=encabezado)

# Nos devuelve toda la info css+html de la página
# print(respuesta.text)


# Para obtener la palabra "español" desde la página
parser = html.fromstring(respuesta.text)

#obtener por id 
#español = parser.get_element_by_id("js-link-box-es")

# obtener el texto contenifo dentro
#print(español.text_content())

# Otra forma de hacerlo: Dentro de la raíz del documento
# busca la etiqueta "a" con el @id ,  luego con las barras busco los hijos de esa etiqueta
#español=parser.xpath("//a[@id='js-link-box-es']/strong/text()")
#print(español)


# Para descargar todos los nombres de los idiomas, lo hago por clase. 
# Busco la etiquta div, y el comienzo de las clases que comparten todos los idiosmas. 
idiomas= parser.xpath("//div[contains(@class,'central-featured-lang')]//strong/text()")


for idioma in idiomas:
    print(idioma)

idiomas = parser.find_class('central-featured-lang')
for idioma in idiomas:
  print(idioma.text_content())