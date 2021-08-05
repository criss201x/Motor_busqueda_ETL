import os 
import sys
import requests
from lxml import html
import urllib.parse as urlparse
from bs4 import BeautifulSoup

class Scraping:    
    def extraerImagenes(self, url):
        print("Obteniendo imagenes de la url" + url)
        try:
            response = requests.get(url)            
            parsed_body = html.fromstring(response.text)
            #usamos una expresion regular para obtener las imagenes
            images = parsed_body.xpath('//img/@src')
            print ('imagenes %s encontradas ' % len(images))
            #creando un directorio para las imagenes que vamos a guardar 
            os.system("mkdir images")
            for image in images:
                if image.startswith("http") == False:
                    download = url + image
                else:
                    download = image
                #descargando imagenes en un directorio
                print(download)
                r = requests.get(download)
                f = open('images/%s' % download.split('/')[-1],'wb')
                f.write(r.content)
                f.close()
        except e:            
            print (e)
            print("Error de conexion con: " + url)
            pass
        
    def ScrapingPdf(self,url):
        print("\nObteniendo pdfs de la url" + url)
        
        try:
            response = requests.get(url)
            parsed_body = html.fromstring(response.text)
            #expresion regular para obtener los pdfs 
            pdfs = parsed_body.xpath('//a[@href[contains(., ".pdf")]]/@href')
            print(pdfs)
            #creando directorio para los pdfs a guardar 
            if len(pdfs) > 0:
                os.system("mkdir los_pdfs")
                
            print('Encontrados:  %s pdf' % len(pdfs))
            for pdf in pdfs:
                if pdf.startswith("http") == False:
                    download = url + pdf
                else:
                    download = pdf
                #descarga pdfs
                r = requests.get(download)
                f = open('pdfs/%s' % download.split('/')[-1], 'wb')
                #f = open(download.split('/')[-1], 'wb')
                f.write(r.content)
                f.close()
                
        except e:
            print (e)
            print ("Error de conexion con: " + url)
            pass
        
    def ScrapingLinks(self,url):
        print("\nObteniendo links de la url" + url)        
        
        try:
            response = requests.get(url)
            parsed_body = html.fromstring(response.text)            
            #expresion regular para obtener los links
            links = parsed_body.xpath('//a/@href')
            
            print('Encontrados:  %s links' % len(links))
            for link in links:
                print (link)
                
        except e:
            print (e)
            print ("Error de conexion con: " + url)
            pass        