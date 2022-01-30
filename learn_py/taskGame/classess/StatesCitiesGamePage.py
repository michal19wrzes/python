import tkinter as tk
class StatesCitiesGamePage(tk.Frame):
    from ..defs.statesCitiesTaskGenerate import statesCitiesTaskGenerate
    from ..defs.showCurrentScore import showCurrentScore
    from ..defs.getListOfPlayers import getListOfPlayers
    
    

    def __init__(self, parent, controller):
        self.x=0
        
        def acceptAnswer():
            listOfPlayers = self.getListOfPlayers(controller.mydb)
           #update task by the entered params where id = idTaskEntry, result inserted to big output entry
            query="UPDATE users SET user_points=user_points+1 WHERE user_name ='{}'".format(listOfPlayers[self.x])
            cursor = controller.mydb.cursor()
            cursor.execute(query)
            controller.mydb.commit()       
            cursor.close()
            afterGenerate()
            
        def denyAnswer():
            afterGenerate()
            
        def nextPlayer():
            infoArea.delete('1.0',tk.END)
            listOfPlayers=self.getListOfPlayers(controller.mydb)
            lenL= len(listOfPlayers)-1
            if self.x == lenL:
                self.x=0
            else:
                self.x += 1

            f = 'Twoja kolej: {}'.format(listOfPlayers[self.x])
            infoArea.insert('1.0',f)
        def afterGenerate():
            wynikiArea.delete('1.0',tk.END)
            txtArea.delete('1.0',tk.END)
            self.statesCitiesTaskGenerate(txtArea) #wylosowanie pytania
            self.showCurrentScore(controller.mydb,wynikiArea)#pokaż aktualny wynik graczy
            nextPlayer()#gracze jadą po kolei
            
            
             
            
            #jesli zalicz to +1 punkt dla gracza
            
        tk.Frame.__init__(self, parent,background='black')      
        self.controller = controller
        
        label = tk.Label(self, text="GRA PAŃSTWA-MIASTA",width=25, font=controller.title_font)
        label.grid(row=0, column=0 ,sticky="S", pady=30,padx=20)
        
        
        
        txtArea = tk.Text(self,width=27, height=1, font=controller.font4,background='gray')
        txtArea.grid(sticky="sn", row=2,column=1, padx=5, pady=5,columnspan=2)
        
        infoArea = tk.Text(self,width=40, height=0.5, font=controller.font3,background='gray')
        infoArea.grid(sticky="sn", row=1,column=1, padx=5, pady=5,columnspan=2)
        
        wynikiArea = tk.Text(self,width=20, height=10, font=controller.font3,background='gray')
        wynikiArea.grid(sticky="SN", row=2,column=3, padx=5, pady=5,rowspan=1)
        
        
        button = tk.Button(self,
                           text="Rozpocznij",
                           command=afterGenerate,
                           pady=30,
                           padx=5,
                           width=25,
                           bg='violet',
                           font = controller.title_font)
        button.grid(row=2,column=0,sticky="S",pady=30,padx=50)
        
        
        
        button1 = tk.Button(self,
                           text="Cofnij",
                           command=lambda: controller.show_frame("GamesPage"),
                           pady=30,
                           
                           width=25,
                           bg='violet',
                           font = controller.title_font)
        button1.grid(row=3,column=0,sticky="S",pady=30,padx=50)

        button2 = tk.Button(self,
                           text="Nie zalicz",
                           command=denyAnswer,
                           pady=11,
                           
                           width=15,
                           bg='Tomato',
                           font = controller.title_font)
        button2.grid(row=3,column=2,sticky="W",pady=30,padx=50)

        button3 = tk.Button(self,
                           text="Zalicz",
                           command=lambda:acceptAnswer(),
                           pady=11,
                           padx=5,
                           width=15,
                           bg='#66FF66',
                           font = controller.title_font)
        button3.grid(row=3,column=1,sticky="W",pady=30,padx=50)
