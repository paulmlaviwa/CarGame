user_input = ""
started = False
while True:
    user_input = input(">> ").lower()
    if user_input == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car started... Ready to go!")
    elif user_input == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car stopped")
    elif user_input == "quit":
        exit()
    elif user_input == "help":
        print('''
start - to start the car
stop - to stop the car
quit - to exit
        ''')
    else:
        print(f"Sorry, I don't understand '{user_input}'")

