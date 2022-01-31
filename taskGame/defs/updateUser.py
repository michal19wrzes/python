def updateUser(self,mydb,taskEntry,idTaskEntry):
    #update task by the entered params where id = idTaskEntry, result inserted to big output entry
    query="UPDATE users SET user_name='{}' WHERE user_id={}".format(
    taskEntry.get(),
    idTaskEntry.get())    
    cursor = mydb.cursor()
    cursor.execute(query)
    mydb.commit()       
    cursor.close()  