#imports
import time
import os
import random
import pygame

#Game Variables
total_actions = 0   
clock = "12:00 AM"
Foxy_Stage = 0
Ldoor = 0
Rdoor = 0
Freddy_POS = 0
Chica_POS = 0
Bonnie_POS = 0 
Endo_POS = 0
power = 200
usage = 0
Foxy_Energy = 0
Freddy_AI = 0
Bonnie_AI = 0
Chica_AI = 0
Endo_AI = 0
Foxy_AI = 0
cams_on = 0
Endo_Flashed = 0
Foxy_INCOMING = 0
Endo_waiting = 0
Bonnie_Waiting = 0
Chica_Waiting = 0
Freddy_Waiting = 0

#Functions
def Bonnie_Move():
    global Bonnie_POS, Ldoor
    a = 0
    if Bonnie_AI >= random.randint(0,20):
        if Bonnie_POS == 0:
            Bonnie_POS = random.randint(0,1)
        elif Bonnie_POS == 1:
            Bonnie_POS = random.randint(1,3)
        elif Bonnie_POS == 2:
            Bonnie_POS = random.randint(1,4)
        elif Bonnie_POS == 3:
            Bonnie_POS = random.randint(2,6)
        elif Bonnie_POS == 4:
            Bonnie_POS = random.randint(3,5)
        elif Bonnie_POS == 5:
            if not Endo_POS >6:
                Bonnie_POS = random.randint(5,6)
            else:
                Bonnie_POS = 5 
            Bonnie_POS = random.randint(5,6)
        elif Bonnie_POS == 6:
            if Bonnie_Waiting < 1:
                if Ldoor == 1:
                    a = random.randint(0,3)
                    if a == 1:
                        Bonnie_POS = 6
                    else:
                        Bonnie_POS = a
                else:
                    Bonnie_POS = 7
            else: 
                Bonnie_POS = 6
    if Bonnie_POS == 6 and Ldoor == 1:
        if random.randint(0,2) == 1:
            Bonnie_POS = random.randint(0,2)
    if Bonnie_POS == 7 and cams_on == 1:
        print("   __________________________________________________________________")
        print("  /                                                                 \\")
        print(" |                                                                   |")
        print(" |                                                                   |")
        print(" |                                                                   |")
        print(" |                                                                   |")
        print(" |                                                                   |")
        print(" |                                                                   |")
        print(" |                                                                   |")
        print(" |                                                                   |")
        print(" |                                                                   |")
        print(" |                                                                   |")
        print(" |                                                                   |")
        print(" |                                                                   |")
        print(" |                                                                   |")
        print(" |                                                                   |")
        print(" |                                                                   |")
        print(" |                                                                   |")
        print(" |                                                                   |")
        print(" |                                                                   |")
        print(" |                                                                   |")
        print(" |                                                                   |")
        print(" |                                                                   |")
        print(" |                                                                   |")
        print(" |                                                                   |")
        print("  \\_________________________________________________________________/")        
        
        
def Chica_Move():
    global Chica_POS, Rdoor
    a = None
    if Chica_AI > random.randint(0,20):
        if Chica_POS == 0:
            Chica_POS = random.randint(0,1)
        elif Chica_POS == 1:
            Chica_POS = random.randint(1,3)
        elif Chica_POS == 2:
            a = random.randint(1,4)
            if not a == 3:
                Chica_POS = a
        elif Chica_POS == 3:
            a = random.randint(2,6)
            if not a == 4:
                Chica_POS = a
        elif Chica_POS == 4:
            a = random.randint(2,5)
            if not a == 3:
                Chica_POS = a
        elif Chica_POS == 5:
            if not Freddy_POS > 5:
                Chica_POS = random.randint(5,6)
            else:
                Chica_POS = 5
        elif Chica_POS == 6:
            Chica_Waiting = random.randint(3,5)
            if Rdoor == 1:
                a = random.randint(0,3)
                if a == 2:
                    Chica_POS = 6
                else:
                    Chica_POS = a
            elif Chica_Waiting < 1:
                Chica_POS = 7
            else:
                Chica_POS = 6
    if Chica_POS == 6 and Rdoor == 1:
        if random.randint(0,2) == 1:
            Chica_POS = random.randint(0,2)
    if Chica_POS == 7 and cams_on == 1:
        input("CHICA JUMPSCARE PRESET: ")

def Endo_Move():
    global Endo_POS, Endo_Flashed
    if Endo_AI > random.randint(0,20):
        if Endo_POS < 5:
            Endo_POS = random.randint(0,5)
        if Endo_POS == 5:
            if not Bonnie_POS > 5:
                Endo_POS = 6
                Endo_waiting = random.randint(3,7)
            else:
                Endo_POS = 5
        if Endo_POS == 6:
            if Endo_waiting < 1:
                Endo_POS = 7
            Endo_POS = 7
    if  Endo_POS == 7 and cams_on == 1 and not Ldoor == 1:
            input("ENDO JUMPSCARE PRESET: ")

def Foxy_Move():
    global Foxy_Stage, Foxy_Energy, cams_on, Foxy_INCOMING
    if cams_on == 0:
        Foxy_Energy += Foxy_AI
        if Foxy_Energy >= 80:
            Foxy_Stage += 1
            Foxy_Energy = 0
            if Foxy_Stage == 4:
                print("FOXY RUNNING PRESET")
                if Foxy_INCOMING <1:
                    if Ldoor == 1:
                        Foxy_Energy = random.randint(0,20)
                        Foxy_Stage = random.randint(0,1)
                    else:
                        input("FOXY JUMPSCARE PRESET")

                
    else:
        Foxy_Energy -= 10
        if Foxy_Energy < 0:
            Foxy_Energy = 0

def Freddy_Move():
    a = None
    global Freddy_POS, Rdoor
    if Freddy_AI > random.randint(0,20):
        if Freddy_POS == 0:
            Freddy_POS = random.randint(0,1)
        elif Freddy_POS == 1:
            Freddy_POS = random.randint(1,3)
        elif Freddy_POS == 2:
            a = random.randint(1,4)
            if not a == 3:
                Freddy_POS = a
        elif  Freddy_POS == 3:
            a = random.randint(2,6)
            if not a == 4:
                Freddy_POS = a
        elif Freddy_POS == 4:
            a = random.randint(2,5)
            if not a == 3:
                Freddy_POS = a
        elif Freddy_POS == 5:
            if not Chica_POS > 6:
                Freddy_POS = random.randint(5,6)
            else:
                Freddy_POS = 5
        elif Freddy_POS == 6:
            if Rdoor == 1:
                a = random.randint(0,3)
                if a == 2:
                    Freddy_POS = 6
                else:
                    Freddy_POS = a
            else:
                Freddy_POS = 7
    if Freddy_POS == 7:
        input("FREDDY JUMPSCARE PRESET: ")    

