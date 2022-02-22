from tkinter import *

app = Tk()
app.geometry('200x50')

bt = Button(text='Start',bg='green',fg='white')
bt.pack(fill=BOTH, expand= True,after=True)
#bt.grid()
def mouse_click(mouse):
    if str(mouse.widget.cget('text'))=='Start':
        bt.configure(text='Stop')
        bt['bg'] = 'red'
    else:
        bt.config(text='Start', bg='green')
        for cfg in mouse.widget.keys():
            #positioning in shell
            print(f'{cfg:20}', mouse.widget[cfg])
bt.bind('<Button-1>',mouse_click)
app.mainloop()