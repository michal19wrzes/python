import tkinter as tk
class AssociateGamePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background='green')      
        self.controller = controller
        
        label = tk.Label(self, text="GRA SKOJARZENIA",width=25, font=controller.title_font)
        label.grid(row=0, column=0 ,sticky="S", pady=30,padx=20)
        
        button = tk.Button(self,
                           text="Cofnij",
                           command=lambda: controller.show_frame("GamesPage"),
                           pady=30,
                           padx=5,
                           width=25,
                           bg='violet',
                           font = controller.title_font)
        button.grid(row=2,column=0,sticky="S",pady=30,padx=50)