def end_night():
    global night
    for i in range(random.randint(1,3)):
        os.system("cls")
        os.system("color 0F")
        print(f"| |=================================================================| |")
        print(f"| |=================================================================| |")
        print(f"| |                                                                 | |")
        print(f"| |                              _______                            | |")
        print(f"| |                /            |       |   |\     /|               | |")
        print(f"| |               /             |       |   | \   / |               | |")
        print(f"| |              /____          |_______|   |  \_/  |               | |")
        print(f"| |             /     \         |       |   |       |               | |")
        print(f"| |            |      |         |       |   |       |               | |")
        print(f"| |             \____/          |       |   |       |               | |")
        print(f"| |                                                                 | |")
        print(f"| |                                                                 | |")
        print(f"| |                                                                 | |")
        print(f"| |                                                                 | |")
        print(f"| |                                                                 | |")
        print(f"| |                                                                 | |")
        print(f"| |=================================================================| |")
        print(f"| |=================================================================| |")  
        time.sleep(0.5) 
        os.system("color 0A")
        os.system("cls")
        print(f"| |=================================================================| |")
        print(f"| |=================================================================| |")
        print(f"| |                                                                 | |")
        print(f"| |                              _______                            | |")
        print(f"| |                /            |       |   |\     /|               | |")
        print(f"| |               /             |       |   | \   / |               | |")
        print(f"| |              /____          |_______|   |  \_/  |               | |")
        print(f"| |             /     \         |       |   |       |               | |")
        print(f"| |            |      |         |       |   |       |               | |")
        print(f"| |             \____/          |       |   |       |               | |")
        print(f"| |                                                                 | |")
        print(f"| |                                                                 | |")
        print(f"| |                                                                 | |")
        print(f"| |                                                                 | |")
        print(f"| |                                                                 | |")
        print(f"| |                                                                 | |")
        print(f"| |=================================================================| |")
        print(f"| |=================================================================| |")   

    action = get_int_input("1. Continue to next night 2. Main Menu ", [1, 2])
    if action == 1:
        night += 1
        save_game()
        night_start()  
    elif action == 2:
        night += 1
        save_game()
        menu()

def power_drain( ):
        global power
        global usage
        power -= usage
        os.system("cls")
        if power <= 0:
            power = 0
            print("   __________________________________________________________________")
            print("  /                           ____/    |   |    |                   \\")
            print(" |                        ___/         |   |    |                     |")
            print(" |                   ____/             |   |    |                     |")
            print(" |                   |                 |   |    |                     |")
            print(" |                   |                 |   |    |             ________|")
            print(" |                   |                 |   |    |_____________|       |")
            print(" |                   |                 |   |                  |   POWE|")
            print(" |                   |                 |   |                  |    OUT|")
            print(" |                   |                 |   |                  |       |")
            print(" |                   |                 |   |__________________|       |")
            print(" |            _______|                 |   / /________________________|")
            print(" |           |       |                 |  /  |                        |")
            print(" |           |       |                 | /   |________________________|")
            print(" |           |       |                 |/    | |                      |")
            print(" |           |       |                 /     | |                      |")
            print(" |           |       |                /      | |                      |")
            print(" |           |_______|               /       | |                      |")
            print(" |                   |              /                                 |")
            print(" |                   |             /                                  |")
            print(" |                   |            /                                   |")
            print(" |                   |           /                                    |")
            print(" |                   |          /                                     |")
            print(" |                   |         /                                      |")
            print(" |                   |        /                                       |")
            print("  \\__________________|_______/_______________________________________/")
            print("power left:", power,"%")
            while True:
                time.sleep(2)
                total_actions = update_clock(3)
                if random.randint(1,30) <=  Freddy_AI + 5:
                    for i in range(random.randint(1,3)):
                        os.system("cls")
                        print("   __________________________________________________________________")
                        print("  /                           ____/    |   |    |                   \\")
                        print(" |                        ___/         |   |    |                     |")
                        print(" |                   ____/             |   |    |                     |")
                        print(" |                   |       _         |   |    |                     |")
                        print(" |                   |      |█|        |   |    |             ________|")
                        print(" |                   | {  ^/|█|\^  }   |   |    |_____________|       |")
                        print(" |                   | { /0     0\ }   |   |                  |   POWE|")
                        print(" |                   | { \   O   / }   |   |                  |    OUT|")
                        print(" |                   |   _|^v^v^|_     |   |                  |       |")
                        print(" |                   |  /   >O<   \    |   |__________________|       |")
                        print(" |            _______|  |  /   \  |    |   / /________________________|")
                        print(" |           |       |  | |     | |    |  /  |                        |")
                        print(" |           |       |  | |     | |    | /   |________________________|")
                        print(" |           |       |  | |     | |    |/    | |                      |")
                        print(" |           |       |                 /     | |                      |")
                        print(" |           |       |                /      | |                      |")
                        print(" |           |_______|               /       | |                      |")
                        print(" |                   |              /                                 |")
                        print(" |                   |             /                                  |")
                        print(" |                   |            /                                   |")
                        print(" |                   |           /                                    |")
                        print(" |                   |          /                                     |")
                        print(" |                   |         /                                      |")
                        print(" |                   |        /                                       |")
                        print("  \\__________________|_______/_______________________________________/")
                        print("power left:", power,"%")
                        time.sleep(2)
                        total_actions = update_clock(2)
                        os.system("cls")
                        print("   __________________________________________________________________")
                        print("  /                           ____/    |   |    |                   \\")
                        print(" |                        ___/         |   |    |                     |")
                        print(" |                   ____/             |   |    |                     |")
                        print(" |                   |       _         |   |    |                     |")
                        print(" |                   |      |█|        |   |    |             ________|")
                        print(" |                   |{   ^/|█|\^    } |   |    |_____________|       |")
                        print(" |                   |{  /0     0\   } |   |                  |   POWE|")
                        print(" |                   |{  \   O   /   } |   |                  |    OUT|")
                        print(" |                   |   _|^v^v^|_     |   |                  |       |")
                        print(" |                   |  /   >O<   \    |   |__________________|       |")
                        print(" |            _______|  |  /   \  |    |   / /________________________|")
                        print(" |           |       |  | |     | |    |  /  |                        |")
                        print(" |           |       |  | |     | |    | /   |________________________|")
                        print(" |           |       |  | |     | |    |/    | |                      |")
                        print(" |           |       |                 /     | |                      |")
                        print(" |           |       |                /      | |                      |")
                        print(" |           |_______|               /       | |                      |")
                        print(" |                   |              /                                 |")
                        print(" |                   |             /                                  |")
                        print(" |                   |            /                                   |")
                        print(" |                   |           /                                    |")
                        print(" |                   |          /                                     |")
                        print(" |                   |         /                                      |")
                        print(" |                   |        /                                       |")
                        print("  \\__________________|_______/_______________________________________/")
                        print("power left:", power,"%")
                        time.sleep(2)
                        total_actions  = update_clock(2)
                    os.system("cls")
                    print('Jumscare Preset')
                    input("Continue... ")
                    menu()
                    break
                else:
                    pass

