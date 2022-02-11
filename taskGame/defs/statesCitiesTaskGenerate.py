import string
import random
# def addHistory(self,mydb,v,f):
# #action after click 'add task' button
    # query="INSERT INTO gameHistory(category,letter) VALUES ('{}',{},{})".format(taskEntry.get(),statusEntry.get(),priorityEntry.get())
    # cursor = mydb.cursor()
    # cursor.execute(query)
    # mydb.commit()
    # cursor.close()
    
def randomCapitalLetter():
    n =string.ascii_uppercase
    return random.choice(n.replace('XY','').replace('V','').replace('Q',''))
def statesCitiesTaskGenerate(self,txtArea,mydb):
    #txtArea.delete('1.0',END)
#action after click 'show task' button
    listOfCategory = ['Państwo',
                      'Miasto',
                      'Zbiornik wodny (np. rzeka, morze)',
                      'Rzecz',
                      'Imię męskie',
                      'Imię żeńskie',
                      #'Rasa psów',
                      'Wyraz angielski',
                      'Marka auta',
                      'Marka ubrań',
                      'Przymiotnik',
                      'Czasownik',
                      'Zawód',
                      'Postać z bajki',
                      'Postać z filmu / serialu',
                      'Firma',
                      'Aktor',
                      #'Osoba popularna',
                      'Zwierzę',
                      'Sportowiec',
                      'Influencer',
                      'Warzywo',
                      'Owoc',
                      'Święto',
                      'Tytuł filmu / serialu',
                      'Kolor',
                      'Firma alkoholu lub papierosów',
                      'Dyscyplina sportu',
                      'Piosenkarz / Muzyk / Zespół muzyczny',
                      'Wieś',
                      'Element ciała',
                      'Potrawa',
                      'Gra',
                      'Tytuł piosenki',
                      'Książka',
                      'Roślina']
    randCat = listOfCategory[random.randint(0,len(listOfCategory)-1)]
    randLet = randomCapitalLetter()
    
    yield randCat
    yield randLet
    
    s = '{} na literę {}\n'.format(randCat,randLet)
    
    txtArea.insert('1.0',s) #na początek