import mysql.connector

class student:
    myDb = mysql.connector.connect(host="localhost",
                                        user="root",
                                        password="student")
    myCursor = myDb.cursor(buffered=True)
    myCursor.execute("USE ifaTabTrack")

    def __init__(self, rollNo, age, weight, height, gender, name) :
        self.name = name
        self.rollNo = rollNo
        self.age = age
        self.weight = weight
        self.height = height
        self.gender = gender


    def DescTable(self,col):
        self.myCursor.execute(f"DESc {col}")
        myRes = self.myCursor.column_names
        for x in myRes:
            print(x, '   | ', end=" ")
        print()

        row = self.myCursor.fetchall()
        for i in row:
            for j in i:
                print(j, '   | ', end="")

    def InsertingIntoTablenewStud(self,rn, name, age, gender, height, weight):
        sql = "INSERT INTO newStud (RollNo,Name,Age,Gender,Height,Weight) VALUES (%s,%s,%s,%s,%s,%s)"
        val = [rn, name, age, gender, height, weight]
        self.myCursor.execute(sql, val)
        self.myDb.commit()
        print("Entered into database")



    def displayingData(self,table):
        sql = ""
        if (table == "newStud"):
            sql = "SELECT * FROM newStud"
        else:
            sql = "SELECT * FROM tabTaken"
        self.myCursor.execute(sql)
        res = self.myCursor.fetchall()
        for i in res:
            print(i)

    def countTabTaken(self,rn): # can be used during project expansion
        sql = "SELECT COUNT(*) FROM tabTaken INNER JOIN newStud ON tabTaken.RollNo = newStud.RollNo WHERE newStud.RollNo = %s"
        val = [rn]
        self.myCursor.execute(sql, val)
        res = self.myCursor.fetchall()
        for i in res:
            print(i)



class tab:
    myDb = mysql.connector.connect(host="localhost",
                                   user="root",
                                   password="student")
    myCursor = myDb.cursor(buffered=True)
    myCursor.execute("USE ifaTabTrack")

    def __init__(self, rn, date):
        self.rn = rn
        self.date = date

    def InsertingIntoTabletabTaken(self,rn, date):
        sql = "INSERT INTO tabTaken(RollNo,dateTaken) VALUES (%s, %s)"
        val = [rn, date]
        self.myCursor.execute(sql, val)
        self.myDb.commit()