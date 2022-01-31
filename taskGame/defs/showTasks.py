
def showTasks(self,mydb,txtArea):
#action after click 'show task' button
    query="SELECT task_id,task_title,task_status,task_priority FROM tasks"
    f = ""
    cursor = mydb.cursor()
    cursor.execute(query)
    for (task_id,task_title,task_status,task_priority) in cursor:
        f = f + "{}  {}  Status:{}  Priorytet:{}\n".format(task_id,task_title,task_status,task_priority);  
    cursor.close()  
    txtArea.insert('2.0',f) #na początek