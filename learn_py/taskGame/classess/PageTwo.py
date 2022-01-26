import tkinter as tk
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)      
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.grid(pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid()
