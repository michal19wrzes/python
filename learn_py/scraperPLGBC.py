#2021:12:29   
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
from xlsxwriter import Workbook


dfItems = [] #list of dict to pandas
urlList = [] #list of urls from current webpage

file_name = 'test.xlsx' #output file
v=0 #counter
#load url to urlList

urlList.append("https://plgbc.org.pl/czlonkostwo/czlonkowie-plgbc/")

    
#extract filtered data and save in xlsx
for url in urlList:
    v+=1
    x = requests.get(url) #request get
    soup = BeautifulSoup(x.content, 'html5lib') #html parser
    time.sleep(0.05)
    #for record from filtered html raw
    #print(soup.find('div'))
    for element in soup.find_all('div',{"class":"member_info"}): 
    #data customizing 
        
        title = element.find("h2")
        if title is None:
            continue
        title = title.text
        
        branza = element.find("span")
        if branza is None:
            continue
        branza = branza.text
        branza = ''.join(branza.split())
        
        
        adresHtml = element.find("a",{"target":"_blank"})
        if adresHtml is None:
            continue
        adresHtml = adresHtml.text
        
        
        
        df = {'Nazwa firmy' : title,'Branza' : branza, 'Adres strony' : adresHtml}
        dfItems.append(df)
        
    print('Pobrana ' + str(v) + ' strona')
    #save to xlsx with pandas
df1 = pd.DataFrame(dfItems)
writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
df1.to_excel(writer, sheet_name='Sheet1')    
writer.save()
