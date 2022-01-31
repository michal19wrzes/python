import tkinter as tk

class UserManagePage(tk.Frame):
    from ..defs.updateUser import updateUser
    from ..defs.showUsersOff import showUsersOff
    from ..defs.showUsersOn import showUsersOn
    from ..defs.changeUserStatus import changeUserStatus
    from ..defs.showUsers import showUsers
    from ..defs.addUser import addUser
    from ..defs.delUser import delUser
    from ..defs.clearOutput import clearOutput
    from ..defs.resetPoints import resetPoints
    
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent,background='black')
        self.controller = controller
        
        frame = tk.Frame(self,borderwidth=4)  
        frame.grid(row=0, column=1 )
        frame.config(background='black')
        
        userEntry = tk.Text(self, width=15,height=1) 
        userEntry.grid(row=2,column=1,padx=5, pady=5) 
        userEntry.config(font=controller.font3)
        
        userLabel = tk.Label(self,text='Wprowadź nazwę gracza:') 
        userLabel.grid(sticky="N", row=1, column=1, padx=5, pady=5)
        userLabel.config(font=controller.font2)

        self.idUserEntry = tk.Text(self, width=15,height=1)   
        self.idUserEntry.grid(sticky="N",row=2,column=2,padx=5, pady=5)
        self.idUserEntry.config(font=controller.font3)
        
        idUserLabel = tk.Label(self,text='Wprowadź ID gracza:') 
        idUserLabel.grid(sticky="N", row=1, column=2, padx=5, pady=5)
        idUserLabel.config(font=controller.font2)

        #BUTTONS
        #show Users button
        showUsersButton = tk.Button(self,text='Pokaż graczy',
                                    command=lambda: self.showUsers(controller.mydb,txtArea))
        showUsersButton.grid(row=3,column=0)
        showUsersButton.config(background='green', foreground='#FFFF00', font=controller.font2,width=20,pady=5,padx=5,height=1)
        
        #show ON
        showUsersOnButton = tk.Button(self,text='Pokaż włączonych graczy',
                                      command=lambda: self.showUsersOn(controller.mydb,txtArea))
        showUsersOnButton.grid(row=3,column=1)
        showUsersOnButton.config(background='green', foreground='#FFFF00', font=controller.font2,width=20,pady=5,padx=5,height=1)
        
        #show OFF
        showUsersOffButton = tk.Button(self,text='Pokaż wyłączonych graczy',
                                       command=lambda: self.showUsersOff(controller.mydb,txtArea))
        showUsersOffButton.grid(row=3,column=2)
        showUsersOffButton.config(background='green', foreground='#FFFF00', font=controller.font2,width=20,pady=5,padx=5,height=1)
        
        #add User button
        addUserButton = tk.Button(self,text='Dodaj gracza',
                                  command=lambda: self.addUser(controller.mydb,userEntry))
        addUserButton.grid(row=4,column=0)
        addUserButton.config(background='blue', foreground='#FFFF00', font=controller.font2,width=20,pady=5,padx=5,height=1)
        
        #delete User by id button
        delUserButton = tk.Button(self,text='Usuń gracza po ID',
                                  command=lambda: self.delUser(controller.mydb,idUserEntry))
        delUserButton.grid(row=4,column=3)
        delUserButton.config(background='red', foreground='#FFFF00', font=controller.font2,width=20,pady=5,padx=5,height=1)
        
        #clear out/in area button
        clearEntryButton = tk.Button(self,text='Wyczyść out/in',
                                     command=lambda: self.clearOutput(txtArea,userEntry,self.idUserEntry))
        clearEntryButton.grid(row=5,column=3)
        clearEntryButton.config(background='gray', foreground='#FFFF00', font=controller.font2,width=20,pady=5,padx=5,height=1)
        #reset points button
        resetPointsButton = tk.Button(self,text='Resetuj punkty',
                                     command=lambda: self.resetPoints(controller.mydb))
        resetPointsButton.grid(row=5,column=1)
        resetPointsButton.config(background='gray', foreground='#FFFF00', font=controller.font2,width=20,pady=5,padx=5,height=1)
        
        #change status (on/off) button
        changeStatusButton = tk.Button(self,text='Włącz/Wyłącz gracza po ID',
                                       command=lambda: self.changeUserStatus(controller.mydb,self.idUserEntry))
        changeStatusButton.grid(row=4,column=1)
        changeStatusButton.config(background='blue', foreground='#FFFF00', font=controller.font2,width=20,pady=5,padx=5,height=1)
        

        #change User params button
        updateUserButton = tk.Button(self,text='Modyfikuj gracza',
                                     command=lambda: self.updateUser(controller.mydb,userEntry,idUserEntry))
        updateUserButton.grid(sticky="N",row=4,column=2)
        updateUserButton.config(background='blue', foreground='#FFFF00', font=controller.font2,width=20,pady=5,padx=5,height=1)
      

        #back to menu button
        backButton = tk.Button(self, text="Wróć do menu",
                                command=lambda: controller.show_frame("MenuPage"))
        backButton.grid(row=5,column=2)
        backButton.config(font=controller.font2,width=20,pady=5,padx=5,height=1)

        #output big textfield area 
        txtArea = tk.Text(self,width=100, height=20, font=controller.title_font,background='gray')
        txtArea.grid(sticky="wn", row=0,column=0, padx=5, pady=5,columnspan=4)
        