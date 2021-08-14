import scrapy
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logzero import logfile, logger



class PruebaClienteSpider(scrapy.Spider):
    logfile("logspider.log", maxBytes=1e6, backupCount=3)
    name = 'prueba_cliente'
    
    
    def start_requests(self):
        url = "https://www.dropbox.com/sh/qe9h0jdh7fgz006/AADWQ5v8_4YRIF61uAbu75oua?dl=0"
        yield scrapy.Request(url=url, callback=self.parse_links)
        
    def parse_links(self, response):                
        options = webdriver.ChromeOptions()
        options.add_argument("headless")        
        driver = webdriver.Chrome('./chromedriver')
        driver.get("https://www.dropbox.com/sh/qe9h0jdh7fgz006/AADWQ5v8_4YRIF61uAbu75oua?dl=0")         #url = "https://www.dropbox.com/sh/qe9h0jdh7fgz006/AADWQ5v8_4YRIF61uAbu75oua?dl=0",
        driver.implicitly_wait(10)        
        links = driver.find_elements_by_xpath('//a[contains(@href,".pdf")]')
        links_count = 0
        for link in links:                        
            yield {
                "link": link.get_attribute("href"),
            }
            links_count += 1

        driver.quit()
        logger.info(f"Total de enlaces encontrados: {links_count}")
         


