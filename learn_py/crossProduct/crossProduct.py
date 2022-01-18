#testing mysql + tkinter
from tkinter import * 
import mysql.connector
import time

mydb = mysql.connector.connect(host="localhost",user="mysql_user",passwd="password",database="krzyzowka")

root = Tk()  
root.resizable(width=False, height=True)

# FUNKCJE OBSŁUGI OKNA
def klikniętoPrzycisk() :
  query="SELECT data,answer FROM question"
  f = ""
  cursor = mydb.cursor()
  cursor.execute(query)
  for (id,name) in cursor:
    f = f + "{} = {}\n".format(id,name);  
  cursor.close()  
  txt.insert('2.0',f) #na początek

################ PROGRAM GŁÓWNY #######################

#NAPIS
#haj = Label(root, text='Witaj świecie') 
#haj.grid(row=0,column=0) 

#RAMKA
frame = Frame(root,borderwidth=4)  
frame.grid(row=0, column=1 )
frame.config(background='black')

#NAPIS W RAMCE
#lab1 = Label(frame,text='Ramka1') 
#lab1.grid(sticky=E, row=0, column=0, padx=5, pady=5) 

#POLE INPUT JEDNOLINIOWE 
ent = Entry(frame, width=40)  # pole tekstowe jednoliniowe 
ent.grid(sticky=W,row=1,column=0,padx=5, pady=5) 
ent1 = Entry(frame, width=40)   
ent1.grid(sticky=E,row=1,column=1,padx=5, pady=5) 

#PRZYCISK
przycisk = Button(frame,text='Pokaż pytania', command=klikniętoPrzycisk)
przycisk.grid(row=4,column=1)
przycisk.config(background='blue', foreground='#FFFF00')



#POLE TEKSTOWE WIELOLINIOWE 
txt = Text(frame,width=40, height=5)
txt.grid(sticky=W+N, row=4,column=0, padx=5, pady=5) 

root.mainloop()
mydb.close()
