from tkinter import *
def clearOutput(self,txtArea,taskEntry,priorityEntry,statusEntry,idTaskEntry):
    #delete data from out/in in textfield
    txtArea.delete('1.0',END)
    taskEntry.delete(0,END)
    priorityEntry.delete(0,END)
    statusEntry.delete(0,END)
    idTaskEntry.delete(0,END)