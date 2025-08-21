import time

# main loop

while True:

    # Options

    print("Welcome to the Timer!")
    print()
    print("Choose between the options below:\n\t1) Start the timer\n\t2) Exit")
    print()
    user_choice1 = input("Your choice: ")

    # Option 1

    if user_choice1 == "1":
        input()

    # Option 2

    elif user_choice1 == "2":
        print()
        user_choice2 = input("Are you sure? (y/n) ")
        if "y" in user_choice2:

            print('GoodBye!')
            
            input("Press any key to exit")
            break
    # Error

    else:
        print("Error!, out of range! (Wrong answer) ")
        print()
