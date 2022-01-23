﻿#testing mysql + tkinter
#python -m taskGame.tasker
from .defs.sortPriority import sortPriority
from .defs.randomTask import randomTask
from .defs.updateTask import updateTask
from .defs.showTOffButon import showTOffButon

from tkinter import * 
from tkinter import font as tkFont  # for convenience
import mysql.connector
import time

mydb = mysql.connector.connect(host="localhost",user="root",passwd="root",database="corobic_db")

root = Tk()  
root.resizable(width=False, height=True)
helv36 = tkFont.Font(family='Courier', size=13, weight='bold')


def insertPriority():
    #insert priority querry result to output entry
    sortPriority(mydb,txtArea)
def insertRandomTask():
    #insert randomTask querry result to output entry
    randomTask(mydb,txtArea)#na początek
def executeUpdateTask():
    #update task by the entered params where id = idTaskEntry
    updateTask(mydb,taskEntry,priorityEntry,statusEntry,idTaskEntry)

def executeShowTOffButon():
    showTOffButon(mydb,txtArea)
    
def changeStatus():
    #change status of task
    query="SELECT task_status FROM tasks where task_id ={}".format(idTaskEntry.get())
    cursor = mydb.cursor()
    cursor.execute(query)
    for task_status in cursor:
        if task_status[0] == 1:
            query="UPDATE tasks SET task_status=0 WHERE task_id={}".format(idTaskEntry.get())
        elif task_status[0] == 0:
            query="UPDATE tasks SET task_status=1 WHERE task_id={}".format(idTaskEntry.get())
        cursor.execute(query)
        mydb.commit()       
    cursor.close()  

def showTOnButton():
#action after click 'show task' button
  clearOutput()
  query="SELECT task_id,task_title,task_status,task_priority FROM tasks where task_status = 1"
  f = ""
  cursor = mydb.cursor()
  cursor.execute(query)
  for (task_id,task_title,task_status,task_priority) in cursor:
    f = f + "{}  {}  Status:{}  Priorytet:{}\n".format(task_id,task_title,task_status,task_priority)
  cursor.close()  
  txtArea.insert('2.0',f) #na początek
  
def showQButton():
#action after click 'show task' button
  clearOutput()
  query="SELECT task_id,task_title,task_status,task_priority FROM tasks"
  f = ""
  cursor = mydb.cursor()
  cursor.execute(query)
  for (task_id,task_title,task_status,task_priority) in cursor:
    f = f + "{}  {}  Status:{}  Priorytet:{}\n".format(task_id,task_title,task_status,task_priority);  
  cursor.close()  
  txtArea.insert('2.0',f) #na początek
  
def addQButton():
#action after click 'add task' button
    query="INSERT INTO tasks(task_title,task_status,task_priority) VALUES ('{}',{},{})".format(taskEntry.get(),statusEntry.get(),priorityEntry.get())
    cursor = mydb.cursor()
    cursor.execute(query)
    mydb.commit()
    cursor.close()
    
def delQButton():
#action after click 'delete button' 
    query="DELETE FROM tasks WHERE task_id={}".format(idTaskEntry.get())
    cursor = mydb.cursor()
    cursor.execute(query)
    mydb.commit()
    cursor.close()
    
def clearOutput():
#delete data from out/in in textfield
    txtArea.delete('1.0',END)
    taskEntry.delete(0,END)
    priorityEntry.delete(0,END)
    statusEntry.delete(0,END)
    idTaskEntry.delete(0,END)
    
    
    
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
showQButton = Button(frame,text='Pokaż pytania', command=showQButton)
showQButton.grid(row=3,column=0)
showQButton.config(background='green', foreground='#FFFF00')
#show ON
showTOnButton = Button(frame,text='Pokaż włączone', command=showTOnButton)
showTOnButton.grid(row=3,column=1)
showTOnButton.config(background='green', foreground='#FFFF00')
#show OFF
showTOffButton = Button(frame,text='Pokaż wyłączone', command=executeShowTOffButon)
showTOffButton.grid(row=3,column=2)
showTOffButton.config(background='green', foreground='#FFFF00')
#add task button
addQButton = Button(frame,text='Dodaj zadanie', command=addQButton)
addQButton.grid(row=4,column=0)
addQButton.config(background='blue', foreground='#FFFF00')
#delete task by id button
delQButton = Button(frame,text='Usuń zadanie po ID', command=delQButton)
delQButton.grid(row=4,column=3)
delQButton.config(background='red', foreground='#FFFF00')
#clear out/in area button
clearEntryButton = Button(frame,text='Wyczyść out/in', command=clearOutput)
clearEntryButton.grid(row=5,column=3)
clearEntryButton.config(background='gray', foreground='#FFFF00')
#change status (on/off) button
changeStatusButton = Button(frame,text='Włącz/Wyłącz zadanie', command=changeStatus)
changeStatusButton.grid(row=4,column=1)
changeStatusButton.config(background='blue', foreground='#FFFF00')

#change task params button
updateTaskButton = Button(frame,text='Modyfikuj zadanie', command=executeUpdateTask)
updateTaskButton.grid(sticky=N,row=4,column=2)
updateTaskButton.config(background='blue', foreground='#FFFF00')

#random task button
randomTaskButton = Button(frame,text='Losowe zadanie', command=insertRandomTask)
randomTaskButton.grid(sticky=N,row=5,column=0)
randomTaskButton.config(background='green', foreground='#FFFF00')

#sort order priority
sortPriorityTaskButton = Button(frame,text='Od najważniejszego', command=insertPriority)
sortPriorityTaskButton.grid(sticky=N,row=3,column=3)
sortPriorityTaskButton.config(background='green', foreground='#FFFF00')

#output big textfield area 
txtArea = Text(frame,width=100, height=20, font=helv36)
txtArea.grid(sticky=W+N, row=0,column=0, padx=5, pady=5,columnspan=4) 

root.mainloop()
mydb.close()