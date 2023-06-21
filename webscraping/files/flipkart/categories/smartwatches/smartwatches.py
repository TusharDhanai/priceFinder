# -*- coding: utf-8 -*-
"""
Script for scrapping smartphone data from flipkart website

Created on Tue Jul 19 11:10:31 2022

@author: Tushar
"""

from bs4 import BeautifulSoup
import requests

session = requests.session()

count = 1

header = "number,link,name,rating,features,price,image,\n"

with open('smartwatches.csv','w') as f:
    f.write(header)
for page in range(1,24):
    req = session.get(f"https://www.flipkart.com/search?q=smartwatches&sid=ajy%2Cbuh&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_na&as-pos=1&as-type=RECENT&suggestionId=smartwatches%7CSmart+Watches&requestId=fca720fc-0525-4e47-9264-14e76daebcec&as-searchtext=smartwa={page}")
    
    doc = BeautifulSoup(req.content,'html.parser')
    
    data = doc.findAll('a',{"class":'_1fQZEK'})
    print(data)



     
    
    for item in data:
        try:
             str_ = '"{}","www.flipkart.com{}","{}","{}","{}","{}","{}",\n'.format(count,item.get('href'),           # id of product
                                 item.find(class_='_4rR01T').contents[0],   # Name of product
                                 item.find(class_='_3LWZlK').contents[0],    # Rating of product
                                 list(map(lambda i: i.contents[0],item(class_='rgWa7D'))),   # array of features
                                  item.find(class_='_30jeq3 _1_WHN1').contents[0],   # price
                                  item.find(class_='_396cs4 _3exPp9').get('src')                                 
                                )
             print(str_)
            
        except:
            print('There was an error.')    
         
        count = count + 1
 
    
 
        with open('smartwatches.csv','a',encoding='UTF8') as f:
             f.write(str_)
              

