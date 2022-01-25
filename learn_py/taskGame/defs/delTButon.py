def delTButon(self,mydb,idTaskEntry):
    #action after click 'delete button', delete task by id 
    query="DELETE FROM tasks WHERE task_id={}".format(idTaskEntry.get())
    cursor = mydb.cursor()
    cursor.execute(query)
    mydb.commit()
    cursor.close()