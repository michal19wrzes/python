import tkinter as tk
from PIL import ImageTk, Image
#pip install pillow

class StartPage(tk.Frame):



    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background='black')
        self.controller = controller
        controller.title("Zadanio-inator")
        controller.resizable(False,False)
        
        path=r"C:\\Users\\48791\\Desktop\\pythonowe\\learn_py\\taskGame\\img\\logo.jpg"
        image = Image.open(path)
        photo = ImageTk.PhotoImage(image)
        
        self.imgLabel = tk.Label(image=photo)
        self.imgLabel.image = photo
        self.imgLabel.grid(row=0,column=0,columnspan=2,sticky="E",padx=60)
        
        
        
        self.label = tk.Label(self, text="ROFL ROFL ROFL",width=25, font=controller.title_font)
        self.label.grid(row=0, column=0 ,sticky="S", pady=30,padx=20)

        
        
        
        self.button2 = tk.Button(self,
                            font = controller.title_font,
                            bg="violet", text="Graj",
                            command=lambda: controller.show_frame("PageTwo"),
                            pady=30,
                            width=25,
                            padx=5)
        self.button2.grid(row=1, column=0,sticky="S",pady=30,padx=5)
                #?
        
        self.button1 = tk.Button(self,bg="violet",
                            text="Zarządzaj zadaniami",
                            command=lambda: controller.show_frame("PageOne"),
                            pady=30,
                            padx=5,
                            width=25,
                            font = controller.title_font)
                            
        self.button1.grid(row=2,column=0,sticky="S",pady=30,padx=50)    
        
        self.button3 = tk.Button(self,
                                 font = controller.title_font,
                                 bg="violet",
                                 text="wylacz zdjecie",
                                 command=lambda: self.imgLabel.destroy(),
                                 pady=30,
                                 width=25,
                                 padx=5)
        self.button3.grid(row=3, column=0,sticky="S",pady=30,padx=5)