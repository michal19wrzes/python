import tkinter as tk
import time
from . nextPlayer import nextPlayer
from . countdown import countdown
from . insertHistoryRecord import insertHistoryRecord
def afterGenerate(self,mydb,font3,but=None):
        self.counter +=1
        self.wynikiArea.delete('1.0',tk.END)
        self.txtArea.delete('1.0',tk.END)
        catAndLetterList = list(self.statesCitiesTaskGenerate(self.txtArea,mydb)) #random task
        tim = time.strftime("%d %b %Y %H:%M:%S",time.gmtime())
        self.showCurrentScore(mydb,self.wynikiArea) #show curent score
        player = list(nextPlayer(self,mydb))
        #button acceptAnswer press
        if but==1:
            insertHistoryRecord(self,mydb,self.counter,catAndLetterList[0],catAndLetterList[1],player[0],1,tim)
            #print(catAndLetterList,player,'zal',self.counter,tim)
        #button denyAnswer press
        elif but==2:
            insertHistoryRecord(self,mydb,self.counter,catAndLetterList[0],catAndLetterList[1],player[0],0,tim)
            #print(catAndLetterList,player,'niezal',self.counter,tim)
        countdown(self,31)
        time.sleep(1) #action after button is in the same time with countdown timer
     