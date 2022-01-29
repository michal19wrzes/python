import tkinter as tk

class UserManagePage(tk.Frame):
    from ..defs.updateTask import updateTask
    from ..defs.showUsersOff import showUsersOff
    from ..defs.showUsersOn import showUsersOn
    from ..defs.changeUserStatus import changeUserStatus
    from ..defs.showUsers import showUsers
    from ..defs.addUser import addUser
    from ..defs.delUser import delUser
    from ..defs.clearOutput import clearOutput
    
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent,background='black')
        self.controller = controller
        
        frame = tk.Frame(self,borderwidth=4)  
        frame.grid(row=0, column=1 )
        frame.config(background='black')
        
        taskEntry = tk.Entry(self, width=40) 
        taskEntry.grid(row=2,column=0,padx=5, pady=5) 
        taskLabel = tk.Label(self,text='Wprowadź nazwę gracza:') 
        taskLabel.grid(sticky="N", row=1, column=0, padx=5, pady=5)

        idTaskEntry = tk.Entry(self, width=40)   
        idTaskEntry.grid(sticky="N",row=2,column=3,padx=5, pady=5)
        idTaskLabel = tk.Label(self,text='Wprowadź ID gracza:') 
        idTaskLabel.grid(sticky="N", row=1, column=3, padx=5, pady=5) 

        #BUTTONS
        #show tasks button
        showTButton = tk.Button(self,text='Pokaż graczy', command=lambda: self.showUsers(controller.mydb,txtArea))
        showTButton.grid(row=3,column=0)
        showTButton.config(background='green', foreground='#FFFF00')
        #show ON
        showTOnButton = tk.Button(self,text='Pokaż włączonych graczy', command=lambda: self.showUsersOn(controller.mydb,txtArea))
        showTOnButton.grid(row=3,column=1)
        showTOnButton.config(background='green', foreground='#FFFF00')
        #show OFF
        showTOffButton = tk.Button(self,text='Pokaż wyłączonych graczy', command=lambda: self.showUsersOff(controller.mydb,txtArea))
        showTOffButton.grid(row=3,column=2)
        showTOffButton.config(background='green', foreground='#FFFF00')
        #add task button
        addTButton = tk.Button(self,text='Dodaj gracza', command=lambda: self.addUser(controller.mydb,taskEntry))
        addTButton.grid(row=4,column=0)
        addTButton.config(background='blue', foreground='#FFFF00')
        #delete task by id button
        delTButton = tk.Button(self,text='Usuń gracza po ID', command=lambda: self.delUser(controller.mydb,idTaskEntry))
        delTButton.grid(row=4,column=3)
        delTButton.config(background='red', foreground='#FFFF00')
        #clear out/in area button
        clearEntryButton = tk.Button(self,text='Wyczyść out/in', command=lambda: self.clearOutput(txtArea,taskEntry,idTaskEntry))
        clearEntryButton.grid(row=5,column=3)
        clearEntryButton.config(background='gray', foreground='#FFFF00')
        #change status (on/off) button
        changeStatusButton = tk.Button(self,text='Włącz/Wyłącz gracza po ID', command=lambda: self.changeUserStatus(controller.mydb,idTaskEntry))
        changeStatusButton.grid(row=4,column=1)
        changeStatusButton.config(background='blue', foreground='#FFFF00')

        #change task params button
        updateTaskButton = tk.Button(self,text='Modyfikuj gracza', command=lambda: self.updateTask(controller.mydb,taskEntry,priorityEntry,statusEntry,idTaskEntry))
        updateTaskButton.grid(sticky="N",row=4,column=2)
        updateTaskButton.config(background='blue', foreground='#FFFF00')

        #back to menu button
        backButton = tk.Button(self, text="Wróć do menu",
                                command=lambda: controller.show_frame("MenuPage"))
        backButton.grid(row=5,column=2)

        #output big textfield area 
        txtArea = tk.Text(self,width=100, height=20, font=controller.title_font,background='gray')
        txtArea.grid(sticky="wn", row=0,column=0, padx=5, pady=5,columnspan=4)
        