import tkinter as tk
class StatesCitiesGamePage(tk.Frame):
    from ..defs.statesCitiesTaskGenerate import statesCitiesTaskGenerate
    from ..defs.showCurrentScore import showCurrentScore
    from ..defs.getListOfPlayers import getListOfPlayers
    
    def __init__(self, parent, controller):
    
        from ..defs.afterGenerate import afterGenerate
        from ..defs.acceptAnswer import acceptAnswer
        
        self.counter=0 #count of played rounds, need to history
        self.x=0       #need to nextPlayer
        
        tk.Frame.__init__(self, parent,background='#14285c')      
        self.controller = controller
        
        label = tk.Label(self, text="GRA PAŃSTWA-MIASTA",width=25, font=controller.title_font)
        label.grid(row=0, column=0 ,sticky="S", pady=30,padx=20)
        
        self.txtArea = tk.Text(self,width=27, height=1, font=controller.font4,background='#94bdff')
        self.txtArea.grid(sticky="sn", row=2,column=1, padx=5, pady=5,columnspan=2)
        
        self.infoArea = tk.Text(self,width=40, height=0.5, font=controller.font3,background='#94bdff')
        self.infoArea.grid(sticky="sn", row=1,column=1, padx=5, pady=5,columnspan=2)
        
        self.timeArea = tk.Text(self,width=10, height=0.5, font=controller.font3,background='#94bdff')
        self.timeArea.grid(sticky="sn", row=1,column=3, padx=5, pady=5,columnspan=2)
        
        
        self.wynikiArea = tk.Text(self,width=20, height=10, font=controller.font3,background='#94bdff')
        self.wynikiArea.grid(sticky="SN", row=2,column=3, padx=5, pady=5,rowspan=1)
        
        
        button1 = tk.Button(self,
                           text="Rozpocznij",
                           command=lambda:afterGenerate(self, controller.mydb,controller.font3),
                           pady=30,
                           padx=5,
                           width=25,
                           bg='violet',
                           font = controller.title_font)
        button1.grid(row=2,column=0,sticky="S",pady=30,padx=50)
        
        
        
        button2 = tk.Button(self,
                           text="Cofnij",
                           command=lambda: controller.show_frame("GamesPage"),
                           pady=30,
                           
                           width=25,
                           bg='violet',
                           font = controller.title_font)
        button2.grid(row=4,column=0,sticky="S",pady=30,padx=50)
        
        
        button3 = tk.Button(self,
                           text="Historia rozgrywki",
                           command=lambda: controller.show_frame("GameHistoryPage"),
                           pady=30,
                           padx=5,
                           width=25,
                           bg='violet',
                           font = controller.title_font)
        button3.grid(row=3, column=0,sticky="S",pady=30,padx=5)
        

        button4 = tk.Button(self,
                           text="Nie zalicz",
                           command=lambda:afterGenerate(self,controller.mydb,controller.font3,2),
                           pady=11,
                           
                           width=15,
                           bg='Tomato',
                           font = controller.title_font)
        button4.grid(row=3,column=2,sticky="W",pady=30,padx=50)

        button5 = tk.Button(self,
                           text="Zalicz",
                           command=lambda:acceptAnswer(self,controller.mydb,controller.font3),
                           pady=11,
                           padx=5,
                           width=15,
                           bg='#66FF66',
                           font = controller.title_font)
        button5.grid(row=3,column=1,sticky="W",pady=30,padx=50)
