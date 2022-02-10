import tkinter as tk

class GameHistoryPage(tk.Frame):
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
        tk.Frame.__init__(self, parent,background='#14285c')
        self.controller = controller
        
        frame = tk.Frame(self,borderwidth=4)  
        frame.grid(row=0, column=1 )
        frame.config(background='#14285c')
       
        #BUTTONS
        #show Users button
        showUsersButton = tk.Button(self,text='Pokaż historię',
                                    command=lambda: self.showUsers(controller.mydb,txtArea))
        showUsersButton.grid(row=5,column=0)
        showUsersButton.config(background='green', foreground='#FFFF00', font=controller.font2,width=25,pady=15,padx=5,height=2)
        
       
        #clear out/in area button
        clearEntryButton = tk.Button(self,text='Wyczyść out/in',
                                     command=lambda: self.clearOutput(txtArea,userEntry,self.idUserEntry))
        clearEntryButton.grid(row=5,column=2)
        clearEntryButton.config(background='gray', foreground='#FFFF00', font=controller.font2,width=25,pady=15,padx=5,height=2)
        #reset points button
        resetPointsButton = tk.Button(self,text='Resetuj punkty',
                                     command=lambda: self.resetPoints(controller.mydb))
        resetPointsButton.grid(row=5,column=1)
        resetPointsButton.config(background='gray', foreground='#FFFF00', font=controller.font2,width=25,pady=15,padx=5,height=2)
        
        
        #back to menu button
        backButton = tk.Button(self, text="Cofnij",
                                command=lambda: controller.show_frame("StatesCitiesGamePage"))
        backButton.grid(row=5,column=3)
        backButton.config(font=controller.font2,width=25,pady=15,padx=5,height=2)

        #output big textfield area 
        txtArea = tk.Text(self,width=110, height=20, font=controller.title_font,background='#94bdff')
        txtArea.grid(sticky="wn", row=0,column=0, padx=5, pady=20,columnspan=4)
        