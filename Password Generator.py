import random
import string

# materials

letter = string.ascii_letters
symbols = "!@#$%&*"
num = "0123456789"
al = letter + symbols + num

# main loop

while True:
    print("Options:\n\t1) Generate a random password\n\t2) Exit")
    choice = input("Choose your option: ")
    print()

    # option 1

    if choice == "1":
        length = int(input("Enter the number of characters: "))

        # Retrying loop

        while True:
            password = random.sample(al, length)
            print()
            print("Process finished!, Your password:", "".join(password))
            x = input("Retry? (y/n) ")
            if "y" in x.lower():
                continue
            else:
                break

    # option 2

    elif choice == "2":
        y = input("Are you sure? (y/n) ")
        if "y" in y.lower():
            print('GoodBye!')
            input("press any key to exit")
            break
        else:
            pass
    # Error
    else:
        print("Error!, out of range!! ('Invalid answer')")
        print()

# END OF PROJECT
