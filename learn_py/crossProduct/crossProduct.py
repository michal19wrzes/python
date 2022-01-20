#testing mysql + tkinter
from tkinter import * 
import mysql.connector
import time

mydb = mysql.connector.connect(host="localhost",user="mysql_user",passwd="password",database="krzyzowka")

root = Tk()  
root.resizable(width=False, height=True)

# FUNKCJE OBSŁUGI OKNA
def showQButton() :
#action after click 'show question' button
  query="SELECT question_id,data,answer FROM question"
  f = ""
  cursor = mydb.cursor()
  cursor.execute(query)
  for (question_id,id,name) in cursor:
    f = f + "{} {} = {}\n".format(question_id,id,name);  
  cursor.close()  
  txt.insert('2.0',f) #na początek
def addQButton():
#action after click 'add question' button
    query="INSERT INTO question(data,answer) VALUES ('{}','{}')".format(questionEntry.get(),answerEntry.get())
    cursor = mydb.cursor()
    cursor.execute(query)
    mydb.commit()
    
def delQButton():
#action after click 'delete button' --> for answer
    query="DELETE FROM question WHERE answer='{}'".format(answerEntry.get())
    cursor = mydb.cursor()
    cursor.execute(query)
    mydb.commit()
def clearOutput():
#delete data from output in textfield
    txt.delete('1.0',END)
 


################ PROGRAM GŁÓWNY #######################

#NAPIS
#haj = Label(root, text='Witaj świecie') 
#haj.grid(row=0,column=0) 

#RAMKA
frame = Frame(root,borderwidth=4)  
frame.grid(row=0, column=1 )
frame.config(background='black')

#NAPIS W RAMCE
 


questionEntry = Entry(frame, width=40) 
questionEntry.grid(sticky=W,row=2,column=1,padx=5, pady=5) 
questionLabel = Label(frame,text='Wprowadź pytanie:') 
questionLabel.grid(sticky=E, row=1, column=1, padx=5, pady=5)

answerEntry = Entry(frame, width=40)   
answerEntry.grid(sticky=E,row=4,column=1,padx=5, pady=5)
answerLabel = Label(frame,text='Wprowadź odpowiedź:') 
answerLabel.grid(sticky=E, row=3, column=1, padx=5, pady=5) 

#Pokaż pytania button
showQButton = Button(frame,text='Pokaż pytania', command=showQButton)
showQButton.grid(row=4,column=2)
showQButton.config(background='blue', foreground='#FFFF00')
#Dodaj pytanie button
addQButton = Button(frame,text='Dodaj pytanie', command=addQButton)
addQButton.grid(row=3,column=2)
addQButton.config(background='blue', foreground='#FFFF00')
#Usun pytanie po hasle button
delQButton = Button(frame,text='Usuń pytanie po haśle', command=delQButton)
delQButton.grid(row=2,column=2)
delQButton.config(background='blue', foreground='#FFFF00')
#Wyczysc output button
clearEntryButton = Button(frame,text='Wyczyść output', command=clearOutput)
clearEntryButton.grid(row=1,column=2)
clearEntryButton.config(background='blue', foreground='#FFFF00')




#POLE TEKSTOWE WIELOLINIOWE 
txt = Text(frame,width=100, height=20)
txt.grid(sticky=W+N, row=0,column=0, padx=5, pady=5) 

root.mainloop()
mydb.close()
