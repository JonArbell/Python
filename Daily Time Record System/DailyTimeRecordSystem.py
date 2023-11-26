import sys
from datetime import datetime, timedelta
import pytz

class timeRecord:

    def __init__(self,id,firstName,lastName,department,position):
        self.setID(id)
        self.setFirstName(firstName)
        self.setLastName(lastName)
        self.setDepartment(department)
        self.setPosition(position)
        self.__absences = []
        self.__workHour = []
        self.__datePeriod = {}
        print("Registered Successfully!\n")

    def setAbsences(self, absences):
        self.__absences = []
        self.__absences.append(absences)

    def setFirstName(self,firstName):
        self.__firstName = firstName

    def setLastName(self,lastName):
        self.__lastName = lastName

    def setDepartment(self,department):
        self.__department = department

    def setPosition(self,position):
        self.__position = position

    def setID(self,id):
        self.__id = id

    def setWorkHour(self,workHour):
        self.__workHour = []
        self.__workHour.append(workHour)

    def viewEmployee(self):
        position = ""
        department = ""
        if self.getDepartment() == 1:
            department = "Faculty"
            if self.getPosition() == 1:
                position = "Full-Time"
            else:
                position = "Part-Time"
        else:
            department = "Non-Faculty"
            if self.getPosition() == 1:
                position = "Full-Time"
            else:
                position = "Part-Time"
        print(f">> Employee Details\nFirst Name: {self.getFirstName()}\nLast Name: {self.getLastName()}\nDepartment: {department}\nPosition: {position}\n")
        self.getTimeKeepingEntries()
        
    def getTimeKeepingEntries(self):
        for datePeriod, values in self.__datePeriod.items():
            print(f">> Timekeeping Entries\nDate Period: {datePeriod}\nTotal # of Hours Worked: {values[0]}\nTotal # of Absences: {values[1]}\n")
            
    def getAbsences(self):
        absent = 0
        for absence in self.__absences:
            absent+=absence
        return int(absent)
        
    def getWorkHour(self):
        workHour = 0
        for work in self.__workHour:
            workHour+=work.total_seconds()/3600
        return int(workHour)

    def getID(self):
        return self.__id
        
    def getPosition(self):
        return self.__position
        
    def getDepartment(self):
        return self.__department
        
    def getFirstName(self):
        return self.__firstName
        
    def getLastName(self):
        return self.__lastName

    def setTimeKeepingEntries(self,dateEntry,workHour,absences):
        self.__datePeriod[dateEntry] = workHour,absences

local_timezone = pytz.timezone('Asia/Manila')

current_local_time = datetime.now(local_timezone)

formatted_local_time = current_local_time.strftime('%m/%d/%Y %I:%M%p')

listOfEmployee=[]

