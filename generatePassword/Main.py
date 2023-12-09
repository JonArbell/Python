import GeneratedPassword as gp
import Database as db

while True:

    try:
        print(f"{'-'*5} Welcome to Password Generator! {'-'*5}\n")
        print(" >> What would you like to do? <<\n")
        print(f"1.\tGenerate Password\n2.\tShow Generated Passwords\n3.\tDelete Generated Password\n4.\tExit\n")

        answer = int(input("Enter input: "))

        if answer == 1:
            while True:
                print("What type of password do you want? ")
                print("\na.\tWeak Password\nb.\tModerate Password\nc.\tStrong Password\nd.\tExit")
                ans1 = input("Enter input: ")
                if ans1 == 'a':
                    name = input("Enter your name: ")
                    app = input("Enter the application name: ")
                    db.insertData(name,app,gp.weakPass())
                    break
                elif ans1 == 'b':
                    name = input("Enter your name: ")
                    app = input("Enter the application name: ")
                    db.insertData(name,app,gp.moderatePass())
                    break
                elif ans1 == 'c':
                    name = input("Enter your name: ")
                    app = input("Enter the application name: ")
                    db.insertData(name,app,gp.strongPass())
                    break
                elif ans1 == 'd':
                    break
                else:
                    print("Invalid Input")
        elif answer == 2:
            db.showData()
        elif answer == 3:
            name3= input("Enter the name: ")
            password3 = input("Enter the password: ")
            db.deleteData(name3,password3)


        elif answer == 4:
            print(f"{'-'*5} Goodbye! {'-'*5}")
            break
        else:
            print("Invalid Input\n")

    except Exception as e:
        print(e)
        print("Input should not contain any characters\n")


