#testing mysql + tkinter
#python -m taskGame.tasker
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

from tkinter import * 
from tkinter import font as tkFont  # for convenience
import mysql.connector
import time

mydb = mysql.connector.connect(host="localhost",user="root",passwd="root",database="corobic_db")

root = Tk()  
root.resizable(width=False, height=False)
#font
helv36 = tkFont.Font(family='Courier', size=13, weight='bold')

def executeSortPriority():
    #insert priority querry result to output entry
    executeClearOutput()
    sortPriority(mydb,txtArea)    
def executeRandomTask():
    #insert randomTask querry result to output entry
    randomTask(mydb,txtArea)#na początek  
def executeUpdateTask():
    #update task by the entered params where id = idTaskEntry
    updateTask(mydb,taskEntry,priorityEntry,statusEntry,idTaskEntry)   
def executeShowTOffButon():
    #show disabled tasks
    executeClearOutput()
    showTOffButon(mydb,txtArea)    
def executeShowTOnButon():
    #show enabled tasks
    executeClearOutput()
    showTOnButon(mydb,txtArea)  
def executeChangeStatus():
    #change status (0|1) task 
    changeStatus(mydb,idTaskEntry)  
def executeShowTButon():
    #show all tasks and insert to txtArea
    executeClearOutput()    
    showQButon(mydb,txtArea)  
def executeAddTButon():
    #add task to db
    addTButon(mydb,taskEntry,statusEntry,priorityEntry)  
def executeDelTButon():
    #delete task from db
    delTButon(mydb,idTaskEntry)  
def executeClearOutput():
    #delete inserted data task from output and input textfield
    clearOutput(txtArea,taskEntry,priorityEntry,statusEntry,idTaskEntry)

   
#ENTRYS
frame = Frame(root,borderwidth=4)  
frame.grid(row=0, column=1 )
frame.config(background='black')

taskEntry = Entry(frame, width=40) 
taskEntry.grid(sticky=N,row=2,column=0,padx=5, pady=5) 
taskLabel = Label(frame,text='Wprowadź zadanie:') 
taskLabel.grid(sticky=N, row=1, column=0, padx=5, pady=5)

priorityEntry = Entry(frame, width=40)   
priorityEntry.grid(sticky=N,row=2,column=1,padx=5, pady=5)
priorityLabel = Label(frame,text='Wprowadź priorytet (1-100):') 
priorityLabel.grid(sticky=N, row=1, column=1, padx=5, pady=5)

statusEntry = Entry(frame, width=40)   
statusEntry.grid(sticky=N,row=2,column=2,padx=5, pady=5)
statusLabel = Label(frame,text='Wprowadź status (1-ON | 0-OFF):') 
statusLabel.grid(sticky=N, row=1, column=2, padx=5, pady=5) 

idTaskEntry = Entry(frame, width=40)   
idTaskEntry.grid(sticky=N,row=2,column=3,padx=5, pady=5)
idTaskLabel = Label(frame,text='Wprowadź ID zadania:') 
idTaskLabel.grid(sticky=N, row=1, column=3, padx=5, pady=5) 

#BUTTONS
#show tasks button
showQButton = Button(frame,text='Pokaż pytania', command=executeShowTButon)
showQButton.grid(row=3,column=0)
showQButton.config(background='green', foreground='#FFFF00')
#show ON
showTOnButton = Button(frame,text='Pokaż włączone', command=executeShowTOnButon)
showTOnButton.grid(row=3,column=1)
showTOnButton.config(background='green', foreground='#FFFF00')
#show OFF
showTOffButton = Button(frame,text='Pokaż wyłączone', command=executeShowTOffButon)
showTOffButton.grid(row=3,column=2)
showTOffButton.config(background='green', foreground='#FFFF00')
#add task button
addQButton = Button(frame,text='Dodaj zadanie', command=executeAddTButon)
addQButton.grid(row=4,column=0)
addQButton.config(background='blue', foreground='#FFFF00')
#delete task by id button
delQButton = Button(frame,text='Usuń zadanie po ID', command=executeDelTButon)
delQButton.grid(row=4,column=3)
delQButton.config(background='red', foreground='#FFFF00')
#clear out/in area button
clearEntryButton = Button(frame,text='Wyczyść out/in', command=executeClearOutput)
clearEntryButton.grid(row=5,column=3)
clearEntryButton.config(background='gray', foreground='#FFFF00')
#change status (on/off) button
changeStatusButton = Button(frame,text='Włącz/Wyłącz zadanie', command=executeChangeStatus)
changeStatusButton.grid(row=4,column=1)
changeStatusButton.config(background='blue', foreground='#FFFF00')

#change task params button
updateTaskButton = Button(frame,text='Modyfikuj zadanie', command=executeUpdateTask)
updateTaskButton.grid(sticky=N,row=4,column=2)
updateTaskButton.config(background='blue', foreground='#FFFF00')

#random task button
randomTaskButton = Button(frame,text='Losowe zadanie', command=executeRandomTask)
randomTaskButton.grid(sticky=N,row=5,column=0)
randomTaskButton.config(background='green', foreground='#FFFF00')

#sort order priority
sortPriorityTaskButton = Button(frame,text='Od najważniejszego', command=executeSortPriority)
sortPriorityTaskButton.grid(sticky=N,row=3,column=3)
sortPriorityTaskButton.config(background='green', foreground='#FFFF00')

#output big textfield area 
txtArea = Text(frame,width=100, height=20, font=helv36)
txtArea.grid(sticky=W+N, row=0,column=0, padx=5, pady=5,columnspan=4) 

root.mainloop()
mydb.close()