def update_clock(actions):
    global total_actions
    total_actions += actions
    print(f"Total actions this night: {total_actions}")
    if total_actions >= 360:
        time.sleep(2)
        end_night()
    return total_actions

def update_ingame_clock():
    if total_actions >= 60 and total_actions < 120:
        return "01:00 AM"
    elif total_actions >= 120 and total_actions < 180:   
        return "02:00 AM"
    elif total_actions >= 180 and total_actions < 240:
        return "03:00 AM"
    elif total_actions >= 240 and total_actions < 300:
        return "04:00 AM"
    elif total_actions >= 300 and total_actions < 360:
        return "05:00 AM"
    elif total_actions >= 360:
        return "06:00 AM"        
    else:
        return "12:00 AM"

def move_opportunity():
    global Foxy_Stage, Foxy_INCOMING, Endo_waiting, Bonnie_Waiting, Chica_Waiting, Freddy_Waiting
    if Foxy_Stage == 4:
        Foxy_INCOMING -=1
    if Endo_POS == 6:
        Endo_waiting -= 1
    if Bonnie_POS == 6:
        Bonnie_Waiting -= 1
    if Chica_POS == 6:
        Chica_Waiting -= 1
    if Freddy_POS == 6:
        Freddy_Waiting -= 1
    
    if Endo_POS == 6:
        Endo_waiting -= 1
    if Bonnie_AI > 0:
        if random.randint(0,2) < night:
            Bonnie_Move()
    if Chica_AI > 0:
        if random.randint(0,3) < night:
            Chica_Move()
    if Endo_AI > 0:
        if random.randint(0,3) < night:
            Endo_Move()
    if Foxy_AI > 0:
        Foxy_Move()
    if Freddy_AI > 0:
        Freddy_Move()

def clear_save():
    global night
    if os.path.exists("savegame.txt"):
        os.remove("savegame.txt")
        night = 0

def get_int_input(prompt, valid_options=None):
    """Safely get an integer from user; reprompts on empty or invalid input."""
    while True:
        try:
            s = input(prompt)
        except EOFError:
            print("\nNo input provided.")
            continue
        if s.strip() == '':
            print("No input entered.")
            continue
        try:
            val = int(s)
        except ValueError:
            if s.strip() == 1987:
                exit()
            else:
                print("Invalid input. Please enter a number.")
                continue
        if valid_options is not None and val not in valid_options:
            print("Invalid option.")
            continue
        return val

