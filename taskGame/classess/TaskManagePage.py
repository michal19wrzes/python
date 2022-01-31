import tkinter as tk

class TaskManagePage(tk.Frame):
    from ..defs.sortTaskPriority import sortTaskPriority
    from ..defs.randomTask import randomTask
    from ..defs.updateTask import updateTask
    from ..defs.showTasksOff import showTasksOff
    from ..defs.showTasksOn import showTasksOn
    from ..defs.changeTaskStatus import changeTaskStatus
    from ..defs.showTasks import showTasks
    from ..defs.addTask import addTask
    from ..defs.delTask import delTask
    from ..defs.clearOutput import clearOutput
    
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent,background='black')
        self.controller = controller
        
        frame = tk.Frame(self,borderwidth=4)  
        frame.grid(row=0, column=1 )
        frame.config(background='black')
        
        taskEntry =tk.Text(self, width=15,height=1)
        taskEntry.grid(row=2,column=0,padx=5, pady=5) 
        taskEntry.config(font=controller.font3)
        
        taskLabel = tk.Label(self,text='Wprowadź zadanie:') 
        taskLabel.grid(sticky="NS", row=1, column=0, padx=5, pady=5)
        taskLabel.config(font=controller.font2)
        
        priorityEntry = tk.Text(self, width=3,height=1)  
        priorityEntry.grid(sticky="NS",row=2,column=1,padx=5, pady=5)
        priorityEntry.config(font=controller.font3)
        
        priorityLabel = tk.Label(self,text='Wprowadź priorytet (1-100):') 
        priorityLabel.grid(sticky="NS", row=1, column=1, padx=5, pady=5)
        priorityLabel.config(font=controller.font2)

        statusEntry = tk.Text(self, width=15,height=1)   
        statusEntry.grid(sticky="NS",row=2,column=2,padx=5, pady=5)
        statusEntry.config(font=controller.font3)
        
        statusLabel = tk.Label(self,text='Wprowadź status (1-ON | 0-OFF):') 
        statusLabel.grid(sticky="NS", row=1, column=2, padx=5, pady=5) 
        statusLabel.config(font=controller.font2)
        
        idTaskEntry = tk.Text(self, width=2, height=1)   
        idTaskEntry.grid(sticky="NS",row=2,column=3,padx=5, pady=5)       
        idTaskEntry.config(font=controller.font3)

        
        idTaskLabel = tk.Label(self,text='Wprowadź ID zadania:') 
        idTaskLabel.grid(sticky="NS", row=1, column=3, padx=5, pady=5)
        idTaskLabel.config(font=controller.font2)

        #BUTTONS
        #show tasks button
        showTButton = tk.Button(self,text='Pokaż pytania', command=lambda: self.showTasks(controller.mydb,txtArea))
        showTButton.grid(row=3,column=0)
        showTButton.config(background='green', foreground='#FFFF00', font=controller.font2,width=20,pady=5,padx=5,height=1)
        #show ON
        showTOnButton = tk.Button(self,text='Pokaż włączone', command=lambda: self.showTasksOn(controller.mydb,txtArea))
        showTOnButton.grid(row=3,column=1)
        showTOnButton.config(background='green', foreground='#FFFF00', font=controller.font2,width=20,pady=5,padx=5,height=1)
        #show OFF
        showTOffButton = tk.Button(self,text='Pokaż wyłączone', command=lambda: self.showTasksOff(controller.mydb,txtArea))
        showTOffButton.grid(row=3,column=2)
        showTOffButton.config(background='green', foreground='#FFFF00', font=controller.font2,width=20,pady=5,padx=5,height=1)
        #add task button
        addTButton = tk.Button(self,text='Dodaj zadanie', command=lambda: self.addTask(controller.mydb,taskEntry,statusEntry,priorityEntry))
        addTButton.grid(row=4,column=0)
        addTButton.config(background='blue', foreground='#FFFF00', font=controller.font2,width=20,pady=5,padx=5,height=1)
        #delete task by id button
        delTButton = tk.Button(self,text='Usuń zadanie po ID', command=lambda: self.delTask(controller.mydb,idTaskEntry))
        delTButton.grid(row=4,column=3)
        delTButton.config(background='red', foreground='#FFFF00', font=controller.font2,width=20,pady=5,padx=5,height=1)
        #clear out/in area button
        clearEntryButton = tk.Button(self,text='Wyczyść out/in', command=lambda: self.clearOutput(txtArea,taskEntry,priorityEntry,statusEntry,idTaskEntry))
        clearEntryButton.grid(row=5,column=3)
        clearEntryButton.config(background='gray', foreground='#FFFF00', font=controller.font2,width=20,pady=5,padx=5,height=1)
        #change status (on/off) button
        changeStatusButton = tk.Button(self,text='Włącz/Wyłącz zadanie', command=lambda: self.changeTaskStatus(controller.mydb,idTaskEntry))
        changeStatusButton.grid(row=4,column=1)
        changeStatusButton.config(background='blue', foreground='#FFFF00', font=controller.font2,width=20,pady=5,padx=5,height=1)

        #change task params button
        updateTaskButton = tk.Button(self,text='Modyfikuj zadanie', command=lambda: self.updateTask(controller.mydb,taskEntry,priorityEntry,statusEntry,idTaskEntry))
        updateTaskButton.grid(sticky="N",row=4,column=2)
        updateTaskButton.config(background='blue', foreground='#FFFF00', font=controller.font2,width=20,pady=5,padx=5,height=1)

        #random task button
        randomTaskButton = tk.Button(self,text='Losowe zadanie', command=lambda: self.randomTask(controller.mydb,txtArea))
        randomTaskButton.grid(sticky="N",row=5,column=0)
        randomTaskButton.config(background='green', foreground='#FFFF00', font=controller.font2,width=20,pady=5,padx=5,height=1)

        #sort order priority button
        sortPriorityTaskButton = tk.Button(self,text='Od najważniejszego', command=lambda:self.sortTaskPriority(controller.mydb,txtArea))
        sortPriorityTaskButton.grid(sticky="N",row=3,column=3)
        sortPriorityTaskButton.config(background='green', foreground='#FFFF00', font=controller.font2,width=20,pady=5,padx=5,height=1)
        #back to menu button
        backButton = tk.Button(self, text="Wróć do menu",
                                command=lambda: controller.show_frame("MenuPage"))
        backButton.grid(row=5,column=2)
        backButton.config(font=controller.font2,width=20,pady=5,padx=5,height=1)

        #output big textfield area 
        txtArea = tk.Text(self,width=100, height=20, font=controller.title_font,background='gray')
        txtArea.grid(sticky="wn", row=0,column=0, padx=5, pady=5,columnspan=4)
        