import tkinter as tk
from . nextPlayer import nextPlayer
from . countdown import countdown
def afterGenerate(self,mydb):
    
        self.wynikiArea.delete('1.0',tk.END)
    
        self.txtArea.delete('1.0',tk.END)
    
        self.statesCitiesTaskGenerate(self.txtArea) #wylosowanie pytania
        self.showCurrentScore(mydb,self.wynikiArea)#pokaż aktualny wynik graczy
        nextPlayer(self,mydb)#gracze jadą po kolei
        countdown(self,30)
    # testThread.cancel()
    # newTimer()
    # testThread.start()
    
    #rozpocznij odliczanie czasu 30sekund