def check_for_movement():
    global usage, power, total_actions,cams_on
    if power - usage <= 0:
        power_drain()
    elif total_actions + 2 >= 360:
        total_actions = update_clock(2)
    else:
        total_actions = update_clock(2)
        power_drain()
        foxy_on_stage = "Fx0" if Foxy_Stage == 0 else "Fx1" if Foxy_Stage == 1 else "Fx2" if Foxy_Stage == 2 else  "Fx3" if Foxy_Stage == 3 else "-0-"    
        LdoorS = " " if Ldoor == 0 else "["
        RdoorS = " " if Rdoor == 0 else "]"

        os.system("cls")
        print("   __________________________________________________________________")
        print("  /                   _________________________                     \\")
        if Bonnie_POS == 0 and Chica_POS == 0 and Freddy_POS == 0:
            print(" |                    |   C       F       B   |                      |")
        elif Bonnie_POS == 0 and Chica_POS == 0:
            print(" |                    |   C               B   |                      |")
        elif Bonnie_POS == 0 and Freddy_POS == 0:
            print(" |                    |           F       B   |                      |") 
        elif Chica_POS == 0 and Freddy_POS == 0:
            print(" |                    |   C       F           |                      |")
        elif Bonnie_POS == 0:
            print(" |                    |                   B   |                      |")
        elif Chica_POS == 0:
            print(" |                    |   C                   |                      |")
        elif Freddy_POS == 0:
            print(" |                    |           F           |                      |")
        else:
            print(" |                    |                       |                      |")
        
        print(" |  ___________ ______|_______________________|______ _________ _____|")
        if Bonnie_POS == 2 and Endo_POS == 0:  
            print(" | |  E    B   |                                     |         |     |")
        elif Bonnie_POS == 2:
            print(" | |        B  |                                     |         |     |")
        elif Endo_POS == 0:
            print(" | |  E        |                                     |         |     |")
        else:
            print(" | |           |                                     |         |     |")
        if Bonnie_POS == 1 and Endo_POS == 1 and Chica_POS == 1 and Freddy_POS == 1:
            print(" | |           |    E      B      C      F           |               |")
        elif Bonnie_POS == 1 and Endo_POS == 1 and Chica_POS == 1:
            print(" | |           |    E      B      C                  |               |")  
        elif Bonnie_POS == 1 and Endo_POS == 1 and Freddy_POS == 1:
            print(" | |           |    E      B             F           |               |")
        elif Bonnie_POS == 1 and Chica_POS == 1 and Freddy_POS == 1:
            print(" | |           |            B      C      F          |               |")
        elif Endo_POS == 1 and Chica_POS == 1 and Freddy_POS == 1:
            print(" | |           |    E             C      F           |               |")
        elif Bonnie_POS == 1 and Endo_POS == 1:
            print(" | |           |    E      B                         |               |")
        elif Bonnie_POS == 1 and Chica_POS == 1:
            print(" | |           |            B      C                 |               |")
        elif Bonnie_POS == 1 and Freddy_POS == 1:
            print(" | |           |            B             F          |               |")
        elif Endo_POS == 1 and Chica_POS == 1:
            print(" | |           |    E             C                  |               |")
        elif Endo_POS == 1 and Freddy_POS == 1:
            print(" | |           |    E                  F             |               |")
        elif Chica_POS == 1 and Freddy_POS == 1:
            print(" | |           |            C      F                 |               |")
        elif Bonnie_POS == 1:
            print(" | |           |            B                        |               |")
        elif Endo_POS == 1:
            print(" | |           |    E                                |               |")
        elif Chica_POS == 1:
            print(" | |           |                  C                  |               |")
        elif Freddy_POS == 1:
            print(" | |           |                       F             |               |")
        else:
            print(" | |           |                                     |               |")
        if Chica_POS == 2 and Freddy_POS == 2:
            print(" | |           |                                     |  C   F  |-----|")
        elif Chica_POS == 2:
            print(" | |           |                                     |  C      |-----|")
        elif Freddy_POS == 2:
            print(" | |           |                                     |       F |-----|")
        else:
            print(" | |           |                                     |         |-----|")
        print(" | |           |______                               |         |-----|")
        
        print(" | |           |      |                              |               |")
        if Endo_POS == 2:
            print(f" | |___________| {foxy_on_stage}  |       E                      |         |_____|")    
        else:
            print(f" | |___________| {foxy_on_stage}  |                              |         |_____|")
        print(" |             |______|______________________________|_________|     |")
        if Bonnie_POS == 4:
            print(" |             |   B  |      |         |       |            |        |")
        else:
            print(" |             |      |      |         |       |            |        |")
        if Bonnie_POS == 3 and Chica_POS == 3:
            print(" |             |      |  B   |         |   C   |  NO VIDEO  |        |")
        elif Bonnie_POS == 3 and Freddy_POS == 3:
            print(" |             |      |  B   |         |   F   |  NO VIDEO  |        |")
        elif Endo_POS == 3 and Chica_POS == 3:
            print(" |             |      |  E   |         |   C   |  NO VIDEO  |        |")
        elif Endo_POS == 3 and Freddy_POS == 3:
            print(" |             |      |  E   |         |   F   |  NO VIDEO  |        |")
        elif Bonnie_POS == 3:
            print(" |             |      |  B   |         |       |  NO VIDEO  |        |")
        elif Endo_POS == 3:
            print(" |             |      |  E   |         |       |  NO VIDEO  |        |")
        elif Chica_POS == 3:
            print(" |             |      |      |         |   C   |  NO VIDEO  |        |")
        elif Freddy_POS == 3:
            print(" |             |      |      |         |   F   |  NO VIDEO  |        |")
        else:
            print(" |             |      |      |         |       |  NO VIDEO  |        |")
        print(" |             |______|      |         |       | AUDIO ONLY |        |")
        if Foxy_Stage == 4:
            print(" |   CLOSE THE DOOR!  |  FX  |_________|       |____________|        |")
        else:
            print(" |                    |      |_________|       |____________|        |")
        if Foxy_Stage == 4:
            print(" |                    |  VV  |         |       |                     |")
        else:
            print(" |                    |      |         |       |                     |")
        print(f" |                    |      {LdoorS}   YOU   {RdoorS}       |                     |")
        if Bonnie_POS == 5 and Chica_POS == 5:
            print(" |                    |   B  |_________|   C   |                      |")
        elif Bonnie_POS == 5 and Freddy_POS == 5:  
            print(" |                    |   B  |_________|   F   |                     |")
        elif Endo_POS == 5 and Chica_POS == 5:
            print(" |                    |   E  |_________|   C   |                     |")
        elif Endo_POS == 5 and Freddy_POS == 5:
            print(" |                    |   E  |_________|   F   |                     |")
        elif Bonnie_POS == 5:
            print(" |                    |   B  |_________|       |                     |")
        elif Endo_POS == 5:
            print(" |                    |   E  |_________|       |                     |")
        elif Chica_POS == 5:
            print(" |                    |      |_________|   C   |                     |")
        elif Freddy_POS == 5:
            print(" |                    |      |_________|   F   |                     |")
        else:
            print(" |                    |      |_________|       |                     |")
        
        print(" |                    |______|         |_______|                     |")
        print(" |+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+|")
        print(" |COMMANDS:                                                          |")
        print(" |1: CHECK FOR MOVEMENT                                              |")
        print(" |2: TURN OFF MONITOR                                                |")
        print("  \\_________________________________________________________________/")
        print("Power left:", power/2,"%")
        action = get_int_input("Select Action: ", [1, 2])
        if action == 1:
            move_opportunity()
            check_for_movement()
        elif action == 2:
            usage -= 2
            cams_on = 0
            move_opportunity()
            office_main()    

def cams():
        os.system('cls')
        global usage,power,total_actions,cams_on
        cams_on = 1
        usage += 1
        if power - usage <= 0:
            power_drain() 
        elif total_actions + 4 >= 360:
            total_actions = update_clock(4)
        else:
            power_drain()
            total_actions = update_clock(4)
            foxy_on_stage = "F" if Foxy_Stage < 3 else "0"
            LdoorS = " " if Ldoor == 0 else "["
            RdoorS = " " if Rdoor == 0 else "]"
            print("   __________________________________________________________________")
            print("  /                   _________________________                     \\")
            print(" |                    |                       |                      |")
            print(" |  ___________ ______|_______________________|______ _________ _____|")
            print(" | |           |                                     |         |     |")
            print(" | |           |                                     |               |")
            print(" | |           |______                               |         |-----|")
            print(" | |           |      |                              |               |")
            print(f" | |___________|  {foxy_on_stage}   |                              |         |_____|")
            print(" |             |______|______________________________|_________|     |")
            print(" |             |      |      |         |       |            |        |")
            print(" |             |      |      |         |       |  NO VIDEO  |        |")
            print(" |             |______|      |         |       | AUDIO ONLY |        |")
            print(" |                    |      |_________|       |____________|        |")
            print(" |                    |      |         |       |                     |")
            print(f" |                    |      {LdoorS}   YOU   {RdoorS}       |                     |")
            print(" |                    |      |_________|       |                     |")
            print(" |                    |______|         |_______|                     |")
            print(" |+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+|")
            print(" |COMMANDS:                                                          |")
            print(" |1: CHECK FOR MOVEMENT                                              |")
            print(" |2: TURN OFF MONITOR                                                |")
            print("  \\_________________________________________________________________/")
            print("Power left:", power/2,"%")
            action = get_int_input("Select Action: ", [1, 2])
            if action == 1:
                usage += 1
                move_opportunity()
                check_for_movement()
            elif action == 2:
                usage -= 1
                cams_on = 0
                move_opportunity()
                office_main()
        
