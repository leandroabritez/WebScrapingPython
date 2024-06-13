#C:\Users\user\AppData\Roaming\Python\Python311\Scripts
# scrapy runspider stackoverfloy_scrapy.py -o resultados.csv -t csv
# scrapy runspider eje.py -o resultados.csv -t csv
# scrapy runspider stackoverfloy_scrapy.py  -o result.json -t json
# scrapy runspider stackoverfloy_scrapy.py  -O result.json -t json
# scrapy runspider eje.py -o mercado_libre.csv -t csv

# VER RECURSOS DE LA CLASE PARA INSTALAR SCRAPY
from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup


class Pregunta(Item):       # de scrapy.item
     pregunta = Field()     # de scrapy.item
     descripcion = Field()  # de scrapy.item




class StackOverflowSpider(Spider): # scrapy.spiders
    name = "miPrimerSpider"

    #Encabezado
    custom_settings = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
    }

    # URL a scrapear
    start_urls=['https://stackoverflow.com/questions']


    def parse(self , response):

        sel = Selector(response)
        # Buscar el id y la clase a buscar
        preguntas=sel.xpath('//div[@id="questions"]//div[@class="s-post-summary--content"]')
        for pregunta in preguntas:
            item = ItemLoader(Pregunta(), pregunta) # scrapy.loader
            item.add_xpath('pregunta' , './/h3/a/text()')
            item.add_xpath('descripcion' , './/div[@class="s-post-summary--content-excerpt"]/text()')

            yield item.load_item()

            





