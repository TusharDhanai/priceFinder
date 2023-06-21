
from bs4 import BeautifulSoup
import requests

session = requests.session()

count = 1

header = "number,link,name,features,price,image,\n"

with open('shoes.csv','w') as f:
    f.write(header)

for page in range(1,261):
    req = session.get(f"https://www.flipkart.com/search?q=shoes&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&sort=price_desc={page}")
    
    doc = BeautifulSoup(req.content,'html.parser')
    
    data = doc.findAll('a',{"class":'_1xHGtK _373qXS'})
    print(data)



     
    
    for item in data:
        try:

            # =============================================================================
            #              str_ = '"{}","www.flipkart.com{}","{}","{}","{}","{}","{}",\n'.format(count,item.get('href'),           # id of product
            #                                  item.find(class_='_4rR01T').contents[0],   # Name of product
            #                                 list(map(lambda i: i.contents[0],item(class_='rgWa7D'))),   # array of features
            #                                   item.find(class_='_30jeq3 _1_WHN1').contents[0],   # price
            #                                   item.find(class_='_396cs4 _3exPp9').get('src')    
            #                                 ) 
            # ============================================================================= 
            str_ = '"{}","www.flipkart.com{}","{}","{}","{{}}","{}","{}",\n'.format(count,item.get('title'),           # id of product
                     item.find(class_='_2WkVRV').contents[0],   # Name of brand
                     item.find(class_='IRpwTa').contents[0],   # Name of product
                     list(map(lambda i: i.contents[0],item(class_='rgWa_376u-U7D'))),   # array of features
                     item.find(class_='_30jeq3').contents[0],   # price
                     item.find(class_='_2r_T1I').contents[0],   # iamge of the product
                     
                                                                                  
            print(str_)
        except:
            print('There was an error.')    
         
        count = count + 1
 
    with open('shoes.csv','a',encoding='UTF8') as f:
         f.write(str_)
