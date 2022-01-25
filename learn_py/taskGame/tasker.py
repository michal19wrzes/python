#testing mysql + tk
#python -m taskGame.tasker
import tkinter as tk
from tkinter import font as tkFont  # for convenience
import mysql.connector
import time

mydb = mysql.connector.connect(host="localhost",user="root",passwd="root",database="corobic_db")

class SampleApp(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        
        self.title_font = tkFont.Font(family='Courier', size=13, weight='bold')
        
        mainFrame = tk.Frame(self,borderwidth=4)
        mainFrame.grid(row=0, column=1)
        mainFrame.config(background='black')
        
        self.frames = {}
        for F in (StartPage, PageOne, PageTwo): #?
            page_name = F.__name__
            frame = F(parent=mainFrame, controller=self) #?
            self.frames[page_name] = frame
            
            frame.grid(row=0,column=0, sticky="nsew")
        self.show_frame("StartPage")            #?
    def show_frame(self,page_name):
        frame = self.frames[page_name]
        frame.tkraise()
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page", font=controller.title_font)
        label.grid(sticky="N", pady=10)

        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
        button2.grid(row=0,column=1)
        button1.grid(row=0,column=0)        #?
            
        
class PageOne(tk.Frame):
    from .defs.sortPriority import sortPriority
    from .defs.randomTask import randomTask
    from .defs.updateTask import updateTask
    from .defs.showTOffButon import showTOffButon
    from .defs.showTOnButon import showTOnButon
    from .defs.changeStatus import changeStatus
    from .defs.showTButon import showTButon
    from .defs.addTButon import addTButon
    from .defs.delTButon import delTButon
    from .defs.clearOutput import clearOutput
    
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is menu", font=controller.title_font)
        button = tk.Button(self, text="Go to the start page",
                                command=lambda: controller.show_frame("StartPage"))
        button.grid()
        frame = tk.Frame(self,borderwidth=4)  
        frame.grid(row=0, column=1 )
        frame.config(background='black')
        
        taskEntry = tk.Entry(self, width=40) 
        taskEntry.grid(row=2,column=0,padx=5, pady=5) 
        taskLabel = tk.Label(self,text='Wprowadź zadanie:') 
        taskLabel.grid(sticky="N", row=1, column=0, padx=5, pady=5)

        priorityEntry = tk.Entry(self, width=40)   
        priorityEntry.grid(sticky="N",row=2,column=1,padx=5, pady=5)
        priorityLabel = tk.Label(self,text='Wprowadź priorytet (1-100):') 
        priorityLabel.grid(sticky="N", row=1, column=1, padx=5, pady=5)

        statusEntry = tk.Entry(self, width=40)   
        statusEntry.grid(sticky="N",row=2,column=2,padx=5, pady=5)
        statusLabel = tk.Label(self,text='Wprowadź status (1-ON | 0-OFF):') 
        statusLabel.grid(sticky="N", row=1, column=2, padx=5, pady=5) 

        idTaskEntry = tk.Entry(self, width=40)   
        idTaskEntry.grid(sticky="N",row=2,column=3,padx=5, pady=5)
        idTaskLabel = tk.Label(self,text='Wprowadź ID zadania:') 
        idTaskLabel.grid(sticky="N", row=1, column=3, padx=5, pady=5) 

        #BUTTONS
        #show tasks button
        showTButton = tk.Button(self,text='Pokaż pytania', command=lambda: self.showTButon(mydb,txtArea))
        showTButton.grid(row=3,column=0)
        showTButton.config(background='green', foreground='#FFFF00')
        #show ON
        showTOnButton = tk.Button(self,text='Pokaż włączone', command=lambda: self.showTOnButon(mydb,txtArea))
        showTOnButton.grid(row=3,column=1)
        showTOnButton.config(background='green', foreground='#FFFF00')
        #show OFF
        showTOffButton = tk.Button(self,text='Pokaż wyłączone', command=lambda: self.showTOffButon(mydb,txtArea))
        showTOffButton.grid(row=3,column=2)
        showTOffButton.config(background='green', foreground='#FFFF00')
        #add task button
        addTButton = tk.Button(self,text='Dodaj zadanie', command=lambda: self.addTButon(mydb,taskEntry,statusEntry,priorityEntry))
        addTButton.grid(row=4,column=0)
        addTButton.config(background='blue', foreground='#FFFF00')
        #delete task by id button
        delTButton = tk.Button(self,text='Usuń zadanie po ID', command=lambda: self.delTButon(mydb,idTaskEntry))
        delTButton.grid(row=4,column=3)
        delTButton.config(background='red', foreground='#FFFF00')
        #clear out/in area button
        clearEntryButton = tk.Button(self,text='Wyczyść out/in', command=lambda: self.clearOutput(txtArea,taskEntry,priorityEntry,statusEntry,idTaskEntry))
        clearEntryButton.grid(row=5,column=3)
        clearEntryButton.config(background='gray', foreground='#FFFF00')
        #change status (on/off) button
        changeStatusButton = tk.Button(self,text='Włącz/Wyłącz zadanie', command=lambda: self.changeStatus(mydb,idTaskEntry))
        changeStatusButton.grid(row=4,column=1)
        changeStatusButton.config(background='blue', foreground='#FFFF00')

        #change task params button
        updateTaskButton = tk.Button(self,text='Modyfikuj zadanie', command=lambda: self.updateTask(mydb,taskEntry,priorityEntry,statusEntry,idTaskEntry))
        updateTaskButton.grid(sticky="N",row=4,column=2)
        updateTaskButton.config(background='blue', foreground='#FFFF00')

        #random task button
        randomTaskButton = tk.Button(self,text='Losowe zadanie', command=lambda: self.randomTask(mydb,txtArea))
        randomTaskButton.grid(sticky="N",row=5,column=0)
        randomTaskButton.config(background='green', foreground='#FFFF00')

        #sort order priority
        sortPriorityTaskButton = tk.Button(self,text='Od najważniejszego', command=lambda:self.sortPriority(mydb,txtArea))
        sortPriorityTaskButton.grid(sticky="N",row=3,column=3)
        sortPriorityTaskButton.config(background='green', foreground='#FFFF00')
        #sort order priority
        backButton = tk.Button(self, text="Wróć do menu",
                                command=lambda: controller.show_frame("StartPage"))
        backButton.grid(row=5,column=2)

        #output big textfield area 
        txtArea = tk.Text(self,width=100, height=20, font=controller.title_font)
        txtArea.grid(sticky="wn", row=0,column=0, padx=5, pady=5,columnspan=4)
        
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)      
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.grid(pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid()

    
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
    mydb.close()

