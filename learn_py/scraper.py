#2021:12:29   
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
from xlsxwriter import Workbook


dfItems = [] #list of dict to pandas
urlList = [] #list of urls from current webpage
countOfPages = 2 #count of subpages on webpage  
file_name = 'test.xlsx' #output file
v=0 #counter
#load url to urlList
for i in range(countOfPages):
    urlList.append("https://fachowydekarz.pl/mapa-dekarzy/pg/"+str(i+1))
    
#extract filtered data and save in xlsx
for url in urlList:
    v+=1
    x = requests.get(url) #request get
    soup = BeautifulSoup(x.content, 'html5lib') #html parser
    time.sleep(0.05)
    #for record from filtered html raw
    for element in soup.find_all('div',{"class":"cn-right"}): 
    #data customizing 
    
        #title not null
        title = element.find("span",{'class':'org fn notranslate'})
        if title is None:
            continue
        title = title.text
        
        adres = str(element.find_all('span',{'class':'adr cn-address'}))
        adres = adres.replace('[<span class="adr cn-address"><span class="address-name">Praca</span> <span class="street-address notranslate">','')
        adres = adres.replace('</span> <span class="locality">',' ')
        adres = adres.replace('</span> <span class="region">',' ')
        adres = adres.replace('</span> <span class="postal-code">',' ')
        adres = adres.replace('</span> <span class="type" style="display: none;">work</span></span>]','')
        
        phoneNumber = str(element.find_all('span',{'class':'value'}))
        phoneNumber = phoneNumber.replace('[<span class="value">','')
        phoneNumber = phoneNumber.replace('</span>]','')
        
        name = ' '.join(str(element.find_all('span',{'class':'contact-given-name notranslate'})).split())
        name = name.replace('</span>]','')
        name = name.replace('[<span class="contact-given-name notranslate">','')
        
        vorname = ' '.join(str(element.find_all('span',{'class':'contact-family-name notranslate'})).split())
        vorname = vorname.replace('</span>]','')
        vorname = vorname.replace('[<span class="contact-family-name notranslate">','')
        
        #mail not null
        mail = element.find('a',{'class':'value'})
        if mail is None:
            continue
        mail = mail.text
        
        
        df = {'Imie' : name, 'Nazwisko' : vorname, 'Nazwa firmy' : title, 'Adres' : adres, 'nr Tel' : phoneNumber, 'Email' : mail}
        dfItems.append(df)
        
    print('Pobrana ' + str(v) + ' strona')
    #save to xlsx with pandas
df1 = pd.DataFrame(dfItems)
writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
df1.to_excel(writer, sheet_name='Sheet1')    
writer.save()