def light_right():
    global usage, power
    os.system("cls")
    if not Chica_POS == 7 and not Freddy_POS == 7:
        usage += 1
        if power - usage <= 0:
            power_drain()
        else:
            power_drain()
            if Freddy_POS >= 6:
                print("   __________________________________________________________________")
                print("  /                   |    |   |    \____                           \\")
                print(" |                    |    |   |         \____                       |")
                print(" |                    |    |   |              \ _                    |")
                print(" |                    |    |   |                |                    |")
                print(" |_________           |    |   |  ITS ME        |                    |")
                print(" |   /    |___________|    |   |       _ITs mE  |                    |")
                print(" |  /     |                |   |      |█|       |                    |")
                print(" | { P    |                |   |    ^/|█|\^     |                    |")
                print(" | { R    |                |   |   /0     0\    |                    |")
                print(" | { E    |________________|   |   \   O   /    |                    |")
                print(" |<<_S__________________\  |   |   _|^v^v^|_    |__________          |")
                print(" | { S                  |  \   |  /   >O<   \   |   DOOR  |          |")
                print(" |_{____________________|   \  |  |  /   \  |   |    (1)  |          |")
                print(" | { 3                | |    \ |  | |     | |   |         |          |")
                print(" |  \                 | |     \|  | |     | |   |  LIGHT  |          |")
                print(" |   \                | |      \                |    (2)  |          |")
                print(" |                    | |       \  ITS  ME      |_________|          |")
                print(" |                               \              |                    |")
                print(" |                                \    ItS Me   |                    |")
                print(" |                                 \            |                    |")
                print(" |                                  \           |                    |")
                print(" |                                   \          |                    |")
                print(" |                                    \         |                    |")
                print(" |                                     \        |                    |")
                print("  \\____________________________________\_______|____________________/")
            elif Chica_POS >= 6:
                print("   __________________________________________________________________")
                print("  /                   |    |   |__  \____                           \\")
                print(" |                    |    |   | 0\   |  \____                       |")
                print(" |                    |    |   |^  |  |       \ _                    |")
                print(" |                    |    |   |V / _ |         |                    |")
                print(" |_________           |    |   |██ | \|         |                    |")
                print(" |   /    |___________|    |   |██ | ||         |                    |")
                print(" |  /     |                |   |██ | ||         |                    |")
                print(" | { P    |                |   |   |  |         |                    |")
                print(" | { R    |                |   |   |\/ \     ___|                    |")
                print(" | { E    |________________|   |__/     \   | \ |                    |")
                print(" |<<_S__________________\  |   |M|       \  |  \|__________          |")
                print(" | { S                  |  \   |M|        \ |\  |   DOOR  |          |")
                print(" |_{____________________|   \  |M|         \| \ |    (1)  |          |")
                print(" | { 3                | |    \ |M|          |\ \|         |          |")
                print(" |  \                 | |     \|█\          | \ |  LIGHT  |          |")
                print(" |   \                | |      \ v           \ \|    (2)  |          |")
                print(" |                    | |       \             \ |_________|          |")
                print(" |                               \             \|                    |")
                print(" |                                \             |                    |")
                print(" |                                 \            |                    |")
                print(" |                                  \           |                    |")
                print(" |                                   \          |                    |")
                print(" |                                    \         |                    |")
                print(" |                                     \        |                    |")
                print("  \\____________________________________\_______|____________________/")

            else:
                print("   __________________________________________________________________")
                print("  /                   |    |   |████\____                          \\")
                print(" |                    |    |   |██████|  \____                       |")
                print(" |                    |    |   |██████|       \ _                    |")
                print(" |                    |    |   |██████|         |                    |")
                print(" |_________           |    |   |██████|         |                    |")
                print(" |   /    |___________|    |   |██████|         |                    |")
                print(" |  /     |                |   |██████|         |                    |")
                print(" | { P    |                |   |██████|         |                    |")
                print(" | { R    |                |   |       \     ___|                    |")
                print(" | { E    |________________|   |        \   | \ |                    |")
                print(" |<<_S__________________\  |   |         \  |  \|__________          |")
                print(" | { S                  |  \   |          \ |\  |   DOOR  |          |")
                print(" |_{____________________|   \  |           \| \ |    (1)  |          |")
                print(" | { 3                | |    \ |            |\ \|         |          |")
                print(" |  \                 | |     \|            | \ |  LIGHT  |          |")
                print(" |   \                | |      \             \ \|    (2)  |          |")
                print(" |                    | |       \             \ |_________|          |")
                print(" |                               \             \|                    |")
                print(" |                                \             |                    |")
                print(" |                                 \            |                    |")
                print(" |                                  \           |                    |")
                print(" |                                   \          |                    |")
                print(" |                                    \         |                    |")
                print(" |                                     \        |                    |")
                print("  \\____________________________________\_______|____________________/")
            print("Power left:", power/2,"%")
            usage -= 1
            input("Turn lights off: ")
            office_right()
    else:
        print("ERROR")
        office_right()
    
