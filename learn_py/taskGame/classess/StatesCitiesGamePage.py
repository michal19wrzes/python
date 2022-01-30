import tkinter as tk
class StatesCitiesGamePage(tk.Frame):
    from ..defs.statesCitiesTaskGenerate import statesCitiesTaskGenerate

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background='black')      
        self.controller = controller
        
        label = tk.Label(self, text="GRA PAŃSTWA-MIASTA",width=25, font=controller.title_font)
        label.grid(row=0, column=0 ,sticky="S", pady=30,padx=20)
        txtArea = tk.Text(self,width=40, height=20, font=controller.title_font,background='gray')
        txtArea.grid(sticky="wn", row=2,column=1, padx=5, pady=5,columnspan=4,rowspan=4)
        button = tk.Button(self,
                           text="Generuj losowe zadanie",
                           command=lambda: self.statesCitiesTaskGenerate(txtArea),
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
                           padx=5,
                           width=25,
                           bg='violet',
                           font = controller.title_font)
        button1.grid(row=3,column=0,sticky="S",pady=30,padx=50)
