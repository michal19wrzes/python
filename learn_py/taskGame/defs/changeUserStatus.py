def changeUserStatus(self,mydb,idTaskEntry):
    #change status (0|1) of task
    query="SELECT user_status FROM users where user_id ={}".format(idTaskEntry.get())
    cursor = mydb.cursor()
    cursor.execute(query)
    for task_status in cursor:
        if task_status[0] == 1:
            query="UPDATE users SET user_status=0 WHERE user_id={}".format(idTaskEntry.get())
        elif task_status[0] == 0:
            query="UPDATE users SET user_status=1 WHERE user_id={}".format(idTaskEntry.get())
        cursor.execute(query)
        mydb.commit()       
    cursor.close() 