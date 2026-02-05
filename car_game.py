#car game 
car_started = False 
while True:
    user_input = str(input("> ")).lower()
    if user_input == "help":
        print("start-to start the game! \nstop-to stop the game! \nquite-to exit the game!" )
    elif user_input == "start":
        if not car_started:
            car_started = True
            print('Car is started!')
        else:
            print('car is already started')
    elif user_input == "stop":
        if car_started:
            car_started = False
            print('Car stopped!')
        else:
            print("Car is alredy stopped!")
    elif user_input == "quite":
        print('Exiting game.Goodbye!')
    else:
        print("Invalid command. Type 'help' for options.")
