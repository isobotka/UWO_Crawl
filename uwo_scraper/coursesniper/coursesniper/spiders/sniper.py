# -*- coding: utf-8 -*-
import scrapy

import time

# Import smtplib for the actual sending function
import smtplib

class SniperSpider(scrapy.Spider):
    content = 'CHECK YOUR COURSES'
    name = "sniper"
    search_url = 'http://studentservices.uwo.ca/secure/Timetables/mastertt/ttindex.cfm'                 
    allowed_domains = ["studentservices.uwo.ca"]
    start_urls = [search_url]

    ##1037 Class
    def parse(self, response):
        data = {'catalognbr': '1037',
                'command' : 'search'}
        yield scrapy.FormRequest(url = self.search_url,
            formdata=data, 
            callback=self.parse3)

    def parse3(self, response):
        ##Writing class to body
        xpath = '/html/body/div/div/div[3]/table/tbody/tr[3]/td[10]'
        body = response.xpath(xpath).extract()
        print body
        
        ##Checking if class is not full
        if any("Not" in s for s in body):
            self.content += " 1037"                
            self.email()
            
        time.sleep(10)

        data = {'catalognbr': '2257',
                'command' : 'search'}
        yield scrapy.FormRequest(url = self.search_url,
            formdata=data, 
            callback=self.parse4)
        
        
    
    def parse4(self, response):
        ##Writing class to body
        xpath = '/html/body/div/div/div[3]/table[1]/tbody/tr[9]/td[10]'
        body = response.xpath(xpath).extract()
        print body
        
        if any("Not" in s for s in body):
            self.content += " 2257"            
            self.email()
           
        time.sleep(10)

        data = {'catalognbr': '2277A',
                'command' : 'search'}
        yield scrapy.FormRequest(url = self.search_url,
            formdata=data, 
            callback=self.parse5)
        
        
    
    def parse5(self, response):
        ##Writing class to body
        xpath = '/html/body/div/div/div[3]/table[1]/tbody/tr[12]/td[10]'
        body = response.xpath(xpath).extract()
        print body
        if any("Not" in s for s in body):
            self.content += " 2277A"            
            self.email()
            
        time.sleep(10)

        data = {'catalognbr': '2250B',
                'command' : 'search'}
        yield scrapy.FormRequest(url = self.search_url,
            formdata=data, 
            callback=self.parse6)
        
        
    
    def parse6(self, response):
        ##Writing class to body
        xpath = '/html/body/div/div/div[3]/table[2]/tbody/tr[3]/td[10]'
        body = response.xpath(xpath).extract()
        print body
        if any("Not" in s for s in body):
            self.content += " 2250B"
            self.email()
        
    def email(self):
        
        mail = smtplib.SMTP('smtp.gmail.com',587)
        
        mail.ehlo()
        
        mail.starttls()
        
        mail.login('email','pass')
        
        mail.sendmail('sender', 'reciever', self.content)
        
        mail.close()
        
        
