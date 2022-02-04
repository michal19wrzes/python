from .afterGenerate import afterGenerate
def acceptAnswer(self, mydb):
    listOfPlayers = self.getListOfPlayers(mydb)
   #update task by the entered params where id = idTaskEntry, result inserted to big output entry
    query="UPDATE users SET user_points=user_points+1 WHERE user_name ='{}'".format(listOfPlayers[self.x])
    cursor = mydb.cursor()
    cursor.execute(query)
    mydb.commit()       
    cursor.close()
    afterGenerate(self,mydb)