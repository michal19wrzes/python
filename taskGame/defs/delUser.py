def delUser(self,mydb,idTaskEntry):
    #action after click 'delete button', delete task by id 
    query="DELETE FROM users WHERE user_id={}".format(idTaskEntry.get())
    cursor = mydb.cursor()
    cursor.execute(query)
    mydb.commit()
    cursor.close()