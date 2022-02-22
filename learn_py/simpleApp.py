import tkinter as tk

class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        
class SecondPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        
        


#tkinter main app
class mainApp(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        
        mainFrame = tk.Frame(self)
        mainFrame.grid(row=0,column=0)
        
        self.frames={}
        for page in (StartPage,SecondPage):
            page_name = page.__name__
            frame = page(parent=mainFrame, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame("StartPage")
        
    def show_frame(self,page_name):
        frame = self.frames[page_name]
        frame.tkraise()
if __name__ == "__main__":
    app = mainApp()
    app.mainloop()
    