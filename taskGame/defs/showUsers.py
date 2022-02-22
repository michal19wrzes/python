
def showUsers(self,mydb,txtArea):
#action after click 'show task' button
    query="SELECT user_id,user_name,user_status FROM users"
    f = ""
    cursor = mydb.cursor()
    cursor.execute(query)
    for (task_id,task_title,task_status) in cursor:
        f = f + "{}  {}  Status:{} \n".format(task_id,task_title,task_status);  
    cursor.close()  
    txtArea.insert('2.0',f) #na początek