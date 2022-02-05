import tkinter as tk
from . nextPlayer import nextPlayer
from . countdown import countdown
def afterGenerate(self,mydb,font3):
        self.timeArea.destroy()
        self.timeArea = tk.Text(self,width=10, height=0.5, font=font3,background='gray')
        self.timeArea.grid(sticky="sn", row=1,column=3, padx=5, pady=5,columnspan=2)
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