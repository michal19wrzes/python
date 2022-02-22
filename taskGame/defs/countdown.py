import tkinter as tk

def countdown(self,count):
            self.timeArea.delete('1.0',tk.END)
            self.timeArea.insert('1.0',count)
            
            if count > 0:
            # call countdown again after 1000ms (1s)
                self.after(1000, lambda:countdown(self,count-1))
            
                

            
                
                
