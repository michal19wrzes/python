def showTOffButon(mydb,txtArea):
    #show disabled tasks, result inserted to output entry
    query="SELECT task_id,task_title,task_status,task_priority FROM tasks where task_status = 0"
    f = ""
    cursor = mydb.cursor()
    cursor.execute(query)
    for (task_id,task_title,task_status,task_priority) in cursor:
        f = f + "{}  {}  Status:{}  Priorytet:{}\n".format(task_id,task_title,task_status,task_priority)
    cursor.close()  
    txtArea.insert('2.0',f) #na początek