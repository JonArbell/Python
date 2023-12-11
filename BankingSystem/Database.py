import sqlite3 as sql
import bcrypt
from datetime import datetime as dt

def hashPassword(password):
    hashedPass = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashedPass

def openDB():
    global con
    con = sql.connect('bankAccounts.db')
    global c
    c = con.cursor()

def createTableAccounts():
    openDB()
    c.execute(
        '''
        create table accounts(
            firstName TEXT,
            lastName TEXT,
            mobileNumber INTEGER,
            occupation TEXT,
            balance INTEGER,
            cardNumber INTEGER,
            pin INTEGER,
            accountDateTimeCreated datetime
        )
        '''
    )
    con.commit()
    print("Create table Done!")
    closeDB()

def createTableTransactionHistory():
    openDB()
    c.execute(
        '''
        create table transactionHistory(
            cardNumber INTEGER,
            pin INTEGER,
            senderFullName,
            receiverFullName,
            amount INTEGER
            dateNTime datetime
        )
        '''
    )
    con.commit()
    print("Create table Done!")
    closeDB()

def insertNewAccount(fName,lName,number,occu,bal,card,pin):
    openDB()
    dateNow = dt.now()
    c.execute(
        '''
            insert into accounts(firstName,lastName,mobileNumber,occupation,balance,cardNumber,pin,accountDateTimeCreated) 
            values(?,?,?,?,?,?,?,?)
        ''',(fName,lName,number,occu,bal,card,hashPassword(pin),dateNow)
    )
    con.commit()
    print("Account creation completed.")
    closeDB()
    return True


def updateFirstName(fName,card):
    openDB()

    c.execute(
        '''
            select firstName from accounts
            where cardNumber = ?
        ''',(card,)
    )
    data = c.fetchone()
    if data[0] != fName:
        c.execute(
            '''
                update accounts
                set firstName = ?
                where cardNumber = ?
            ''',(fName,card)
        )
        con.commit()
        print("Your first name has been successfully updated.")
        closeDB()
    else:
        print("You can't use your old first name for your new first name.\n")
        closeDB()

def updateOccupation(occu,card):
    openDB()

    c.execute(
        '''
            select occupation from accounts
            where cardNumber = ?
        ''', (card,)
    )
    data = c.fetchone()
    if data[0] != occu:
        c.execute(
            '''
                update accounts
                set occupation = ?
                where cardNumber = ?
            ''',(occu,card)
        )
        con.commit()
        print("Your occupation has been successfully updated.")
        closeDB()
    else:
        print("You can't use your old occupation for your new occupation.\n")
        closeDB()

def updateLastName(lName,card):
    openDB()
    c.execute(
        '''
            select lastName from accounts
            where cardNumber = ?
        ''', (card,)
    )
    data = c.fetchone()
    if data[0] !=lName:
        c.execute(
            '''
                update accounts
                set lastName = ?
                where cardNumber = ?
            ''',(lName,card)
        )
        con.commit()
        print("Your last name has been successfully updated.")
        closeDB()
    else:
        print("You can't use your old last name for your new last name.\n")
        closeDB()


def updateMobileNumber(number,card):
    openDB()
    c.execute(
        '''
            select mobileNumber from accounts
            where cardNumber = ?
        ''', (card,)
    )
    data = c.fetchone()
    if data[0] != number:
        c.execute(
            '''
                update accounts
                set mobileNumber = ?
                where cardNumber = ? and pin = ?
            ''',(number,card)
        )
        con.commit()
        print("Your mobile number has been successfully updated.")
        closeDB()
    else:
        print("You can't use your old mobile number for your new mobile number.\n")
        closeDB()

def updatePin(card,newPin):
    openDB()
    c.execute(
        '''
            select pin from accounts
            where cardNumber = ?
        ''',(card,)
    )
    data = c.fetchone()
    if bcrypt.checkpw(newPin.encode('utf-8'), data[0]):
        print("You can't use your old pin for your new pin.")
        closeDB()
    else:
        c.execute(
            '''
                update accounts
                set pin = ?
                where cardNumber = ?
            ''', (hashPassword(newPin), card)
        )
        con.commit()
        print("Your pin has been successfully updated.")
        closeDB()

