import scrapy

from scrapy_selenium import SeleniumRequest


class PruebaClienteSpider(scrapy.Spider):
    name = 'prueba_cliente'

    def start_requests(self):
        yield SeleniumRequest(
            #url = "https://www.dropbox.com/sh/qe9h0jdh7fgz006/AADWQ5v8_4YRIF61uAbu75oua?dl=0",
            url = "https://estudiantes.portaloas.udistrital.edu.co/appserv/",
            wait_time = 3,
            screenshot=True,
            callback=self.parse,
            dont_filter=True
        )


    def parse(self, response):        
        datos = response.xpath("//a[contains(@href,'dropbox')]")
        #datos = response.xpath("/html")
        print("tipooooooooooooooo de dato "+ str(type(datos))) 
        for dato in datos:
            yield{
                'Encontrado: ': dato.get()
            }
        pass
