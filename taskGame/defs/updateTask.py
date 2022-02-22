def updateTask(self,mydb,taskEntry,priorityEntry,statusEntry,idTaskEntry):
    #update task by the entered params where id = idTaskEntry, result inserted to big output entry
    query="UPDATE tasks SET task_title='{}',task_priority={},task_status={} WHERE task_id={}".format(
    taskEntry.get(),
    priorityEntry.get(),
    statusEntry.get(),
    idTaskEntry.get())    
    cursor = mydb.cursor()
    cursor.execute(query)
    mydb.commit()       
    cursor.close()  