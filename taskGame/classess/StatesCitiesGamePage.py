import tkinter as tk
class StatesCitiesGamePage(tk.Frame):
    from ..defs.statesCitiesTaskGenerate import statesCitiesTaskGenerate
    from ..defs.showCurrentScore import showCurrentScore
    from ..defs.getListOfPlayers import getListOfPlayers
    
    import time
    
    
    
    def __init__(self, parent, controller):
    
        from ..defs.afterGenerate import afterGenerate
        from ..defs.acceptAnswer import acceptAnswer
        
        self.x=0
        
        
        
               
        
        
           
            
        tk.Frame.__init__(self, parent,background='black')      
        self.controller = controller
        
        label = tk.Label(self, text="GRA PAŃSTWA-MIASTA",width=25, font=controller.title_font)
        label.grid(row=0, column=0 ,sticky="S", pady=30,padx=20)
        
        
        
        self.txtArea = tk.Text(self,width=27, height=1, font=controller.font4,background='gray')
        self.txtArea.grid(sticky="sn", row=2,column=1, padx=5, pady=5,columnspan=2)
        
        self.infoArea = tk.Text(self,width=40, height=0.5, font=controller.font3,background='gray')
        self.infoArea.grid(sticky="sn", row=1,column=1, padx=5, pady=5,columnspan=2)
        
        self.timeArea = tk.Text(self,width=10, height=0.5, font=controller.font3,background='gray')
        self.timeArea.grid(sticky="sn", row=1,column=3, padx=5, pady=5,columnspan=2)
        
        self.wynikiArea = tk.Text(self,width=20, height=10, font=controller.font3,background='gray')
        self.wynikiArea.grid(sticky="SN", row=2,column=3, padx=5, pady=5,rowspan=1)
        
        
        button = tk.Button(self,
                           text="Rozpocznij",
                           command=lambda:afterGenerate(self, controller.mydb,controller.font3),
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
                           command=lambda:afterGenerate(self,controller.mydb,controller.font3),
                           pady=11,
                           
                           width=15,
                           bg='Tomato',
                           font = controller.title_font)
        button2.grid(row=3,column=2,sticky="W",pady=30,padx=50)

        button3 = tk.Button(self,
                           text="Zalicz",
                           command=lambda:acceptAnswer(self,controller.mydb,controller.font3),
                           pady=11,
                           padx=5,
                           width=15,
                           bg='#66FF66',
                           font = controller.title_font)
        button3.grid(row=3,column=1,sticky="W",pady=30,padx=50)
