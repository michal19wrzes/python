def resetHistory(self,mydb):
    
    #update task by the entered params where id = idTaskEntry, result inserted to big output entry
    query="DELETE FROM gameHistory"
    cursor = mydb.cursor()
    cursor.execute(query)
    mydb.commit()       
    cursor.close()  