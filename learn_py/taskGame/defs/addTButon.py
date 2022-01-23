def addTButon(mydb,taskEntry,statusEntry,priorityEntry):
#action after click 'add task' button
    query="INSERT INTO tasks(task_title,task_status,task_priority) VALUES ('{}',{},{})".format(taskEntry.get(),statusEntry.get(),priorityEntry.get())
    cursor = mydb.cursor()
    cursor.execute(query)
    mydb.commit()
    cursor.close()