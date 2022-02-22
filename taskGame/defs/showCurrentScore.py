
def showCurrentScore(self,mydb,wynikiArea):
#action after click 'show task' button
    query="SELECT user_name, user_points FROM users WHERE user_status=1 ORDER BY user_points DESC"
    f = ""
    cursor = mydb.cursor()
    cursor.execute(query)
    for (user_name,user_points) in cursor:
        f = f + "{} : {} \n".format(user_name,user_points);  
    cursor.close()  
    wynikiArea.insert('1.0',f) #na początek