from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup


class Pregunta(Item):
     pregunta = Field()
     descripcion = Field()




class StackOverflowSpider(Spider):
    name = "miPrimerSpider"

    custom_settings = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
    }

    start_urls=['https://www.igrupos.com/whatsapp']


    def parse(self , response):

        sel = Selector(response)
        preguntas=sel.xpath('//div[@class="media-body"]')
     

        for pregunta in preguntas:
            item = ItemLoader(Pregunta(), pregunta)
            item.add_xpath('pregunta' , './/a/h4/text()')
            item.add_xpath('descripcion' , './/a/text()')

            yield item.load_item()







            