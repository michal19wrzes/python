from tkinter import *
import tkinter as tk
def clearOutput(self,txtArea,taskEntry,idTaskEntry=False,priorityEntry=False,statusEntry=False):
    #delete data from out/in in textfield
    txtArea.delete('1.0',END)
    taskEntry.delete('1.0',END)
    if priorityEntry:
        priorityEntry.delete('1.0',END)

    if statusEntry:
        statusEntry.delete('1.0',END)

    if idTaskEntry:
        idTaskEntry.delete('1.0',END)