def logIn(card,pin,service):
    try:
        openDB()
        c.execute(
            '''
                select * from accounts
                where cardNumber = ?
            ''',(card,)
        )
        data = c.fetchone()
        storedHashedPassword = data[6]
        if service == 1:
            if data:
                if bcrypt.checkpw(pin.encode('utf-8'), storedHashedPassword):
                    print(f"\n{data[0]} {data[1]} is logged in successfully\n")
                    return True
                else:
                    print("Wrong Pin. Try Again\n")
                    return False
            else:
                print("This card number is not registered yet.\n")
                return False
        else:
            if data:
                if bcrypt.checkpw(pin.encode('utf-8'), storedHashedPassword):
                    return True
                else:
                    print("Wrong Pin. Try Again\n")
                    return False
            else:
                print("This card number is not registered yet.\n")
                return False
    except Exception as e:
        print(e)
    finally:
        closeDB()

def logOut(card,pin):
    openDB()
    c.execute(
        '''
            select * from accounts
            where cardNumber = ?
        ''',(card,)
    )
    data = c.fetchone()
    if bcrypt.checkpw(pin.encode('utf-8'), data[6]):
        print(f"\n{data[0]} {data[1]} has successfully logged out.\n")
        closeDB()

def showInfo(card,pin):
    openDB()
    c.execute(
        '''
            select * from accounts
            where cardNumber = ?
        ''',(card,)
    )
    data = c.fetchone()
    if bcrypt.checkpw(pin.encode('utf-8'), data[6]):
        print(f"\n{'-' * 7} 'Information' {'-' * 7}\n\nFull name: {data[0]} {data[1]}\nMobile number: {data[2]}\nOccupation: {data[3]}\nDate Created: {str(data[7])[0:19]}\n")
        closeDB()

def showHistory(card):
    openDB()
    c.execute(
        '''
            select * from transactionHistory
            where senderCardNumber = ? or receiverCardNumber = ?
            ORDER by dateNtime
        ''', (card,card)
    )
    dataTransact = c.fetchall()

    print(f"{'-' * 7} 'Transaction History' {'-' * 7}\n")
    for i in dataTransact:
        date = i[5]
        if i[6] == 'deposit':
            print(f">> Deposit\nAmount: {i[1]}\nDate and Time: {str(date)[0:18]}\n")
        if i[6] == 'cashTransfer':
            if card == i[0]:
                print(f">> Cash Transfer\nCash send to: {i[4]}\nAmount: {i[1]}\nDate and Time: {str(date)[0:19]}\n")
            else:
                print(f">> Cash Transfer\nCash received from: {i[3]}\nAmount: {i[1]}\nDate and Time: {str(date)[0:19]}\n")
        if i[6] == 'withdraw':
            print(f">> Withdraw\nAmount: {i[1]}\nDate and Time: {str(date)[0:18]}\n")
    closeDB()

def setHistory(senderCardNumber,amount,service,senderFullName = '',receiverFullname='',receiverCardNumber=''):
    openDB()
    now = dt.now()
    if service == 'deposit':
        c.execute(
            '''
                insert into transactionHistory(senderCardNumber,amount,dateNtime,service)
                values(?,?,?,?)
            ''',(senderCardNumber,amount,now,'deposit')
        )

    elif service == 'withdraw':
        c.execute(
            '''
                insert into transactionHistory(senderCardNumber,amount,dateNtime,service)
                values(?,?,?,?)
            ''', (senderCardNumber, amount,now,'withdraw')
        )

    elif service == 'cashTransfer':
        c.execute(
            '''
                insert into transactionHistory(senderCardNumber,amount,receiverCardNumber,senderFullName,receiverFullname,dateNtime,service)
                values(?,?,?,?,?,?,?)
            ''', (senderCardNumber,amount,receiverCardNumber, senderFullName,receiverFullname,now,'cashTransfer')
        )
    con.commit()
    closeDB()