while(True):
    try:
        
        print(f"========== CC03 DAILY-TIME RECORD SYSTEM ==========\n                                {formatted_local_time}")
        print(f"1. TIMEKEEPING\n2. REGISTER EMPLOYEE\n3. VIEW EMPLOYEE\n4. EXIT\n")
        pick=int(input("Enter your choice here: "))
        
        if pick == 1:
            while True:
                done = False
                try:
                    print(f"========== TIMEKEEPING SCREEN ==========\n                                {formatted_local_time}\n(Enter 'E' if Exit)")
                    id = input("Enter Employee ID: ")
                    checkID = False
                    if id.upper() == "E":
                        break
                    convertID = int(id)

                    for empID in listOfEmployee:
                        if convertID == empID.getID():
                            checkID = True
                            try:
                                while True:
                                    startDate = input("Enter Start Date (Format: YYYY-MM-DD): ")
                                    if startDate == 'E':
                                        break
                                    startDateFormat = datetime.strptime(startDate, "%Y-%m-%d")
                                    current_datetime = datetime.now()
                                    if startDateFormat <= current_datetime:
                                        while True:
                                            endDate = input("Enter End Date (Format: YYYY-MM-DD): ")
                                            if endDate == 'E':
                                                break
                                            endDateFormat = datetime.strptime(endDate, "%Y-%m-%d")
                                            if endDateFormat <= current_datetime and endDateFormat >= startDateFormat:
                                                while startDateFormat <= endDateFormat:
                                                    dateEntryFormatSameAsEndDate = False
                                                    while True:
                                                        dateEntry = input(">> Date of Entry: ")
                                                        dateEntryFormat = datetime.strptime(dateEntry, "%Y-%m-%d")
                                                        if dateEntryFormat >= startDateFormat and dateEntryFormat< endDateFormat:
                                                            print("(Enter 'A' if absent)")
                                                            timeIn = input("Enter Time-In: ")
                                                            timeOut = input("Enter Time-Out: ")
                                                            if timeIn != "A" and timeOut != "A":
                                                                time_in = datetime.strptime(timeIn, "%H:%M")
                                                                time_out = datetime.strptime(timeOut, "%H:%M")
                                                                time_difference = time_out - time_in
                                                                empID.setWorkHour(time_difference)
                                                                startToEndDate = f"{startDate} to {endDate}"
                                                                done = True
                                                                break
                                                            elif timeIn == 'A' and timeOut == 'A':
                                                                done = True
                                                                empID.setAbsences(1)
                                                                break
                                                            else:
                                                                print("Invalid Input. Try Again.".upper())
                                                        elif dateEntryFormat == endDateFormat:
                                                            print("(Enter 'A' if absent)")
                                                            timeIn = input("Enter Time-In: ")
                                                            timeOut = input("Enter Time-Out: ")

                                                            if timeIn != "A" and timeOut != "A":
                                                                time_in = datetime.strptime(timeIn, "%H:%M")
                                                                time_out = datetime.strptime(timeOut, "%H:%M")
                                                                time_difference = time_out - time_in
                                                                empID.setWorkHour(time_difference)
                                                                startToEndDate = f"{startDate} to {endDate}"
                                                                done = True
                                                                dateEntryFormatSameAsEndDate = True
                                                                break
                                                            elif timeIn == 'A' and timeOut == 'A':
                                                                done = True
                                                                empID.setAbsences(1)
                                                                dateEntryFormatSameAsEndDate = True
                                                                break
                                                            else:
                                                                print("Invalid Input. Try Again.".upper())
                                                        else:
                                                            print("INCORRECT DATE ENTRY. END DATE MUST NOT BE BEFORE START DATE. TRY AGAIN.\n")

                                                    startDateFormat += timedelta(days=1)
                                                    if dateEntryFormatSameAsEndDate:
                                                        break
                                                startToEndDate = f"{startDate} to {endDate}"
                                                empID.setTimeKeepingEntries(startToEndDate, empID.getWorkHour(), empID.getAbsences())
                                                break
                                            elif endDateFormat > current_datetime:
                                                print("INCORRECT DATE ENTRY. END DATE MUST NOT BE AFTER CURRENT DATE. TRY AGAIN.\n")
                                            else:
                                                print("INCORRECT DATE ENTRY. END DATE MUST NOT BE BEFORE START DATE. TRY AGAIN.\n")
                                            if done:
                                                break
                                        break
                                    else:
                                        print("INCORRECT DATE ENTRY. END DATE MUST NOT BE AFTER CURRENT DATE. TRY AGAIN.\n")

                            except Exception as e:
                                print(f"{e}")
                                #print("Invalid date format. Please use YYYY-MM-DD.")
                except:
                    print("ID should not have any characters.\n")
                if not checkID:
                    print("This ID is not yet registered.\n")
                    break
                elif done:
                    break
                    
        elif pick == 2:
            print(f"========== REGISTER EMPLOYEE ==========\n                                {formatted_local_time}\n(Enter 'E' if Exit)\n>> Employee Details")
            while(True):
                    convertIdReg = ''
                    while True:
                        try:
                            id = input("Enter your Employee ID: ")
                            if id.upper() == 'E':
                                convertId = 'E'
                                break
                            if int(id) == 0:
                                print("Enter valid ID.\n")
                                continue
                            convertIdReg = int(id)
                            break
                        except Exception as e:
                            print("ID should not have any characters.\n")
                    if convertIdReg == 'E':
                        break

                    firstName = ""
                    while True:
                        fName = input("Enter your First Name: ")
                        if type(fName) == str:
                            if fName.upper() == 'E':
                                firstName = 'E'
                                break
                            elif len(fName) > 1 and len(fName) < 20:
                                firstName = fName
                                break
                            else:
                                print("I think there's no first name with 1 length or less. Try again.\n")
                        else:
                            print("Invalid First Name. Try Again.\n")
                    if firstName == 'E':
                        break

                    lastName = ""
                    while True:
                        lName = input("Enter your Last Name: ")
                        if type(lName) == str:
                            if lName.upper() == 'E':
                                lastName = 'E'
                                break
                            if len(lName) > 1 and len(lName) < 20:
                                lastName = lName
                                break
                            else:
                                print("I think there's no last name with 1 length or less. Try again.")
                        else:
                            print("Invalid Last Name. Try Again")
                    if lastName == 'E':
                        break

                    convertDepartment = ""
                    while True:
                        try:
                            department = input("Enter your Department (1. Faculty) (2. Non-Faculty): ")
                            if department.upper() == 'E':
                                convertDepartment = 'E'
                                break
                            elif int(department) == 1 or int(department) == 2:
                                convertDepartment = int(department)
                                break
                            else:
                                print("Invalid input. Please enter either '1' for Faculty, '2' for Non-Faculty, or 'E' to exit.\n")
                        except Exception as e:
                            print("Please enter valid information.\n")
                    if convertDepartment == 'E':
                        break

                    convertPosition = ""
                    while True:
                        try:
                            position = input("Enter your Position (1. Full-Time) (2. Part-Time): ")
                            if position.upper() == 'E':
                                convertPosition = 'E'
                                break
                            elif int(position) == 1 or int(position) == 2:
                                convertPosition = int(position)
                                break
                            else:
                                print("Invalid input. Please enter either '1' for Full-Time, '2' for Part-Time, or 'E' to exit.\n")
                        except Exception as e:
                            print("Please enter valid information.\n")
                    if convertPosition == 'E':
                        break
                        
                    listOfEmployee.append(timeRecord(convertIdReg,firstName, lastName, convertDepartment, convertPosition))
                    break

        elif pick == 3:
            print(f"========== VIEW EMPLOYEE ==========\n                                {formatted_local_time}\n(Enter 'E' if Exit)")
            while(True):
                idFound = False
                done = False
                exit = False
                try:
                    id = input("Enter Employee ID: ").upper()
                    if id == "E":
                        exit = True
                    idConvert = int(id)
                    for employee in listOfEmployee:
                        if int(idConvert) == employee.getID():
                            employee.viewEmployee()
                            idFound = True
                            break
                    if not idFound:
                        print("This ID is not yet registered.\n")
                    else:
                        while True:
                            again = input("Do you want to enter another ID? (Y/N): ").upper()
                            if again == 'Y':
                                break
                            elif again == 'N':
                                done = True
                                break
                            else:
                                print("Invalid Input.\n")
                except Exception as e:
                    if exit:
                        break
                    else:
                        print("ID should not have any characters.\n")
                if done:
                    break
                    
        elif pick == 4:
            print("GOODBYE!")
            break
            
        else:
            print("Invalid Input.\n")
            
    except:
        print("Please numeric input only.\n")
