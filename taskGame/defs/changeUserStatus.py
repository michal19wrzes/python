from tkinter import END
def changeUserStatus(self,mydb,idUserEntry):
    #change status (0|1) of task
    query="SELECT user_status FROM users where user_id ={}".format(int(self.idUserEntry.get("1.0",END)))
    cursor = mydb.cursor()
    cursor.execute(query)
    for task_status in cursor:
        print(task_status)
        if task_status[0] == 1:
            query="UPDATE users SET user_status=0 WHERE user_id={}".format(idUserEntry.get("1.0",END))
        elif task_status[0] == 0:
            query="UPDATE users SET user_status=1 WHERE user_id={}".format(idUserEntry.get("1.0",END))
        cursor.execute(query)
        mydb.commit()       
    cursor.close() 