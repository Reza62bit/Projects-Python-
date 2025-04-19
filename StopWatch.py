import time
from os import system
# main loop

while True:
    print("Welcome to the stopwatch, Choose between the options below:\n\t1) Start\n\t2) Exit")
    user_choice = input("Your choice: ")

    # option 1

    if user_choice == "1":
        print("fill the questions below: ")
        print()
        hour = int(input("Hour(s): "))
        minute = int(input("Minute(s): "))
        second = int(input("Second(s): "))

        # Invalid values Error

        if minute > 60 or second > 60:
            print("Error, Invalid values! (min and sec values should be under 60!)")
            print()
            continue

        print("StopWatch starts in 3...")
        time.sleep(1)
        print("StopWatch starts in 2...")
        time.sleep(1)
        print("StopWatch starts in 1...")
        time.sleep(1)
        system("cls")

        # stopwatch loop

        while True:
            print(hour, ":", minute, ":", second)
            if second >= 1:
                time.sleep(1)
            system("cls")
            if hour >= 1 and minute == 0 and second == 0:
                hour -= 1
                minute += 59
                second += 60

            elif hour >= 0 and minute >= 1 and second == 0:
                minute -= 1
                second += 60

            elif hour == 0 and minute == 0 and second == 0:
                print("Finished!!")
                break
            second -= 1

    # option 2

    elif user_choice == "2":

        # asking again if the user want to exit

        print()
        ex = input("Are you sure? (y/n) ")
        if "y" in ex.lower():
            print("GoodBye!")
            input("Press any key to exit")
            break

        else:
            print()
            continue

    # Error

    else:
        print("Error, Out of range! (Invalid answer)")
        print()
