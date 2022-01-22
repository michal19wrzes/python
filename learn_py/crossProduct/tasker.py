#testing mysql + tkinter
from tkinter import * 
import mysql.connector
import time

mydb = mysql.connector.connect(host="localhost",user="root",passwd="root",database="corobic_db")

root = Tk()  
root.resizable(width=False, height=True)

#DEFS
def showQOffButton():
#action after click 'show task' button
  clearOutput()
  query="SELECT task_id,task_title,task_status,task_priority FROM tasks where task_status = 0"
  f = ""
  cursor = mydb.cursor()
  cursor.execute(query)
  for (task_id,task_title,task_status,task_priority) in cursor:
    f = f + "{}  {}  Status:{}  Priorytet:{}\n".format(task_id,task_title,task_status,task_priority)
  cursor.close()  
  txt.insert('2.0',f) #na początek
    
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

def showQOnButton():
#action after click 'show task' button
  clearOutput()
  query="SELECT task_id,task_title,task_status,task_priority FROM tasks where task_status = 1"
  f = ""
  cursor = mydb.cursor()
  cursor.execute(query)
  for (task_id,task_title,task_status,task_priority) in cursor:
    f = f + "{}  {}  Status:{}  Priorytet:{}\n".format(task_id,task_title,task_status,task_priority)
  cursor.close()  
  txt.insert('2.0',f) #na początek
  
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
  txt.insert('2.0',f) #na początek
  
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
#delete data from output in textfield
    txt.delete('1.0',END)
    
    
#ENTRY
frame = Frame(root,borderwidth=4)  
frame.grid(row=0, column=1 )
frame.config(background='black')

taskEntry = Entry(frame, width=40) 
taskEntry.grid(sticky=W,row=2,column=1,padx=5, pady=5) 
taskLabel = Label(frame,text='Wprowadź zadanie:') 
taskLabel.grid(sticky=E, row=1, column=1, padx=5, pady=5)

priorityEntry = Entry(frame, width=40)   
priorityEntry.grid(sticky=E,row=4,column=1,padx=5, pady=5)
priorityLabel = Label(frame,text='Wprowadź priorytet (1-100):') 
priorityLabel.grid(sticky=E, row=3, column=1, padx=5, pady=5)

statusEntry = Entry(frame, width=40)   
statusEntry.grid(sticky=E,row=6,column=1,padx=5, pady=5)
statusLabel = Label(frame,text='Wprowadź status (1-ON | 0-OFF):') 
statusLabel.grid(sticky=E, row=5, column=1, padx=5, pady=5) 

idTaskEntry = Entry(frame, width=40)   
idTaskEntry.grid(sticky=E,row=8,column=1,padx=5, pady=5)
idTaskLabel = Label(frame,text='Wprowadź ID zadania:') 
idTaskLabel.grid(sticky=E, row=7, column=1, padx=5, pady=5) 

#BUTTONS
#show tasks button
showQButton = Button(frame,text='Pokaż pytania', command=showQButton)
showQButton.grid(row=4,column=2)
showQButton.config(background='blue', foreground='#FFFF00')
#show ON
showQOnButton = Button(frame,text='Pokaż włączone', command=showQOnButton)
showQOnButton.grid(row=5,column=2)
showQOnButton.config(background='blue', foreground='#FFFF00')
#show OFF
showQOffButton = Button(frame,text='Pokaż wyłączone', command=showQOffButton)
showQOffButton.grid(row=7,column=2)
showQOffButton.config(background='blue', foreground='#FFFF00')
#add task button
addQButton = Button(frame,text='Dodaj zadanie', command=addQButton)
addQButton.grid(row=3,column=2)
addQButton.config(background='blue', foreground='#FFFF00')
#delete task by id button
delQButton = Button(frame,text='Usuń zadanie po ID', command=delQButton)
delQButton.grid(row=2,column=2)
delQButton.config(background='blue', foreground='#FFFF00')
#clear output area button
clearEntryButton = Button(frame,text='Wyczyść output', command=clearOutput)
clearEntryButton.grid(row=1,column=2)
clearEntryButton.config(background='blue', foreground='#FFFF00')
#change status (on/off) button
changeStatusButton = Button(frame,text='Włącz/Wyłącz zadanie', command=changeStatus)
changeStatusButton.grid(row=6,column=2)
changeStatusButton.config(background='blue', foreground='#FFFF00')

#output big textfield area 
txt = Text(frame,width=100, height=20)
txt.grid(sticky=W+N, row=0,column=0, padx=5, pady=5) 

root.mainloop()
mydb.close()
