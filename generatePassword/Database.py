import sqlite3 as sql

def openDB():
    global con
    con = sql.connect('generatedPassword.db')

    global c
    c = con.cursor()

def createTable():
    openDB()
    c.execute(
        '''
        create table password(
            name Text,
            application Text,
            password Text
        )
        '''
    )
    con.commit()
    closeDB()

def insertData(name,app,password):
    try:
        openDB()
        c.execute(
            '''
                insert into password
                values(?,?,?)
            ''',(name,app,password)
        )
        con.commit()
        print("Saved Password!")
    except Exception as e:
        print(e)
    finally:
        closeDB()

def deleteData(name,password):
    try:
        openDB()
        c.execute(
            '''
                Delete from password
                where accountName = ? and password = ?
            ''',(name,password)
        )
        con.commit()
        print("Deleted Data Successfully")
    except Exception as e:
        print(e)
    finally:
        closeDB()

def showData():
    try:
        openDB()
        c.execute(
            '''
                select * from password
            '''
        )
        data = c.fetchall()
        print(f"\n{'-'*7} All Accounts! {'-'*7}\n")
        for i in data:
            print(f"Account name: {i[0]}\nApplication name: {i[1]}\nPassword: {i[2]}\n")
    except Exception as e:
        print(e)
    finally:
        closeDB()
def closeDB():
    c.close()
    con.close()