def sortTaskPriority(self,mydb,txtArea):
    #return sortPriority DESC querry result
    query="SELECT task_id,task_title,task_status,task_priority FROM tasks WHERE task_status=1 ORDER BY task_priority DESC"
    f = ""
    cursor = mydb.cursor()
    cursor.execute(query)
    for (task_id,task_title,task_status,task_priority) in cursor:
        f = f + "{}  {}  Status:{}  Priorytet:{}\n".format(task_id,task_title,task_status,task_priority)
    cursor.close()
    txtArea.insert('2.0',f)
    
    