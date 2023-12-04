import sys
from datetime import datetime, timedelta #Created by Jon Arbell De Ocampo
import pytz
class timeRecord:

    def __init__(self, id, firstName, lastName, tin, sss ,philHealth,department, position,rPh):
        self.setID(id)
        self.setFirstName(firstName)
        self.setLastName(lastName)
        self.setTinId(tin)
        self.setSSSiD(sss)
        self.setPhilHealthId(philHealth)
        self.setDepartment(department)
        self.setPosition(position)
        self.setRatePerHour(rPh)
        self.__absences = []
        self.__workHour = []
        self.__datePeriod = {}
        self.__done = False
        print("Registered Successfully!\n")

    def setDone(self,done):
        self.__done = done

    def isDone(self):
        return self.__done
    def setRatePerHour(self,rPh):
        self.__rPh = rPh
    def setAbsences(self, absences):

        if self.isDone():
            self.__absences = []

        self.__absences.append(absences)

    def setFirstName(self, firstName):
        self.__firstName = firstName

    def setPhilHealthId(self,philHealth):
        self.__philHealth = philHealth

    def setTinId(self,tin):
        self.__tin = tin

    def setSSSiD(self,sss):
        self.__sss = sss
    def setLastName(self, lastName):
        self.__lastName = lastName

    def setDepartment(self, department):
        self.__department = department

    def setPosition(self, position):
        self.__position = position

    def setID(self, id):
        self.__id = id

    def setWorkHour(self, workHour):

        if self.isDone():
            self.__workHour = []

        self.__workHour.append(workHour)

    def viewEmployee(self):

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
        print(self.getRegularPay())
        print(f"\n>> Employee Details\nFull Name: {self.getFirstName()} {self.getLastName()}\nTin ID: {self.getTinID()}\nSSS ID: {self.getSssId()}\nPhilhealth ID: {self.getPhilHealthId()}\nDepartment: {department}\nPosition: {position}\nRate per Hour: {self.getRatePerHour()}\n")
        self.viewPayrollAndTimeKeeping()

    def getRegularPay(self):
        return float(self.getWorkHourRegular()*self.getRatePerHour())
    def getOTPay(self):
        return float(self.getWorkHourOT()*self.getRatePerHour())
    def getGrossPay(self):
        return float(self.getTotalWorkHour()*self.getRatePerHour())

    def getSSSDeduction(self):
        return float(self.getRegularPay() * 0.02)

    def getTaxDeduction(self):
        return float(self.getRegularPay() * 0.15)

    def getPhilhealthDeduction(self):
        return float(self.getRegularPay() * 0.05)
    def getRatePerHour(self):
        return int(self.__rPh)

    def getTinID(self):
        return self.__tin
    def viewPayrollAndTimeKeeping(self):
        for datePeriod, values in self.__datePeriod.items():
            totalDeduction = float((float(values[2]*0.05)*100)+(float(values[2]*0.02)*100)+float(values[2]*0.15)*100)
            print(f">> Timekeeping Entries\nDate Period: {datePeriod}\nTotal # of Hours Worked: {values[0]}\nTotal # of Absences: {values[1]}\n>> Payroll Entries\n  Total # of Regular Hours Worked: {values[2]}\n  Total # of Overtime Hours Worked: {values[3]}\n  Total Regular Pay: P{values[4]}\n  Total Overtime Pay: P{values[5]}\n Total Gross Pay: P{values[6]}")
            print(f" Deductions:\n  Tax (15%): P{float(values[2]*0.15)*100}\n  SSS (2%): P{float(values[2]*0.02)*100}\n  PhilHealth (5%): P{float(values[2]*0.05)*100}\n Total Deductions: P{totalDeduction}\n Total Net Pay: P{values[6]-totalDeduction}\n")

    def getAbsences(self):
        absent = 0
        for absence in self.__absences:
            absent += absence
        return int(absent)

    def getTotalWorkHour(self):
        workHour = 0
        for work in self.__workHour:
            workHour += work.total_seconds() / 3600
        return int(workHour)

    def getWorkHourRegular(self):

        if self.getPosition() == 1:
            totalWork = (self.getTotalWorkHour() // 8) *8
        else:
            totalWork = (self.getTotalWorkHour() // 4) * 4
        return int(totalWork)

    def getWorkHourOT(self):
        if self.getPosition() ==1:
            ot = self.getTotalWorkHour()%8
        else:
            ot = self.getTotalWorkHour()%4
        return int(ot)

    def getID(self):
        return self.__id

    def getSssId(self):
        return self.__sss

    def getPhilHealthId(self):
        return self.__philHealth

    def getPosition(self):
        return self.__position

    def getDepartment(self):
        return self.__department

    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName

    def setTimeKeepingEntries(self,dateEntry):
        self.__datePeriod[dateEntry] = self.getTotalWorkHour(),self.getAbsences(), self.getWorkHourRegular(), self.getWorkHourOT() ,self.getRegularPay(), self.getOTPay() ,self.getGrossPay(),

local_timezone = pytz.timezone('Asia/Manila')

current_local_time = datetime.now(local_timezone)

formatted_local_time = current_local_time.strftime('%m/%d/%Y %I:%M%p')

listOfEmployee = []

while (True):
    try:

        print(f"========== CC03 DAILY-TIME RECORD SYSTEM ==========\n                                {formatted_local_time}")
        print(f"1. TIMEKEEPING\n2. REGISTER EMPLOYEE\n3. VIEW EMPLOYEE\n4. EXIT\n")
        pick = int(input("Enter your choice here: "))

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
                                                        try:
                                                            dateEntryFormat = datetime.strptime(dateEntry, "%Y-%m-%d")
                                                            if dateEntryFormat >= startDateFormat and dateEntryFormat < endDateFormat:
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
                                                        except Exception as e:
                                                            print(e)
                                                            print("Invalid Input. Try Again.".upper())

                                                    startDateFormat += timedelta(days=1)
                                                    if dateEntryFormatSameAsEndDate:
                                                        break
                                                startToEndDate = f"{startDate} to {endDate}"
                                                empID.setTimeKeepingEntries(startToEndDate)
                                                empID.setDone(True)
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
            while (True):
                convertIdReg = ''
                while True:
                    try:
                        id = input("Enter your Employee ID: ")
                        if id.upper() == 'E':
                            convertId = 'E'
                            break
                        elif int(id) == 0:
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
                        elif len(lName) > 1 and len(lName) < 20:
                            lastName = lName
                            break
                        else:
                            print("I think there's no last name with 1 length or less. Try again.")
                    else:
                        print("Invalid Last Name. Try Again")
                if lastName == 'E':
                    break

                tinId = ""
                while True:
                    try:
                        tin = input("Enter 12-digit TIN ID#: ")
                        if tin == 'E':
                            tinId = 'E'
                            break
                        elif len(tin)==12:
                            tinId = int(tin)
                            break
                        else:
                            print("INVALID INPUT. MUST BE 12 DIGITS. TRY AGAIN.\n")
                    except Exception as e:
                        print("Please enter valid information.\n")
                if tinId == 'E':
                    break

                SSSiD = ""
                while True:
                    try:
                        sss = input("Enter 10-digit SSS ID#: ")
                        if sss == 'E':
                            SSSiD = 'E'
                            break
                        elif len(sss) == 10:
                            SSSiD = int(sss)
                            break
                        else:
                            print("INVALID INPUT. MUST BE 10 DIGITS. TRY AGAIN.\n")
                    except Exception as e:
                        print("Please enter valid information.\n")
                if SSSiD == 'E':
                    break

                philHealthId = ""
                while True:
                    try:
                        philHealth = input("Enter 12-digit TIN ID#: ")
                        if philHealth == 'E':
                            philHealthId = 'E'
                            break
                        elif len(philHealth) == 12:
                            philHealthId = int(philHealth)
                            break
                        else:
                            print("INVALID INPUT. MUST BE 12 DIGITS. TRY AGAIN.\n")
                    except Exception as e:
                        print("Please enter valid information.\n")
                if philHealthId == 'E':
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
                            print(
                                "Invalid input. Please enter either '1' for Faculty, '2' for Non-Faculty, or 'E' to exit.\n")
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
                            print(
                                "Invalid input. Please enter either '1' for Full-Time, '2' for Part-Time, or 'E' to exit.\n")
                    except Exception as e:
                        print("Please enter valid information.\n")
                if convertPosition == 'E':
                    break

                ratePerHour = ""
                while True:
                    try:
                        rPhour = input("Enter rate per hour: ")
                        if rPhour == 'E':
                            ratePerHour = 'E'
                            break
                        elif int(rPhour) > 10:
                            ratePerHour = int(rPhour)
                            break
                        else:
                            print("INVALID INPUT. TRY AGAIN.\n")
                    except Exception as e:
                        print("Please enter valid information.\n")
                if ratePerHour == 'E':
                    break

                listOfEmployee.append(timeRecord(convertIdReg, firstName, lastName, tinId,SSSiD,philHealthId, convertDepartment, convertPosition,ratePerHour))
                break

        elif pick == 3:
            print(
                f"========== VIEW EMPLOYEE ==========\n                                {formatted_local_time}\n(Enter 'E' if Exit)")
            while (True):
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
                            again = input("Do you want to view another ID? (Y/N): ").upper()
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
                        #print("ID should not have any characters.\n")
                        print(f"{e}")
                if done:
                    break

        elif pick == 4:
            print("GOODBYE!")
            break

        else:
            print("Invalid Input.\n")

    except:
        print("Please numeric input only.\n")
