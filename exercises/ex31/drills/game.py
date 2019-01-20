def start():
    loop()    

def victory():
    print("Victorius!")
    print("Exit? (y / n)")

    exit = input("> ")

    if "y" in exit or "Y" in exit:
        exit(0)
    else:
        start()

def death():
    print("You have lost your mind and your body, you are dead.")
    exit_inp = input("Do you want to continue? Y/N ")
    exit_inp = exit_inp.lower()
		
    if exit_inp == "n":
        exit(0)
    elif exit_inp == "y":
        start()
    else:
        print("Incorrect command, try again")
        death()

def loop():
    print("""
    ---------------------------------------------------------
    You are standing in an open field west of a white house, with a boarded front door.
    (A secret path leads southwest into the forest.)
    There is a Small Mailbox.
    From here, you can go north, south, east or west.
    ---------------------------------------------------------
    """)
    action = input("What do you do? > ")
    
    while True:
        if action.lower() == ("take mailbox"):
            print("---------------------------------------------------------")
            print("It is securely anchored.")
        elif action.lower() == ("open mailbox"):
            print("---------------------------------------------------------")
            print("Opening the small mailbox reveals a leaflet.")
        elif action.lower() == ("open door"):
            print("---------------------------------------------------------")
            print("The door cannot be opened.")
        elif action.lower() == ("take boards"):
            print("---------------------------------------------------------")
            print("The boards are securely fastened.")
        elif action.lower() == ("look at house"):
            print("---------------------------------------------------------")
            print("The house is a beautiful colonial house which is painted white. It is clear that the owners must have been extremely wealthy.")
        elif action.lower() == ("read leaflet"):
            print("---------------------------------------------------------")
            print("To whomever this may concern: keep going north.")
        elif "north" in action.lower():
            cthulhu()
        elif "south" in action.lower():
            prince()
        elif "east" in action.lower():
            princess()
        elif "west" in action.lower():
            lion()
        else:
            print("I got no idea what you're saying. Is it that hard picking a cardinal direction?")