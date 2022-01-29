import tkinter as tk
from tkinter import font as tkFont
from .classess.MenuPage import MenuPage
from .classess.TaskManagePage import TaskManagePage
from .classess.UserManagePage import UserManagePage
from .classess.GamesPage import GamesPage
from .classess.AssociateGamePage import AssociateGamePage
import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="root",database="corobic_db")
class mainApp(tk.Tk):  
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)      
        self.title_font = tkFont.Font(family='Courier', size=16, weight='bold')
        self.mydb = mydb
        mainFrame = tk.Frame(self,borderwidth=10)
        mainFrame.grid(row=0, column=0)
        mainFrame.config(background='black')
        
        self.frames = {}
        for F in (MenuPage, GamesPage, TaskManagePage,AssociateGamePage,UserManagePage): #?
            page_name = F.__name__
            frame = F(parent=mainFrame, controller=self) #?
            self.frames[page_name] = frame
            
            frame.grid(row=0,column=0, sticky="nsew")
        self.show_frame("MenuPage")
    def show_frame(self,page_name):
        frame = self.frames[page_name]
        frame.tkraise()
    
  
if __name__ == "__main__":
    app = mainApp()
    app.mainloop()

mydb.close()


    

