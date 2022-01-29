def changeTaskStatus(self,mydb,idTaskEntry):
    #change status (0|1) of task
    query="SELECT task_status FROM tasks where task_id ={}".format(idTaskEntry.get())
    cursor = mydb.cursor()
    cursor.execute(query)
    for task_status in cursor:
        if task_status[0] == 1:
            query="UPDATE tasks SET task_status=0 WHERE task_id={}".format(idTaskEntry.get())
        elif task_status[0] == 0:
            query="UPDATE tasks SET task_status=1 WHERE task_id={}".format(idTaskEntry.get())
        cursor.execute(query)
        mydb.commit()       
    cursor.close() 