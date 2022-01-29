from tkinter import *
import tkinter as tk
def clearOutput(self,txtArea,taskEntry,idTaskEntry,priorityEntry=False,statusEntry=False):
    #delete data from out/in in textfield
    txtArea.delete('1.0',END)
    taskEntry.delete(0,END)
    if priorityEntry:
        priorityEntry.delete(0,END)
    else: pass
    if statusEntry:
        statusEntry.delete(0,END)
    else: pass   
    
    idTaskEntry.delete(0,END)