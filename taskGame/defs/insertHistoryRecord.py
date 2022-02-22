import tkinter as tk
def insertHistoryRecord(self,mydb,counter,cattegory,letter,player,zal,tim):
#action after click 'add task' button
    query="INSERT INTO gameHistory(category,letter,round_id,user,zal) VALUES ('{}','{}',{},'{}',{})".format(cattegory,letter,counter,player,zal)
    cursor = mydb.cursor()
    cursor.execute(query)
    mydb.commit()
    cursor.close()