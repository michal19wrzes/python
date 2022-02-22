
def showGameHistory(self,mydb,txtArea):
#action after click 'show task' button
    query="SELECT round_id,category,letter,user,zal FROM gameHistory"
    f = ""
    cursor = mydb.cursor()
    cursor.execute(query)
    for (round_id,category,letter,user,zal) in cursor:
        f = f + f"{round_id:3} {category:25} {'na literę':13} {letter:3} {user:8} {zal:4}"+'\n'  
    cursor.close()  
    txtArea.insert('2.0',f) #na początek