def light_left():
    global usage, power, Endo_Flashed, Endo_POS
    os.system('cls')
    if not Bonnie_POS == 7:
        usage += 1
        if power - usage <= 0:
            power_drain()
        else:
            power_drain()
            if Bonnie_POS >= 6:
                print("   __________________________________________________________________")
                print("  /                           ____/    |   |    |                    \\")
                print(" |                        ___/|        |   |    |                     |")
                print(" |                   ____/ ^  |        |   |    |                     |")
                print(" |                   |M    M  |        |   |    |                     |")
                print(" |                   |M ___M  |        |   |    |             ________|")
                print(" |                   | 0  0 \ |        |   |    |_____________|   \   |")
                print(" |                   | { X }| |        |   |                  |    \  |")
                print(" |                   |______/_|__      |   |                  |  P }  |")
                print(" |                   |VVVVVVVVV|Y|\_   |                      |  R }  |")
                print(" |                   |NN_____ N|MM| \__|   |__________________|  E }  |")
                print(" |            _______|P/     \P|RR|    |   / /_________________  S > >|")
                print(" |           | DOOR  ||       ||YY|    |  /  |                   S }  |")
                print(" |           |  (1)  ||       ||MM|    | /   |__________________   }  |")
                print(" |           |       ||       ||RR|    |/    | |                 3 }  |")
                print(" |           | LIGHT |V\_____/VV\ \    /     | |                   }  |")
                print(" |           |  (2)  |NNN|  |NNN/_/   /      | |                   /  |")
                print(" |           |_______|PPP|  |PPP|    /       | |                  /   |")
                print(" |                   |VVV|  |VVV|   /                                 |")
                print(" |                   |NNN|  |NNN|  /                                  |")
                print(" |                   |PPP|  |PPP| /                                   |")
                print(" |                   |_V_)  (_V_)/                                    |")
                print(" |                   |          /                                     |")
                print(" |                   |         /                                      |")
                print(" |                   |        /                                       |")
                print("  \\__________________|_______/_______________________________________/")
            elif Endo_POS >= 6:
                Endo_Flashed += 1
                if Endo_Flashed == 3:
                    Endo_Flashed = 0
                    Endo_POS = 0
                print("   __________________________________________________________________")
                print("  /                           ____/████|   |    |                    \\")
                print(" |                        ___/|████████|   |    |                     |")
                print(" |                   ____/ |  |████████|   |    |                     |")
                print(" |                   ||    |  |████████|   |    |                     |")
                print(" |                   || _______████████|   |    |             ________|")
                print(" |                   || |     |████████|   |    |_____________|   \   |")
                print(" |                   |X |0   0|████████|   |                  |    \  |")
                print(" |                   |  |     |        |   |                  |  P }  |")
                print(" |                   |  \_===_/        |   |                  |  R }  |")
                print(" |                   |     |           |   |__________________|  E }  |")
                print(" |            _______|/====|====\---   |   / /_________________  S > >|")
                print(" |           | DOOR  |_____|_____| |   |  /  |                   S }  |")
                print(" |           |  (1)  |_____|_____| |   | /   |__________________   }  |")
                print(" |           |       | /   |       |   |/    | |                 3 }  |")
                print(" |           | LIGHT |/ ___|____    \  /     | |                   }  |")
                print(" |           |  (2)  |  |  ||  |     \       | |                   /  |")
                print(" |           |_______|  |  | \/       \      | |                  /   |")
                print(" |                   |   \/   |     /  []==                           |")
                print(" |                   |    |   |    /   |                              |")
                print(" |                   |    |   }   /                                   |")
                print(" |                   |    {   |  /                                    |")
                print(" |                   |    |   []]                                     |")
                print(" |                   |  [[]    /                                      |")
                print(" |                   |        /                                       |")
                print("  \\__________________|_______/_______________________________________/")
            else:
                print("   __________________________________________________________________")
                print("  /                           ____/████|   |    |                   \\")
                print(" |                        ___/|████████|   |    |                     |")
                print(" |                   ____/ |  |████████|   |    |                     |")
                print(" |                   ||    |  |████████|   |    |                     |")
                print(" |                   ||    *  |████████|   |    |             ________|")
                print(" |                   ||       |████████|   |    |_____________|   \   |")
                print(" |                   |X   _   |████████|   |                  |    \  |")
                print(" |                   |   / | /         |   |                  |  P }  |")
                print(" |                   |  ||/|/          |   |                  |  R }  |")
                print(" |                   |  |/|/           |   |__________________|  E }  |")
                print(" |            _______|  | /            |   / /_________________  S > >|")
                print(" |           | DOOR  |  |/             |  /  |                   S }  |")
                print(" |           |  (1)  |  /              | /   |__________________   }  |")
                print(" |           |       | /               |/    | |                 3 }  |")
                print(" |           | LIGHT |/                /     | |                   }  |")
                print(" |           |  (2)  |                /      | |                   /  |")
                print(" |           |_______|               /       | |                  /   |")
                print(" |                   |              /                                 |")
                print(" |                   |             /                                  |")
                print(" |                   |            /                                   |")
                print(" |                   |           /                                    |")
                print(" |                   |          /                                     |")
                print(" |                   |         /                                      |")
                print(" |                   |        /                                       |")
                print("  \\__________________|_______/_______________________________________/")
            print("Power left:", power/2,"%")
            usage -= 1
            input("Turn lights off: ")
            office_left()
    else:
        print("ERROR")
        office_left()

