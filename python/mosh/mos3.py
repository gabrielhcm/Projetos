command = ""

estado = ""
estado2 = ""
while True:
    command = input("").lower()
    if command == "start" and estado == "":
        print("Car started..")
        estado = "started"
    elif command == "stop" and estado2 == "":
        print("car stopped") 
        estado2 = "stopped"
    elif estado == "started" and command =="start":
        print("car already started")
    elif estado2 == "stopped"and command =="stop":
        print("car already stopped")
    elif command == "help":
        print("""
start - start the car
stop - stop the car
help - show commands
quit - quit the program
        """)
    elif command =="quit":
        break    
    else:
        print("nao entendi, digite outro comando!")
