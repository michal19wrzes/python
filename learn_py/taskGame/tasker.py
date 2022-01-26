import tkinter as tk
from tkinter import font as tkFont
from .classess.StartPage import StartPage
from .classess.PageOne import PageOne
from .classess.PageTwo import PageTwo
import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="root",database="corobic_db")
class SampleApp(tk.Tk):  
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)      
        self.title_font = tkFont.Font(family='Courier', size=13, weight='bold')
        self.mydb = mydb
        mainFrame = tk.Frame(self,borderwidth=4)
        mainFrame.grid(row=0, column=1)
        mainFrame.config(background='black')
        
        self.frames = {}
        for F in (StartPage, PageOne, PageTwo): #?
            page_name = F.__name__
            frame = F(parent=mainFrame, controller=self) #?
            self.frames[page_name] = frame
            
            frame.grid(row=0,column=0, sticky="nsew")
        self.show_frame("StartPage")
    def show_frame(self,page_name):
        frame = self.frames[page_name]
        frame.tkraise()
    
  
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
print("to sie dzieje")
mydb.close()


    