def office_left():
        global Ldoor, total_actions, usage
        os.system("cls")
        if power - usage <= 0:           
            power_drain()
        elif total_actions + 2 >= 360:
            total_actions = update_clock(1)
        else:
            power_drain()
            total_actions = update_clock(1)
            if Ldoor == 0:
                print("   __________________________________________________________________")
                print("  /                           ____/    |   |    |                   \\")
                print(" |                        ___/         |   |    |                     |")
                print(" |                   ____/             |   |    |                     |")
                print(" |                   |                 |   |    |                     |")
                print(" |                   |                 |   |    |             ________|")
                print(" |                   |                 |   |    |_____________|   \   |")
                print(" |                   |                 |   |                  |    \  |")
                print(" |                   |                 |   |                  |  P }  |")
                print(" |                   |                 |   |                  |  R }  |")
                print(" |                   |                 |   |__________________|  E }  |")
                print(" |            _______|                 |   / /_________________  S > >|")
                print(" |           | DOOR  |                 |  /  |                   S }  |")
                print(" |           |  (1)  |                 | /   |__________________   }  |")
                print(" |           |       |                 |/    | |                 3 }  |")
                print(" |           | LIGHT |                 /     | |                   }  |")
                print(" |           |  (2)  |                /      | |                   /  |")
                print(" |           |_______|               /       | |                  /   |")
                print(" |                   |              /                                 |")
                print(" |                   |             /                                  |")
                print(" |                   |            /                                   |")
                print(" |                   |           /                                    |")
                print(" |                   |          /                                     |")
                print(" |                   |         /                                      |")
                print(" |                   |        /                                       |")
                print("  \\__________________|_______/_______________________________________/")
            else: 
                print("   __________________________________________________________________")
                print("  /                           ____/████|   |    |                   \\")
                print(" |                        ___/█████████|   |    |                     |")
                print(" |                   ____/█████████████|   |    |                     |")
                print(" |                   |████████████=====|   |    |                     |")
                print(" |                   |██████======|[][]|   |    |             ________|")
                print(" |                   |======|[][]]|====|   |    |_____________|   \   |")
                print(" |                   |[][][]|======████|   |                  |    \  |")
                print(" |                   |=======██████████|   |                  |  P }  |")
                print(" |                   |█████████████████|   |                  |  R }  |")
                print(" |                   |█████████████████|   |__________________|  E }  |")
                print(" |            _______|███████████======|   / /_________________  S > >|")
                print(" |           | DOOR  |█████======|[][]]|  /  |                   S }  |")
                print(" |           |  (1)  |=====|[][]]|=====| /   |__________________   }  |")
                print(" |           |       |[][]]|======█████|/    | |                 3 }  |")
                print(" |           | LIGHT |======███████████/     | |                   }  |")
                print(" |           |  (2)  |████████████████/      | |                   /  |")
                print(" |           |_______|███████████████/       | |                  /   |")
                print(" |                   |██████████████/                                 |")
                print(" |                   |█████████████/                                  |")
                print(" |                   |████████████/                                   |")
                print(" |                   |███████████/                                    |")
                print(" |                   |██████████/                                     |")
                print(" |                   |█████████/                                      |")
                print(" |                   |████████/                                       |")
                print("  \\__________________|████████/_______________________________________/")
            print("Power left:", power/2,"%")
            action = get_int_input("Select Action: ", [1, 2, 3])
            if action == 1:
                if total_actions + 2 >= 360:
                    total_actions = update_clock(2)
                else:
                    total_actions = update_clock(2)
                    if Bonnie_POS == 7:
                        input("ERROR")
                        office_left()
                    elif Ldoor == 0:
                            usage += 2
                            Ldoor = 1
                            office_left()
                    else: 
                        usage -= 2
                        Ldoor = 0
                        office_left()
            elif action == 2:
                if Ldoor == 1:
                    input("ERROR")
                    office_left()
                else:
                    light_left()
            elif action == 3:
                move_opportunity()    
                office_main()

def office_right():
        move_opportunity()
        global Rdoor, total_actions, usage
        os.system("cls")
        if power - usage <= 0:           
            power_drain()
        elif total_actions + 1 >= 360:
            total_actions = update_clock(1)
        else:
            power_drain()
            total_actions = update_clock(1)
            if Rdoor == 0: 
                print("   __________________________________________________________________")
                print("  /                   |    |   |    \____                           \\")
                print(" |                    |    |   |         \____                       |")
                print(" |                    |    |   |              \ _                    |")
                print(" |                    |    |   |                |                    |")
                print(" |_________           |    |   |                |                    |")
                print(" |   /    |___________|    |   |                |                    |")
                print(" |  /     |                |   |                |                    |")
                print(" | { P    |                |   |                |                    |")
                print(" | { R    |                |   |                |                    |")
                print(" | { E    |________________|   |                |                    |")
                print(" |<<_S__________________\  |   |                |__________          |")
                print(" | { S                  |  \   |                |   DOOR  |          |")
                print(" |_{____________________|   \  |                |    (1)  |          |")
                print(" | { 3                | |    \ |                |         |          |")
                print(" |  \                 | |     \|                |  LIGHT  |          |")
                print(" |   \                | |      \                |    (2)  |          |")
                print(" |                    | |       \               |_________|          |")
                print(" |                               \              |                    |")
                print(" |                                \             |                    |")
                print(" |                                 \            |                    |")
                print(" |                                  \           |                    |")
                print(" |                                   \          |                    |")
                print(" |                                    \         |                    |")
                print(" |                                     \        |                    |")
                print("  \\____________________________________\_______|____________________/")
            else:
                print("   __________________________________________________________________")
                print("  /                   |    |   |████\____                           \\")
                print(" |                    |    |   |█████████\____                       |")
                print(" |                    |    |   |██████████████\ _                    |")
                print(" |                    |    |   |======██████████|                    |")
                print(" |_________           |    |   |[][]]|=====█████|                    |")
                print(" |   /    |___________|    |   |=====|[][]|=====|                    |")
                print(" |  /     |                |   |█████=====|[][]]|                    |")
                print(" | { P    |                |   |██████████======|                    |")
                print(" | { R    |                |   |████████████████|                    |")
                print(" | { E    |________________|   |████████████████|                    |")
                print(" |<<_S__________________\  |   |████████████████|__________          |")
                print(" | { S                  |  \   |======██████████|   DOOR  |          |")
                print(" |_{____________________|   \  |[][]]|=======███|    (1)  |          |")
                print(" | { 3                | |    \ |=====|[][][]|===|         |          |")
                print(" |  \                 | |     \|█████=======|[]]|  LIGHT  |          |")
                print(" |   \                | |      \████████████====|    (2)  |          |")
                print(" |                    | |       \███████████████|_________|          |")
                print(" |                               \██████████████|                    |")
                print(" |                                \█████████████|                    |")
                print(" |                                 \████████████|                    |")
                print(" |                                  \███████████|                    |")
                print(" |                                   \██████████|                    |")
                print(" |                                    \█████████|                    |")
                print(" |                                     \████████|                    |")
                print("  \\_____________________________________\███████|____________________/")
            print("Power left:", power/2,"%")
            action = get_int_input("Select Action: ", [1, 2, 3])
            if action == 1:
                if total_actions >= 360:
                    total_actions = update_clock(2)
                else:
                    total_actions = update_clock(2)
                    if Freddy_POS == 7 or Chica_POS == 7:
                        input("ERROR")
                        office_right()
                    elif Rdoor == 0:
                        Rdoor = 1
                        usage += 2
                        office_right()
                    else: 
                        Rdoor = 0
                        usage -= 2
                        office_right()
            elif action == 2:
                if Rdoor == 1:
                    input("ERROR")
                    office_right()
                else:
                    light_right()
            elif action == 3:
                move_opportunity()    
                office_main()

