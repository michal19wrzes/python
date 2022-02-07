import tkinter as tk
from tkinter import font as tkFont

class StartPage(tk.Frame):
    def resetStartTimer(self, entry):
            entry.insert(0,"pozdro")
            
            
            
            
            
            
            
            
            
            
    def __init__(self,parent,controller):
    
        
        
        tk.Frame.__init__(self,parent)
        self.controller = controller
        self.font4 = tkFont.Font(family='Courier',size=30,weight='bold')
        
        self.label = tk.Label(self, text= "Weź liczniku zadziałaj",font=self.font4)
        self.label.grid(row=0,column=0,sticky="N")
        
        self.entry = tk.Entry(self,font=self.font4)
        self.entry.grid(row=1,column=0,sticky="N")
        
        self.button = tk.Button(self,text="Reset/Włącz",
                           font=self.font4,
                           command = lambda:self.resetStartTimer(self.entry))
        self.button.grid(row=2,column=0,sticky="N")
        
        
class SecondPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        
        


#tkinter main app
class mainApp(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        
        
        
        mainFrame = tk.Frame(self)
        mainFrame.grid(row=0,column=0)
        
        self.frames={}
        for page in (StartPage,SecondPage):
            page_name = page.__name__
            frame = page(parent=mainFrame, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame("StartPage")
        
    def show_frame(self,page_name):
        frame = self.frames[page_name]
        frame.tkraise()
if __name__ == "__main__":
    app = mainApp()
    app.mainloop()
    