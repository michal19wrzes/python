import string
import random
def randomCapitalLetter():
    n =string.ascii_uppercase
    return random.choice(n.replace('XY','').replace('V','').replace('Q',''))
def statesCitiesTaskGenerate(self,txtArea):
    #txtArea.delete('1.0',END)
#action after click 'show task' button
    listOfCategory = ['Państwo',
                      'Miasto',
                      'Rzeka',
                      'Rzecz',
                      'Imię męskie',
                      'Imię żeńskie',
                      'Rasa psów',
                      'Wyraz angielski',
                      'Marka auta',
                      'Marka ubrań',
                      'Przymiotnik',
                      'Czasownik',
                      'Zawód',
                      'Postać z bajki',
                      'Firma',
                      'Aktor',
                      'Osoba popularna',
                      'Zwierzę',
                      'Warzywo',
                      'Owoc',
                      'Tytuł filmu',
                      'Kolor',
                      'Firma alkoholu lub papierosów',
                      'Dyscyplina sportu',
                      'Roślina']
    v = listOfCategory[random.randint(0,len(listOfCategory)-1)]
    f = randomCapitalLetter()
    s = '{} na literę {}\n'.format(v,f)
    
    txtArea.insert('1.0',s) #na początek