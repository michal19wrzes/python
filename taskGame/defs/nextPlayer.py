import tkinter as tk
from .getListOfPlayers import getListOfPlayers
def nextPlayer(self,mydb):
    
    self.infoArea.delete('1.0',tk.END)
    listOfPlayers=getListOfPlayers(self,mydb)
    lenL= len(listOfPlayers)-1 
    if self.x == lenL:
        self.x=0
    else:
        self.x += 1

    f = 'Twoja kolej: {}'.format(listOfPlayers[self.x])
    self.infoArea.insert('1.0',f)