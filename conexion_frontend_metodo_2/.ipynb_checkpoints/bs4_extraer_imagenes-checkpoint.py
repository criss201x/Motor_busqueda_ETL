from bs4 import BeautifulSoup
import urllib.parse as urlparse 
import requests
import os

class Scraping:
    def scrapingBeautifulSoup(self, url):
        try:
            print("Obteniento imagenes con Beautiful soup! " + url)
            #directorio para las imagenes a guardar 
            os.system("mkdir images")
            response = requests.get(url)
            bs = BeautifulSoup(response.text, 'lxml')
            for tagImage in bs.find_all("img"):
                if tagImage['src'].startswith("http") == False:
                    download = url + tagImage['src']
                else:
                    download = tagImage['src']
                print(download)
                #descargando imagenes al directorio 
                r = requests.get(download)
                f = open('images/%s' % download.split('/')[-1], 'wb')
                f.write(r.content)
                f.close()
        except e:
            print (e)
            print ("Error de conexion: "+ url)
            pass
