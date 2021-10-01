# CLI(Command line interface) text-based, required

def choice_one():
    print("Handle first option")

def choice_two():
    print("Handle second option")

def choice_three():
    print("Handle third option")

def main():
    while True:
        # display the menu
        print("[1] First option")
        print("[2] Second option")
        print("[3] Third option")
        print("[q]uit")
        # get the user choice
        print()
        print("Make a selection.")
        choice = input("> ")
        print()

        # handle the choice
        if choice == "1":
            choice_one()
        elif choice == "2":
            choice_two()
        elif choice == "3":
            choice_three()
        elif choice == "q":
            print("Bye")
            break

        print()
        input("Enter to contiune")
        print()


if __name__== "__main__":
    main()
