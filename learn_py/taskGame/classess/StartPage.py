import tkinter as tk
from PIL import ImageTk, Image
#pip install pillow

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background='black')
        self.controller = controller
        controller.title("Zadanio-inator")
        
        path=r"########################################"
        image = Image.open(path)
        photo = ImageTk.PhotoImage(image)
        
        self.imgLabel = tk.Label(image=photo)
        self.imgLabel.image = photo
        self.imgLabel.grid(row=0,column=0,columnspan=2)
        
        
        label = tk.Label(self, text="ROFL ROFL ROFL", font=controller.title_font)
        label.grid(row=1,column=0,sticky="S", pady=10)

        button1 = tk.Button(self, text="Zarządzaj zadaniami",command=lambda: controller.show_frame("PageOne"))
        button1.grid(row=2,column=0,sticky="S")
        
        button2 = tk.Button(self, text="Graj",command=lambda: controller.show_frame("PageTwo"))
        button2.grid(row=3,column=0,sticky="S")
                #?
            
        