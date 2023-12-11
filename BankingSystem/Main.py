import Database as db

# db.openDB()
# db.createTableAccounts()
# db.createTableTransactionHistory()
global globalPin

while True:
    print(f"{'-'*10} 'Welcome to Jon's Bank!' {'-'*10}\n")
    print(f"1.\tCreate Account\n2.\tLogin Account\n3.\tExit\n")
    inp = input("Enter input: ")
    if inp == '1':
        while True:
            print(f">>\tAccount creation\n\nEnter 'c' if you want to cancel\n")
            firstName = ''
            while True:
                fName = input("Enter your first name: ")
                if fName.lower() == 'c':
                    firstName = fName.lower()
                    break
                if any(not char.isdigit() for char in fName):
                    if len(fName) > 0:
                        firstName = fName
                        break
                    else:
                        print("Oops! It seems you left the first name field blank. Please enter your first name.")
                else:
                    print("First name should not contains numbers\n")
            if firstName == 'c':
                print("Cancelled!")
                break

            lastName = ''
            while True:
                lName = input("Enter your last name: ")
                if fName.lower() == 'c':
                    lastName = lName.lower()
                    break
                if any(not char.isdigit() for char in lName):

                    if len(fName) > 0:
                        lastName = lName
                        break
                    else:
                        print("Oops! It seems you left the last name field blank. Please enter your last name.")
                else:
                    print("Last name should not contains numbers\n")
            if lastName == 'c':
                print("Cancelled!")
                break

            mobileNumber = ''
            while True:
                try:
                    mobNum = input("Enter your mobile number: ")
                    if mobNum.lower() == 'c':
                        mobileNumber = mobNum.lower()
                        break
                    x = int(mobNum)
                    if len(str(mobNum)) == 11:
                        mobileNumber = mobNum
                        break
                    else:
                        print("Mobile number should be 11 digits")
                except Exception as e:
                    #print(e)
                    print("Mobile number should not have any characters")
            if mobileNumber == 'c':
                print("Cancelled!")
                break


            occupation = ''
            while True:
                occu = input("Enter your occupation: ")
                if occu.lower() == 'c':
                    occupation = occu.lower()
                    break
                if any(not char.isdigit() for char in occu):
                    if occu == 'e':
                        occupation = occu
                        break
                    if len(occu) > 0:
                        occupation = occu
                        break
                    else:
                        print("Oops! It seems you left the occupation field blank. Please enter your occupation.")
                else:
                    print("Enter valid occupation.\n")
            if occupation == 'c':
                print("Cancelled!")
                break

            cardNumber = ''
            while True:
                try:
                    cardNum = input("Enter your card number: ")
                    if cardNum.lower() == 'c':
                        cardNumber = cardNum.lower()
                        break
                    x = int(cardNum)
                    if len(cardNum) == 16:
                        cardNumber = cardNum
                        break
                    else:
                        print("Card number should be 16 digits")
                except Exception as e:
                    # print(e)
                    print("Card number should not have any characters")
            if cardNumber == 'c':
                print("Cancelled!")
                break

            pinNum = ''
            while True:
                try:
                    pin = input("Enter your pin number: ")
                    if pin.lower() == 'c':
                        pinNum = pin.lower()
                        break
                    x = int(pin)
                    if len(pin) == 4:
                        pinNum = pin
                        break
                    else:
                        print("Pin number should be 4 digits")
                except Exception as e:
                    # print(e)
                    print("Pin number should not have any characters")

            if pinNum == 'c':
                print("Cancelled!")
                break
            if db.insertNewAccount(firstName,lastName,mobileNumber,occupation,0,cardNumber,pinNum):
                break

    elif inp== '2':
        print(f">>\tLogin\n\nEnter 'c' if you want to cancel\n")
        cardNumber2 = ''
        while True:
            try:
                cardNum = input("Enter your card number: ")
                if cardNum.lower() == 'c':
                    cardNumber2 = cardNum.lower()
                    break
                x = int(cardNum)
                if len(cardNum) == 16:
                    cardNumber2 = cardNum
                    break
                else:
                    print("Card number should be 16 digits")
            except Exception as e:
                #print(e)
                print("Card number should not have any characters")
        if cardNumber2 == 'c':
            break

        pinNum2 = ''
        while True:
            try:
                pin = input("Enter your pin number: ")
                if pin.lower() == 'e':
                    pinNum2 = pin.lower()
                    break
                x = int(pin)
                if len(pin) == 4:
                    pinNum2 = pin
                    break
                else:
                    print("Pin number should be 4 digits")
            except Exception as e:
                # print(e)
                print("Pin number should not have any characters")
        if pinNum2 == 'c':
            break
        if db.logIn(cardNumber2,pinNum2,1):
            globalPin = pinNum2
            while True:
                print(f">>\tServices\n")
                print(f"a. Check balance\nb. Deposit\nc. Withdraw\nd. Cash Transfer\ne. Transactions\nf. Change Information\ng. Show Information\nh. Logout\n")
                inp2 = input("Enter service: ").lower()

                if inp2.lower() == 'a':
                    db.showBalance(cardNumber2)
                elif inp2.lower() == 'b':
                    print(f">> Deposit\nEnter 'c' if you want to cancel\n")
                    while True:

                        amount = ''
                        while True:
                            try:
                                amnt = input("Enter amount: ")
                                if amnt.lower() == 'c':
                                    amount = amnt.lower()
                                    break
                                if int(amnt) > 0:
                                    amount = int(amnt)
                                    break
                                else:
                                    print("Please enter any amount\n")
                            except:
                                print("Amount should not have any characters.\n")
                        if amount == 'c':
                            print("Cancelled!")
                            break

                        pinNum2b = ''
                        while True:
                            try:
                                pin = input("Enter your pin number again: ")
                                if pin.lower() == 'c':
                                    pinNum2b = pin.lower()
                                    break
                                x = int(pin)
                                if len(pin) == 4:
                                    pinNum2b = pin
                                    break
                                else:
                                    print("Pin number should be 4 digits")
                            except Exception as e:
                                # print(e)
                                print("Pin number should not have any characters")
                        if pinNum2b == 'c':
                            print("Cancelled!")
                            break

                        if db.deposit(cardNumber2,pinNum2b,amount):
                            break

                elif inp2 == 'c':
                    while True:
                        print(">> Withdraw <<\n\nEnter 'c' if you want to cancel\n")

                        amount = ''
                        while True:
                            try:
                                amnt = input("Enter amount: ")
                                if amnt.lower() == 'c':
                                    amount = amnt.lower()
                                    break
                                if int(amnt) > 0:
                                    amount = int(amnt)
                                    break
                                else:
                                    print("Please enter any amount\n")
                            except:
                                print("Amount should not have any characters.\n")
                        if amount == 'c':
                            print("Cancelled!")
                            break

                        pinNum2c = ''
                        while True:
                            try:
                                pin = input("Enter your pin number again: ")
                                if pin.lower() == 'c':
                                    pinNum2c = pin.lower()
                                    break
                                x = int(pin)
                                if len(pin) == 4:
                                    pinNum2c = pin
                                    break
                                else:
                                    print("Pin number should be 4 digits")
                            except Exception as e:
                                # print(e)
                                print("Pin number should not have any characters")
                        if pinNum2c == 'c':
                            print("Cancelled!")
                            break

                        if db.withdraw(cardNumber2,pinNum2c,amount):
                            break
                elif inp2 == 'd':
                    while True:
                        print(">> Cash Transfer <<\n\nEnter 'c' if you want to cancel\n")

                        amount = ''
                        while True:
                            try:
                                amnt = input("Enter amount: ")
                                if amnt.lower() == 'c':
                                    amount = amnt.lower()
                                    break
                                if int(amnt) > 0:
                                    amount = int(amnt)
                                    break
                                else:
                                    print("Please enter any amount\n")
                            except:
                                print("Amount should not have any characters.\n")
                        if amount == 'c':
                            print("Cancelled!")
                            break

                        receiver = ''
                        while True:
                            try:
                                cardNum = input("Enter receiver card number: ")
                                if cardNum.lower() == 'c':
                                    receiver = cardNum
                                    break
                                x = int(cardNum)
                                if len(cardNum) == 16:
                                    receiver = cardNum
                                    break
                                else:
                                    print("Card number should be 16 digits")
                            except Exception as e:
                                # print(e)
                                print("Card number should not have any characters")
                        if receiver == 'c':
                            break

                        pinNum2d = ''
                        while True:
                            try:
                                pin = input("Enter your pin number again: ")
                                if pin.lower() == 'c':
                                    pinNum2d = pin.lower()
                                    break
                                x = int(pin)
                                if len(pin) == 4:
                                    pinNum2d = pin
                                    break
                                else:
                                    print("Pin number should be 4 digits")
                            except Exception as e:
                                # print(e)
                                print("Pin number should not have any characters")
                        if pinNum2d == 'c':
                            print("Cancelled!")
                            break

                        if db.cashTransfer(cardNumber2,pinNum2d,amount,receiver):
                            break

                elif inp2 == 'e':
                    db.showHistory(cardNumber2)
                elif inp2 == 'f':
                    while True:
                        print(">> Change Information\n\nChoose what you want to change in your details\n")
                        print("1.\tFirst Name\t2. Last Name\t3. Occupation\t4. Pin\t5. Cancel\n")
                        inp2f = input("Enter input: ")

                        if inp2f == '1':
                            while True:
                                print(">> Edit first name <<\n\nEnter 'c' if you want to cancel\n")
                                firstName = ''
                                while True:
                                    fName = input("Enter your desired first name: ")
                                    if fName.lower() == 'c':
                                        firstName = fName.lower()
                                        break
                                    if any(not char.isdigit() for char in fName):
                                        if len(fName) > 0:
                                            firstName = fName
                                            break
                                        else:
                                            print(
                                                "Oops! It seems you left the first name field blank. Please enter your first name.")
                                    else:
                                        print("First name should not contains numbers\n")
                                if firstName == 'c':
                                    print("Cancelled!")
                                    break

                                pinNum2f1 = ''
                                while True:
                                    try:
                                        pin = input("Enter your pin number again: ")
                                        if pin.lower() == 'c':
                                            pinNum2f1 = pin.lower()
                                            break
                                        x = int(pin)
                                        if len(pin) == 4:
                                            pinNum2f1 = pin
                                            break
                                        else:
                                            print("Pin number should be 4 digits")
                                    except Exception as e:
                                        # print(e)
                                        print("Pin number should not have any characters")
                                if pinNum2f1 == 'c':
                                    print("Cancelled!")
                                    break

                                if db.logIn(cardNumber2,pinNum2f1,2):
                                    db.updateFirstName(firstName,cardNumber2)
                                    break

                        elif inp2f == '2':
                            while True:
                                print(">> Edit last name <<\n\nEnter 'c' if you want to cancel\n")
                                lastName = ''
                                while True:
                                    lName = input("Enter your desired last name: ")
                                    if lName.lower() == 'c':
                                        lastName = lName.lower()
                                        break
                                    if any(not char.isdigit() for char in lName):
                                        if len(lName) > 0:
                                            lastName = lName
                                            break
                                        else:
                                            print(
                                                "Oops! It seems you left the last name field blank. Please enter your last name.")
                                    else:
                                        print("Last name should not contains numbers\n")
                                if lastName == 'c':
                                    print("Cancelled!")
                                    break

                                pinNum2f2 = ''
                                while True:
                                    try:
                                        pin = input("Enter your pin number again: ")
                                        if pin.lower() == 'c':
                                            pinNum2f2 = pin.lower()
                                            break
                                        x = int(pin)
                                        if len(pin) == 4:
                                            pinNum2f2 = pin
                                            break
                                        else:
                                            print("Pin number should be 4 digits")
                                    except Exception as e:
                                        # print(e)
                                        print("Pin number should not have any characters")
                                if pinNum2f2 == 'c':
                                    print("Cancelled!")
                                    break
                                if db.logIn(cardNumber2, pinNum2f2,2):
                                    db.updateLastName(lastName, cardNumber2)
                                    break

                        elif inp2f == '3':
                            while True:
                                print(">> Edit Occupation <<\n\nEnter 'c' if you want to cancel")

                                occupation = ''
                                while True:
                                    occu = input("Enter your new occupation: ")
                                    if occu.lower() == 'c':
                                        occupation = occu.lower()
                                        break
                                    if any(not char.isdigit() for char in occu):
                                        if occu == 'c':
                                            occupation = occu
                                            break
                                        if len(occu) > 0:
                                            occupation = occu
                                            break
                                        else:
                                            print(
                                                "Oops! It seems you left the occupation field blank. Please enter your occupation.")
                                    else:
                                        print("Enter valid occupation.\n")
                                if occupation == 'c':
                                    print("Cancelled!")
                                    break

                                pinNum2f3 = ''
                                while True:
                                    try:
                                        pin = input("Enter your pin number again: ")
                                        if pin.lower() == 'c':
                                            pinNum2f3 = pin.lower()
                                            break
                                        x = int(pin)
                                        if len(pin) == 4:
                                            pinNum2f3 = pin
                                            break
                                        else:
                                            print("Pin number should be 4 digits")
                                    except Exception as e:
                                        # print(e)
                                        print("Pin number should not have any characters")
                                if pinNum2f3 == 'c':
                                    print("Cancelled!")
                                    break
                                if db.logIn(cardNumber2,pinNum2f3,2):
                                    db.updateOccupation(occupation,cardNumber2)
                                    break

                        elif inp2f == '4':
                            while True:
                                print(">> Edit pin <<\n\nEnter 'c' if you want to cancel")

                                newPinNum = ''
                                while True:
                                    try:
                                        pin = input("Enter your new desired pin number again: ")
                                        if pin.lower() == 'c':
                                            newPinNum = pin.lower()
                                            break
                                        x = int(pin)
                                        if len(pin) == 4:
                                            newPinNum = pin
                                            break
                                        else:
                                            print("Pin number should be 4 digits")
                                    except Exception as e:
                                        # print(e)
                                        print("Pin number should not have any characters")
                                if newPinNum == 'c':
                                    print("Cancelled!")
                                    break

                                oldPinNum = ''
                                while True:
                                    try:
                                        pin = input("Enter your pin number again: ")
                                        if pin.lower() == 'c':
                                            oldPinNum = pin.lower()
                                            break
                                        x = int(pin)
                                        if len(pin) == 4:
                                            oldPinNum = pin
                                            break
                                        else:
                                            print("Pin number should be 4 digits")
                                    except Exception as e:
                                        # print(e)
                                        print("Pin number should not have any characters")
                                if oldPinNum == 'c':
                                    print("Cancelled!")
                                    break

                                if db.logIn(cardNumber2,oldPinNum,2):
                                    globalPin = newPinNum
                                    db.updatePin(cardNumber2,newPinNum)
                                    break

                        elif inp2f == '5':
                            break
                        else:
                            print("Invalid Input\n")

                elif inp2 == 'g':
                    db.showInfo(cardNumber2,globalPin)
                elif inp2 == 'h':
                    db.logOut(cardNumber2,pin)
                    break
                else:
                    print("Invalid Input\n")

    elif inp == '3':
        print(f"\n{'-'*7} GOODBYE! {'-'*7}")
        break
    else:
        print("Invalid Input.\n")