def cashTransfer(senderCard,pin,amount,receiverCard):
    if senderCard != receiverCard:
        openDB()
        c.execute(
            '''
                select pin,firstName,lastName,balance from accounts 
                where cardNumber = ?
            ''', (senderCard,)
        )  # Sender
        dataSender = c.fetchone()

        if bcrypt.checkpw(pin.encode('utf-8'), dataSender[0]):
            if dataSender[3] > 0:
                if dataSender[3] >=amount:
                    c.execute(
                        '''
                            select cardNumber,firstName,lastName,balance from accounts 
                            where cardNumber = ?
                        ''',(receiverCard,)
                    ) # Receiver
                    dataReceiver = c.fetchone()
                    if dataReceiver[0] == receiverCard:
                        totalReceived = amount + dataReceiver[3]
                        c.execute(
                            '''
                                update accounts
                                set balance = ?
                                where cardNumber = ?
                            ''', (totalReceived, receiverCard)
                        )

                        totalSend = dataSender[3]-amount
                        c.execute(
                            '''
                                update accounts
                                set balance = ?
                                where cardNumber = ?
                            ''', (totalSend, senderCard)
                        )

                        con.commit()
                        senderName = dataSender[1]+" "+dataSender[2]
                        receiverName = f"{dataReceiver[1]} {dataReceiver[2]}"
                        print(f"Successfully send P{amount} to {receiverName}.")
                        setHistory(senderCard,amount,'cashTransfer',senderName,receiverName,receiverCard)
                        return True
                    else:
                        print("This card number is not registered yet.\n")
                        closeDB()
                        return False
                else:
                    print("Insufficient Balance\n")
                    closeDB()
                    return False
            else:
                print("You have zero balance")
                closeDB()
                return False
        else:
            print("Wrong pin.\n")
            closeDB()
            return False
    else:
        print("Cannot send to your bank account.\n")
        return False


def updateBalance(bal,card):
    openDB()
    c.execute(
        '''
            update accounts
            set balance = ?
            where cardNumber = ?
        ''',(bal,card)
    )
    con.commit()
    closeDB()

def showBalance(card):
    openDB()
    c.execute(
        '''
            select balance from accounts
            where cardNumber = ?
        ''',(card,)
    )
    data = c.fetchone()
    print(f"{'-'*7} 'Balance' {'-'*7}\nBalance: {data[0]}\n")
    closeDB()

def deposit(card,pin,amount):
    openDB()
    c.execute(
        '''
            select balance,pin from accounts
            where cardNumber = ?
        ''', (card,)
    )
    data = c.fetchone()
    if bcrypt.checkpw(pin.encode('utf-8'), data[1]):
        updatedBal = data[0]+amount
        updateBalance(updatedBal,card)
        print("Deposit successful. Your funds have been added to your account.")
        setHistory(card,amount,'deposit')
        return True
    else:
        print("Wrong pin.")
        closeDB()
        return False


def withdraw(card,pin,amount):
    openDB()
    c.execute(
        '''
            select balance , pin from accounts
            where cardNumber = ?
        ''', (card, )
    )
    data = c.fetchone()
    if bcrypt.checkpw(pin.encode('utf-8'), data[1]):
        if data[0] > 0:
            if data[0] >= amount:
                updatedBal = data[0]-amount
                updateBalance(updatedBal,card)
                print("Withdraw successfully\n")
                setHistory(card,amount,'withdraw')
                return True
            else:
                print("Insufficient balance\n")
                closeDB()
                return False
        else:
            print("You have zero balance\n")
            closeDB()
            return False
    else:
        print("Wrong pin. Try Again.\n")
        closeDB()
        return False


def closeDB():
    c.close()
    con.close()