def office_main():
    os.system("cls")
    global total_actions
    move_opportunity()
    if power - usage <= 0:
        power_drain() 
    elif total_actions + 2 >= 360:
        total_actions = update_clock(2)
    else:
        total_actions = update_clock(2)
        power_drain()
        clock = update_ingame_clock()
        print("   __________________________________________________________________")
        print("  /                                                                 \\")
        print(" |                                                                   |")
        print(" |                                                                   |")
        print(" |                                                                   |")
        print(" |                                                                   |")
        print(" |    /        ____________________________________             \    |")
        print(" |   /         |  ______________________________  |              \   |")
        print(f" |   ( P       | |           {clock}           | |            P )   |")
        print(" |   { R       | |                              | |            R }   |")
        print(" |   { E       | |          open cams           | |            E }   |")
        print(" | <<  S       | |             (1)              | |            S  > >|")
        print(" |   { S       | |                              | |            S }   |")
        print(" |   {         | |                              | |              }   |")
        print(" |   { 2       | |                              | |            3 }   |")
        print(" |   \          | |____________________________| |               /   |")
        print(" |    \         |______________(O)_______________|              /    |")
        print(" |           /                 | |                  \                |")
        print(" |          /                                        \               |")
        print(" |_________/                                          \______________|")
        print(" |        /____________________________________________\             |")
        print(" |        |                                            |             |")
        print(" |        |                                            |             |")
        print("  \\_________________________________________________________________/")
        print("Power left:", power/2,"%")
        action = get_int_input("Select Action: ", [1, 2, 3])
        if action == 1:
            cams()
        elif action == 2:
            office_left()
        elif action == 3:
            office_right()
        time.sleep(2)

def night_start():  
    global usage, power, Bonnie_AI, Chica_AI, Freddy_AI, Foxy_AI, Endo_AI, Foxy_Stage
    Foxy_Stage = 0
    usage = 0
    power = 200
    if night == 1:
        Bonnie_AI = 3
        Chica_AI = 2
        Freddy_AI = 0
        Foxy_AI = 0
        Endo_AI = 1
    elif night == 2:
        Bonnie_AI = 3
        Chica_AI = 3
        Freddy_AI = 0
        Foxy_AI = 1
        Endo_AI = 3
    elif night == 3:
        Bonnie_AI = 1
        Chica_AI = 6
        Freddy_AI = 1
        Foxy_AI = 2
        Endo_AI = 5
    elif night == 4:
        Bonnie_AI = 3
        Chica_AI = 6
        Freddy_AI = 3
        Foxy_AI = 7
        Endo_AI = 7
    elif night >= 5:
        Bonnie_AI = 7
        Chica_AI = 9
        Freddy_AI = 5
        Foxy_AI = 7
        Endo_AI = 9
    elif night >= 6:
        Bonnie_AI = 10
        Chica_AI = 12
        Freddy_AI = 6
        Foxy_AI = 6
        Endo_AI = 7 

    os.system("cls")
    print(f"| |=================================================================| |")
    print(f"| |=================================================================| |")
    print(f"| |                                                                 | |")
    print(f"| |                                                                 | |")
    print(f"| |                                                                 | |")
    print(f"| |                                                                 | |")
    print(f"| |                                                                 | |")
    print(f"| |                                                                 | |")
    print(f"| |                           NIGHT {night}                               | |")
    print(f"| |                                                                 | |")
    print(f"| |                                                                 | |")
    print(f"| |                                                                 | |")
    print(f"| |                                                                 | |")
    print(f"| |                                                                 | |")
    print(f"| |                                                                 | |")
    print(f"| |                                                                 | |")
    print(f"| |=================================================================| |")
    print(f"| |=================================================================| |")
    input(": ")
    office_main()
    
def save_game():
    with open("savegame.txt", "w") as f:
        f.write(str(night))

def load_save():
    try:
        with open("savegame.txt", "r") as f:
            return int(f.read())
    except FileNotFoundError:
        return 1

def pasek_ladowania(czas):
    for i in range(czas+1):
        procenty = int((i / czas) * 100)
        pasek = '#' * (procenty // 2) + '-' * (50 - (procenty // 2))
        print(f"\r[{pasek}] {procenty}%", end='')
        time.sleep(0.5)

def menu():
    global power
    global total_actions
    global night
    global usage
    total_actions = 0
    usage = 0
    power = 200    
    t = True
    while t:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("| |=================================================================| |")
        print("| |=================================================================| |")
        print("| |                                                                 | |")
        print("| |Five Nights at Freddy's - Python Edition                         | |")
        print("| |                                                                 | |")
        print("| |  1. New Game                                                    | |")
        if night > 1:
            print(f"| |  2. Continue from Night {night}                                       | |")
            print("| |  3. Custom Night                                                | |")
            print("| |  4. Clear Save                                                  | |")
            print("| |  5. Exit Game                                                   | |")
            print("| |                                                                 | |")
            print("| |                                                                 | |")
            print("| |=================================================================| |")
            print("| |=================================================================| |")
            wybor = get_int_input("Choose option (1-5): ", [1, 2, 3, 4, 5])
            t = False
        else:
            print("| |  2. Custom Night                                                 | |")
            print("| |  3. Exit Game                                                    | |")
            print("| |                                                                  | |")
            print("| |                                                                  | |")
            print("| |                                                                  | |")
            print("| |                                                                  | |")
            print("| |=================================================================| |")
            print("| |=================================================================| |")
            wybor = get_int_input("Choose option (1-3): ", [1, 2, 3])
            t = False
        if wybor == 1:
            clear_save()
            total_actions = 0
            night = 1
            night_start()
            time.sleep(1)
        if night > 1:
            if wybor == 2:
                total_actions = 0
                night_start()
                time.sleep(1)
            elif wybor == 3:
                print("Custom Night selected.")
                time.sleep(1)
            elif wybor == 4:
                pasek_ladowania(5)
                print('')
                input("Save cleared.")
                clear_save()
                menu()
            elif wybor == 5:
                os.system("cls")
                print("Exiting...")
                time.sleep(0.5)
                pasek_ladowania(5)
                os.system("cls")
                exit()
        else:
            if wybor == 2:
                print("Custom Night selected.")
                time.sleep(1)
            elif wybor == 3:
                os.system("cls") 
                print("Exiting...")
                time.sleep(1)
                pasek_ladowania(5)
                exit()
              
#Główna pętla
os.system("cls") 
#clear_save()
night = load_save()
pasek_ladowania(10)
print("")
input("Ready!")
os.system("cls")
menu()