import mysql.connector
try:
    mydb = mysql.connector.connect(host="localhost",user="mysql_user",passwd="password",database="testowadb")
    cursor = mydb.cursor()
    querry = "SELECT * FROM cities"
    cursor.execute(querry)
    for citi in cursor:
        print(citi)
except mysql.connector.Error as err:
    print("Connection failed",err.errno,'\n',err)
except:
    print("Other fail")
mydb.close()