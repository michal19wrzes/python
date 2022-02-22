import tkinter as tk
def addUser(self,mydb,taskEntry):
#action after click 'add task' button
    query="INSERT INTO users(user_name) VALUES ('{}')".format(taskEntry.get("1.0",tk.END).replace('\n',''))
    cursor = mydb.cursor()
    cursor.execute(query)
    mydb.commit()
    cursor.close()