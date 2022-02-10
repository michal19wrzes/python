import tkinter as tk
import time
from . nextPlayer import nextPlayer
from . countdown import countdown
def afterGenerate(self,mydb,font3):
        
        self.wynikiArea.delete('1.0',tk.END)
        self.txtArea.delete('1.0',tk.END)
        self.statesCitiesTaskGenerate(self.txtArea) #random task
        self.showCurrentScore(mydb,self.wynikiArea) #show curent score
        nextPlayer(self,mydb)
        countdown(self,31)
        time.sleep(1) #action after button is in the same time with countdown timer
     