import tkinter as tk
class GamesPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background='#14285c')      
        self.controller = controller
        
        label = tk.Label(self, text="Wybierz tryb",width=25, font=controller.title_font)
        label.grid(row=0, column=0 ,sticky="S", pady=30,padx=20)
        
        button1 = tk.Button(self,
                           text="Skojarzenia",
                           command=lambda: controller.show_frame("AssociateGamePage"),
                           pady=30,
                           padx=5,
                           width=25,
                           bg='violet',
                           font = controller.title_font)
        button1.grid(row=1, column=0,sticky="S",pady=30,padx=5)
        
        button2 = tk.Button(self,
                           text="Państwa-Miasta",
                           command=lambda: controller.show_frame("StatesCitiesGamePage"),
                           pady=30,
                           padx=5,
                           width=25,
                           bg='violet',
                           font = controller.title_font)
        button2.grid(row=2, column=0,sticky="S",pady=30,padx=5)

        button3 = tk.Button(self,
                           text="Cofnij do menu",
                           command=lambda: controller.show_frame("MenuPage"),
                           pady=30,
                           padx=5,
                           width=25,
                           bg='violet',
                           font = controller.title_font)
        button3.grid(row=3,column=0,sticky="S",pady=30,padx=50)

