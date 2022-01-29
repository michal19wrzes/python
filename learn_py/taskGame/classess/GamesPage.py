import tkinter as tk
class GamesPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)      
        self.controller = controller
        label = tk.Label(self, text="Wybierz tryb", font=controller.title_font)
        label.grid(pady=10)
        button = tk.Button(self, text="Wróć do menu",
                           command=lambda: controller.show_frame("MenuPage"))
        button.grid()
