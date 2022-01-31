
def getListOfPlayers(self,mydb):
#action after click 'show task' button
    query="SELECT user_name FROM users WHERE user_status = 1"
    f = []
    cursor = mydb.cursor()
    cursor.execute(query)
    for (user_name) in cursor:
        f.append(user_name[0]) 
    cursor.close()
    return f