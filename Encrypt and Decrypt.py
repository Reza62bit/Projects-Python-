from random import randint, seed
while True:
    # random seed generator
    seed(input("Enter a random number (you need it for decryption, so remember it): "))
    # options
    print()
    print("Options:\n\t1) Encrypt\n\t2) Decrypt\n\t3) Exit")
    user_choice = input("What do you want to do? ")
    print()

    # option 1

    if user_choice == "1":
        plain_text = input("Write the text that you wanna ENCRYPT: ")
        encrypted_text = ""
        for char in plain_text:
            x = ord(char) * randint(1, 10) + 6
            encrypted_text += chr(x)
        print()
        print("Process finished, Your encrypted text:", encrypted_text)
        print()

        # asking if the user wants to continue or not

        user_choice2 = input("Do you want to continue? (y/n) ")
        if "n" in user_choice2.lower():
            print("GoodBye!")
            input("Press any key to exit")
            break
        else:
            pass
        print()

    # option 2

    elif user_choice == "2":
        encrypted_text = input("Write the text that you wanna DECRYPT: ")
        plain_text = ""
        for char in encrypted_text:
            x = (ord(char) - 6) // randint(1, 10)
            plain_text += chr(x)
        print()
        print("Process finished, Your decrypted text:", plain_text)
        print()

        # asking if the user wants to continue or not

        user_choice3 = input("Do you want to continue? (y/n) ")
        if "n" in user_choice3.lower():
            print("GoodBye!")
            input("Press any key to exit")
            break
        else:
            pass
        print()

    # option 3

    elif user_choice == "3":
        user_choice4 = input("Are you sure? (y/n) ")
        if "y" in user_choice4.lower():
            print("Goodbye!")
            input("Press any key to exit")
            break
        else:
            pass
        print()

    # Error

    else:
        print("Error!, out of range!! (Invalid answer)")
        print()

# END OF PROJECT
