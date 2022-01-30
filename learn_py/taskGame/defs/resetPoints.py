def resetPoints(self,mydb):
    #update task by the entered params where id = idTaskEntry, result inserted to big output entry
    query="UPDATE users SET user_points=0"
    cursor = mydb.cursor()
    cursor.execute(query)
    mydb.commit()       
    cursor.close()  