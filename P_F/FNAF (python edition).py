#things to do 
#-add chinese golden freddy 
#-add sound
#-balance changes
#-options?
#-fix animatronic AI
#+idea Freedy would be a hybrid of foxy and Bonnie also when hes at the door he cant go back you can just lower his
# agro with flashing lights and stun him with closing door (also you dont need to worry about chica anymore cause she
# is to afraid of him to be on same position as him)
#-maybe if im not doing smt else at the moment change cameras from map to ASCII art

#imports
import time
import os
import random
#import pygame

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
gameON = 0  
CustomNight = 0
Deez = 0
score_to_get = 0


#Functions
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

def Bonnie_Move():
    global Bonnie_POS, Ldoor
    a = 0
    if cams_on == 0:
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
        for i in range(random.randint(1,3)):
            os.system("cls")
            os.system("color 0C")
            print("   __________________________________________________________________")
            print("  /                                                                 \\")
            print(" |                                                                   |")
            print(" |                                                                   |")
            print(" |                    __                  __                         |")
            print(" |                   /  |                |  \                        |")
            print(" |                   \| \                / |/                        |")
            print(" |                    \| \              / |/                         |")
            print(" |                     \| \            / |/                          |")
            print(" |                      \| \          / |/                           |")
            print(" |                       || |________| ||                            |")
            print(" |                      /                \                           |")
            print(" |                     /                  \                          |")
            print(" |                    /     0        0     \                         |")
            print(" |                   |    ______OO______    |                        |")
            print(" |                    \  /              \  /                         |")
            print(" |               ______\/       ||       \/______                    |")
            print(" |            __/       \_______||_______/       \                   |")
            print(" |           /          /_^_          _^_\        \__                |")
            print(" |          /             \_\_^_^^_^_/_/             \               |")
            print(" |         |          /   ________________   \        \              |")
            print(" |        /          /   /                \   \        |             |")
            print(" |       /          /|  |                  |  |\        \            |")
            print("  \\_____|_________/_|__|__________________|__|_\_________\__________/")      
            time.sleep(0.3)  
            os.system("color 0A")
            time.sleep(0.3)  
        game_over_screen()
                     
def Chica_Move():
    global Chica_POS, Rdoor,Chica_Waiting
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
            if Chica_Waiting < 1:
                if Rdoor == 1:
                    a = random.randint(0,3)
                    if a == 1:
                        Chica_POS = 6
                    else:
                        Chica_POS = a
                else:
                    Chica_POS = 7
    if Chica_POS == 6 and Rdoor == 1:
        if random.randint(0,2) == 1:
            Chica_POS = random.randint(0,2)
    if Chica_POS == 7 and cams_on == 1:
        for i in range(random.randint(1,3)):
            os.system("cls")
            os.system("color 0C")
            print("   __________________________________________________________________")
            print("  /                                                                 \\")
            print(" |                                                                   |")
            print(" |                                                                   |")
            print(" |                                                                   |")
            print(" |                                                                   |")
            print(" |                                                                   |")
            print(" |                                                                   |")
            print(" |                                                                   |")
            print(" |                            __\__/__                               |")
            print(" |                         __/        \__                            |")
            print(" |                        /  ___   ___  \                           |")
            print(" |                       /    0 ___ 0     \                          |")
            print(" |                       |     /___\      |                          |")
            print(" |                       |     |___|      |                          |")
            print(" |                  ____ _\    \___/     /_ ____                     |")
            print(" |                 /    /  \____________/  \    \                    |")
            print(" |                /    /|  \            /  |\    \                   |")
            print(" |               /    / |   \__________/   | \    \                  |")
            print(" |               |   |  |                  |  |    |                 |")
            print(" |               |   |  |       LET`S      |  |    |                 |")
            print(" |               |   |  |        EAT!      |  |    |                 |")
            print(" |               |   |  \ _________________/  |    |                 |")
            print("  \\_____________\___|________________________|____/________________/")      
            time.sleep(0.3)  
            os.system("color 0A")
            time.sleep(0.3)  
        game_over_screen()

def Endo_Move():
    global Endo_POS, Endo_Flashed, Endo_waiting
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
    if  Endo_POS == 7 and cams_on == 1 and not Ldoor == 1 and Endo_waiting <= 0:
        for i in range(random.randint(1,3)):
            os.system("cls")
            os.system("color 0C")
            print("   __________________________________________________________________")
            print("  /                                                                 \\")
            print(" |                                                                   |")
            print(" |                                                                   |")
            print(" |                                                                   |")
            print(" |                       ___m_m_________________                     |")
            print(" |                       |                     |                     |")
            print(" |                       |                     |                     |")
            print(" |                       |  (0)           (0)  |                     |")
            print(" |                       |                     |                     |")
            print(" |                       |\     ||     ||     /|                     |")
            print(" |                       | \_________________/ |                     |")
            print(" |                         |_________________|                       |")
            print(" |                          v|  v v v v v  |v                        |")
            print(" |                         _^|^_^_^_^_^_^_^|^_                       |")
            print(" |                         |_________________|                       |")
            print(" |                           / /| |   | |\ \                         |")
            print(" |                          / / | |   | | \ \                        |")
            print(" |          ___ ___________/_/__|_|___|_|__\_\___________ ___        |")
            print(" |         (___)||________________|___|________________||(___)       |")
            print(" |          ||| ||================| | |================|| |||        |")
            print(" |         // / ||________________|   |________________||  \\\\\       |")
            print(" |        // /  ||================|   |================||   \\\\\      |")
            print("  \\______//_/___||________________|_|_|________________||____\\\\\____/")      
            time.sleep(0.3)  
            os.system("color 0A")
            time.sleep(0.3) 
        game_over_screen()

def Foxy_Move():
    global Foxy_Stage, Foxy_Energy, cams_on, Foxy_INCOMING,Deez
    if Foxy_Stage == 0:
        Deez = 0
    if cams_on == 0:
        Foxy_Energy += Foxy_AI
        if Foxy_Energy >= 80:
            Foxy_Stage += 1
            # Cap stage so Foxy doesn't skip the "stage 4 incoming" logic.
            if Foxy_Stage > 4:
                Foxy_Stage = 4
            Foxy_Energy = 0
    if Foxy_Stage >= 4:
        if Deez == 0:
            print("FOXY RUNNING PRESET")
            Foxy_INCOMING = random.randint(3,6)
            Deez = 1
        if Foxy_INCOMING < 1:
            if Ldoor == 1:
                Foxy_Energy = random.randint(0,20)
                Foxy_Stage = random.randint(0,1)
            else:
                os.system("cls")
                os.system("color 0C")
                print("   __________________________________________________________________")
                print("  /                                                                 \\")
                print(" |                                                                   |")
                print(" |                                                                   |")
                print(" |                                                                   |")
                print(" |                                                                   |")
                print(" |                        __             __                          |")
                print(" |         ____          /()\           /()\                         |")
                print(" |         \   \         \() \         / ()/                         |")
                print(" |          |  /          \__/ __\_/__ \__/             | |          |")
                print(" |          |_             __\/       \/__              |_||         |")
                print(" |         /  \           /  (O)          \           |/  \|         |")
                print(" |         \   \          |---0         0  |          /   /          |")
                print(" |          \   \        /      __OO__      \        /   /           |")
                print(" |           \  _\__ ___/     _/      \_     \___ __/   /            |")
                print(" |            \/    /________/____||____\________\     /             |")
                print(" |             \____________/ /v v v v v\ \___________/              |")
                print(" |                       __/ \^        ^/   \                        |")
                print(" |                    __/    /\^      ^/\    \__                     |")
                print(" |                   / /    /  \^    ^/  \    \ \                    |")
                print(" |                  / /____/    \_^^_/    \____\ \                   |")
                print(" |                 /O  O/                    \O  O\                  |")
                print(" |                /_/_//                      \i_\_\                 |")
                print("  \\_________________________________________________________________/")      
                time.sleep(0.3)  
                os.system("color 0A")
                os.system('cls')
                print("   __________________________________________________________________")
                print("  /                                                                 \\")
                print(" |                                                                   |")
                print(" |                                                                   |")
                print(" |                                                                   |")
                print(" |                        __             __                          |")
                print(" |         ____          /()\           /()\                         |")
                print(" |         \   \         \() \         / ()/                         |")
                print(" |          |  /          \__/ __\_/__ \__/             | |          |")
                print(" |          |_             __\/       \/__              |_||         |")
                print(" |         /  \           /  (O)          \           |/  \|         |")
                print(" |         \   \          |---0         0  |          /   /          |")
                print(" |          \   \        /      __OO__      \        /   /           |")
                print(" |           \  _\__ ___/     _/      \_     \___ __/   /            |")
                print(" |            \/    /________/____||____\________\     /             |")
                print(" |             \____________/ /v v v v v\ \___________/              |")
                print(" |                       __/ \^        ^/   \                        |")
                print(" |                    __/    /\^      ^/\    \__                     |")
                print(" |                   / /    /  \^    ^/  \    \ \                    |")
                print(" |                  / /____/    \_^^_/    \____\ \                   |")
                print(" |                 /O  O/                    \O  O\                  |")
                print(" |                /_/_//                      \i_\_\                 |")
                print(" |                                                                   |")
                print("  \\_________________________________________________________________/")   
                time.sleep(0.3)
                os.system("color 0C")                
                os.system("cls")
                print("   __________________________________________________________________")
                print("  /                                                                 \\")
                print(" |                                                                   |")
                print(" |                                                                   |")
                print(" |                        __             __                          |")
                print(" |         ____          /()\           /()\                         |")
                print(" |         \   \         \() \         / ()/                         |")
                print(" |          |  /          \__/ __\_/__ \__/             | |          |")
                print(" |          |_             __\/       \/__              |_||         |")
                print(" |         /  \           /  (O)          \           |/  \|         |")
                print(" |         \   \          |---0         0  |          /   /          |")
                print(" |          \   \        /      __OO__      \        /   /           |")
                print(" |           \  _\__ ___/     _/      \_     \___ __/   /            |")
                print(" |            \/    /________/____||____\________\     /             |")
                print(" |             \____________/ /v v v v v\ \___________/              |")
                print(" |                       __/ \^        ^/   \                        |")
                print(" |                    __/    /\^      ^/\    \__                     |")
                print(" |                   / /    /  \^    ^/  \    \ \                    |")
                print(" |                  / /____/    \_^^_/    \____\ \                   |")
                print(" |                 /O  O/                    \O  O\                  |")
                print(" |                /_/_//                      \i_\_\                 |")
                print(" |                                                                   |")
                print(" |                                                                   |")                    
                print("  \\_________________________________________________________________/")   
                os.system("color 0A")
                time.sleep(0.3)
                os.system('cls')
                print("   __________________________________________________________________")
                print("  /                                                                 \\")
                print(" |                                                                   |")
                print(" |                                                                   |")
                print(" |                        __             __                          |")
                print(" |         ____          /()\           /()\                         |")
                print(" |         \   \         \() \         / ()/                         |")
                print(" |          |  /          \__/ __\_/__ \__/             | |          |")
                print(" |          |_             __\/       \/__              |_||         |")
                print(" |         /  \           /  (O)          \           |/  \|         |")
                print(" |         \   \          |---0         0  |          /   /          |")
                print(" |          \   \        /      __OO__      \        /   /           |")
                print(" |           \  _\__ ___/     _/      \_     \___ __/   /            |")
                print(" |            \/    /________/____||____\________\     /             |")
                print(" |             \____________/ /v v v v v\ \___________/              |")
                print(" |                       __/ \^        ^/   \                        |")
                print(" |                    __/    /\^      ^/\    \__                     |")
                print(" |                   / /    /  \^    ^/  \    \ \                    |")
                print(" |                  / /____/    \_^^_/    \____\ \                   |")
                print(" |                 /O  O/                    \O  O\                  |")
                print(" |                /_/_//                      \i_\_\                 |")
                print(" |                                                                   |")
                print(" |                                                                   |")
                print(" |                                                                   |")                    
                print("  \\_________________________________________________________________/")                      
                game_over_screen()

                
    else:
        Foxy_Energy -= 10
        if Foxy_Energy < 0:
            Foxy_Energy = 0

def Freddy_Move():
    a = None
    global Freddy_POS, Rdoor
    if not cams_on == 1:
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
        for i in range(random.randint(1,3)):
            os.system("cls")
            os.system("COLOR 0C")
            print("   ________________________________________________________________")
            print("  /                                                                \\")
            print(" |      ITS ME                                          ItS Me       |")
            print(" |                                      Its ME                       |")
            print(" |                 its me                                            |")
            print(" |                                                ITS ME             |")
            print(" |      ITs mE                  ______                    its me     |")
            print(" |                              |    |                               |")
            print(" |                              |    |                               |")
            print(" |                     _____  __|____|__  _____                      |")
            print(" |                     | (_|_/__________\_|_) |                      |")
            print(" |                      \/                  \/                       |")
            print(" |                      /    0          0    \                       |")
            print(" |                      |     _____O_____     |                      |")
            print(" |                     /     /           \     \                     |")
            print(" |                     \____/______|______\____/                     |")
            print(" |                      __|                 |__                      |")
            print(" |               ______ \ \^_^_^_^_^_^_^_^_^/ /_ ______              |")
            print(" |              /      | \___________________/  \      \             |")
            print(" |             |\       \     | __/O\ __ |       |    __\            |")
            print(" |            /  |_____ |    _|/        \|____   |___/   |           |")
            print(" |           /         \/ \  \                \   \       \          |")
            print(" |          /          /   \  \                \   \       \         |")
            print("  \\_______/__________/_____|__|________________|___|_______\________/")
            time.sleep(0.3)  
            os.system("color 0A")            
            time.sleep(0.3)  
        game_over_screen() 

def power_drain( ):
        global power
        global usage
        power -= usage
        os.system("cls")
        if power <= 0:
            power = 0
            os.system("COLOR 0F")
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
                        os.system("color 0F")
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
                        os.system("color 0E")
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
                    os.system("COLOR 0A")
                    os.system("cls")
                    for i in range(random.randint(1,3)):
                        os.system("cls")
                        os.system("COLOR 0C")
                        print("   __________________________________________________________________")
                        print("  /                                                                 \\")
                        print(" |      ITS ME                                           ItS Me      |")
                        print(" |                                      Its ME                       |")
                        print(" |                 its me                                            |")
                        print(" |                                                ITS ME             |")
                        print(" |      ITs mE                  ______                     its me    |")
                        print(" |                              |    |                               |")
                        print(" |                              |    |                               |")
                        print(" |                     _____  __|____|__  _____                      |")
                        print(" |                     | (_|_/__________\_|_) |                      |")
                        print(" |                      \/                  \/                       |")
                        print(" |                      /    0          0    \                       |")
                        print(" |                      |     _____O_____     |                      |")
                        print(" |                     /     /           \     \                     |")
                        print(" |                     \____/______|______\____/                     |")
                        print(" |                      __|                 |__                      |")
                        print(" |               ______ \ \^_^_^_^_^_^_^_^_^/ /_ ______              |")
                        print(" |              /      | \___________________/  \      \             |")
                        print(" |             |\       \     | __/O\ __ |       |    __\            |")
                        print(" |            /  |_____ |    _|/        \|____   |___/   |           |")
                        print(" |           /         \/ \  \                \   \       \          |")
                        print(" |          /          /   \  \                \   \       \         |")
                        print("  \\_______/__________/_____|__|________________|___|_______\________/")
                        time.sleep(0.3)  
                        os.system("color 0A")            
                        time.sleep(0.3) 
                    game_over_screen()
                    break
                else:
                    pass

def update_clock(actions):
    global total_actions
    total_actions += actions
    #print(f"Total actions this night: {total_actions}")
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

def check_for_movement():
    global usage, power, total_actions,cams_on
    if power - usage <= 0:
        power_drain()
    elif total_actions + 2 >= 360 or gameON == 0:
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
            usage -= 1
            cams_on = 0
            move_opportunity()
            office_main()    

def cams():
        move_opportunity()
        os.system('cls')
        global usage,power,total_actions,cams_on
        cams_on = 1
        usage += 1
        if power - usage <= 0:
            power_drain() 
        elif total_actions + 4 >= 360 or gameON == 0:
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
        elif total_actions + 2 >= 360 or gameON == 0:
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
        elif total_actions + 1 >= 360 or gameON == 0:
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
    global total_actions, gameON
    move_opportunity()
    if power - usage <= 0:
        power_drain() 
    elif total_actions + 2 >= 360 or gameON == 0:
        total_actions = update_clock(2)
    else:
        if random.randint(1,1987) == 1:
            total_actions = update_clock(2)
            power_drain()
            clock = update_ingame_clock()
            
            os.system("color 0E")
            print("   __________________________________________________________________")
            print("  /                                                                 \\")
            print(" |     ITS ME             ITS ME                             ITS ME  |")
            print(" |                                                ITS ME             |")
            print(" |              ITS ME        ________                               |")
            print(" |                            |      |                               |")
            print(" |    /     ITS ME            |      |              ITS ME      \    |")
            print(" |   /            ___         |      |          ___              \   |")
            print(" |   ( P         | ()|     ___|______|___      |() |           P )   |")
            print(" |   { R         |__ \_____|____________|_____/ __|            R }   |")
            print(" |   { E            \/                         \/              E }   |")
            print(" | <<  S             |                         |               S  > >|")
            print(" |   { S             |     0             0     |               S }   |")
            print(" |   {               |                         |                 }   |")
            print(" |   { 2             |     ______OO_______     |               3 }   |")
            print(" |   \               |    |      ||       |    |                 /   |")
            print(" |    \               \   \______/\_______/   /                 /    |")
            print(" |                    |___/███████████████\___|                      |")
            print(" |                     \ \█████████████████/ /                       |")
            print(" |                      | |███████████████| |                        |")
            print(" |                       \_________________/                         |")
            print(" |                                                                   |")
            print(" |                                                                   |")
            print("  \\_________________________________________________________________/")
            for i in range(random.randint(3,5)):
                os.system("color 6F")
                time.sleep(0.3)
                os.system("color 0E")
                time.sleep(0.3)
            os.system("color 0E")
            fate = random.randint(1,4)
            if fate == 1:
                os.system("cls")
                print("ERROR" * 1987)
                time.sleep(1)
                exit()
            elif fate == 2:
                office_main()
            elif fate == 3:
                gameON = 0
                game_over_screen()
            
        else:
            if gameON == 1:
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
                print(" |   ( P       | |                              | |            P )   |")
                print(f" |   | R       | |           {clock}           | |            R |   |")
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
                print(" |                                                                   |")
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
    global usage, power, Bonnie_AI, Chica_AI, Freddy_AI, Foxy_AI, Endo_AI, Foxy_Stage, Foxy_Energy, Foxy_INCOMING, Deez, gameON, night
    global Bonnie_POS, Chica_POS, Freddy_POS, Endo_POS
    Bonnie_POS = 0
    Chica_POS = 0
    Freddy_POS = 0
    Endo_POS = 0
    Foxy_Stage = 0
    Foxy_Energy = 0
    Foxy_INCOMING = 0
    Deez = 0
    usage = 0
    power = 200
    gameON = 1
    if not CustomNight == 1:
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
            Bonnie_AI =  1
            Chica_AI =  6
            Freddy_AI = 1
            Foxy_AI = 10
            Endo_AI = 5
        elif night == 4:
            Bonnie_AI = 3
            Chica_AI = 6
            Freddy_AI = 3
            Foxy_AI = 7
            Endo_AI = 7
        elif night == 5:
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
    if not CustomNight == 1:
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
    else:
        os.system("cls")
        print(f"| |=================================================================| |")
        print(f"| |=================================================================| |")
        print(f"| |                                                                 | |")
        print(f"| |                                                                 | |")
        print(f"| |                                                                 | |")
        print(f"| |                                                                 | |")
        print(f"| |                                                                 | |")
        print(f"| |                                                                 | |")
        print(f"| |                          CUSTOM NIGHT                           | |")
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

def end_night():
    global night, gameON, usage, power, Ldoor, Rdoor, Bonnie_POS, Chica_POS, Freddy_POS, Endo_POS,score_to_get,highscore
    gameON = 0
    usage = 0
    power = 200
    Ldoor = 0
    Rdoor = 0
    Bonnie_POS = 0
    Chica_POS = 0
    Freddy_POS = 0
    Endo_POS = 0
    os.system("cls")
    print("| |=================================================================| |")
    print("| |=================================================================| |")
    print("| |                                                                 | |")
    print("| |                              _______                            | |")
    print("| |                /            |       |   |\     /|               | |")
    print("| |               /             |       |   | \   / |               | |")
    print("| |              /____          |_______|   |  \_/  |               | |")
    print("| |             /     \         |       |   |       |               | |")
    print("| |            |      |         |       |   |       |               | |")
    print("| |             \____/          |       |   |       |               | |")
    print("| |                                                                 | |")
    print("| |                                                                 | |")
    print("| |                                                                 | |")
    print("| |                                                                 | |")
    print("| |                                                                 | |")
    print("| |                                                                 | |")
    print("| |=================================================================| |")
    print("| |=================================================================| |")  
    for i in range(random.randint(2,5)):
        time.sleep(0.5)
        os.system("color 0F")
        time.sleep(0.5) 
        os.system("color 0A")
    action = get_int_input("1. Continue to next night 2. Main Menu ", [1, 2])
    if action == 1:
        if not CustomNight == 1:
            night += 1
            save_game()    
        else:
            if highscore < score_to_get:
                highscore = score_to_get
                score_to_get = 0
                save_game()
        night_start()  
    elif action == 2:
        if not CustomNight == 1:    
            night += 1
            save_game()
        else:
            if highscore < score_to_get:
                highscore = score_to_get
                score_to_get = 0
                save_game()
        menu()

def save_game():
    with open("savegame.txt", "w") as f:
        f.write(str(night),)
    with open("highscore.txt", "w") as f:
        f.write(str(highscore),)

def load_save():
    try:
        with open("savegame.txt", "r") as f:
            return int(f.read())
    except FileNotFoundError:
        return 1

def load_score():
    try:
        with open("highscore.txt", "r") as f:
            return int(f.read())  
    except FileNotFoundError:
        return 0

def clear_save():
    global night, highscore
    if os.path.exists("savegame.txt"):
        os.remove("savegame.txt")
        night = 0

def Loading(duration):
    # draw a loading bar centred inside a 70-column frame
    total_width = 70
    inner_width = total_width - 2  # account for the bars on each side
    # border characters can be changed to taste
    top_bottom = "+" + "-" * inner_width + "+"
    side = "|"

    for i in range(duration + 1):
        procenty = int((i / duration) * 100)
        # build the bar itself (50 characters long as before)
        pasek = '#' * (procenty // 2) + '-' * (50 - (procenty // 2))
        content = f"[{pasek}] {procenty}%"
        # calculate loading dots animation (cycles through 0-3 dots)
        dots = "." * (i % 4)
        loading = f"Loading{dots}"
        # centre the content within the available inner width
        centered = content.center(inner_width)
        loading_centered = loading.center(inner_width)

        # clear the screen so the frame redraws neatly each step
        os.system('cls')
        print(top_bottom)
        # print animated loading text above bar
        print(side + loading_centered + side)
        print(side + centered + side)
        print(top_bottom)
        time.sleep(0.5)

def game_over_screen():
    global gameON
    gameON = 0
    os.system("cls")
    os.system("color 0C")
    print("   __________________________________________________________________")
    print("  /                                    ______                        \\")
    print(" |                                    |######|                       |")
    print(" |        GAME                  ___   |######|  ___                  |")
    print(" |        OVER                 |   |__|######|_|   |                 |")
    print(" |                             | /              \ /                  |")
    print(" |                              |    ____   ____ |                   |")
    print(" |                              /    |O_|   |__|  \                  |")
    print(" |                             /_   |     O   | | /                  |")
    print(" |                               \| \_____|___O_/|                   |")
    print(" |                      _____  ___\|_^_^_^_^_^_^/  _____             |")
    print(" |                     /     \/   |\___________/ \/     \            |")
    print(" |                    /  []}  /   |/ ______\|     \  []} \           |")
    print(" |                    \  {   /   ___/      \___    | {   |           |")
    print(" |                    I\____/   /              \   |_____|           |")
    print(" |                   /IIIII|    |  []          |   |IIIIII           |")
    print(" |                   |    ||    |   ]          |   ||    |_____      |")
    print(" |                   |    ||    |              |   ||    |     \     |")
    print(" |                   |____||    |              |   ||    |      \    |")
    print(" |                   IIIIII|    |              |   ||    |       \   |")
    print(" |                   |     \    |              |   |IIIIII__      \  |")
    print(" |                  / / / /|/___|___         __|___|\ \ \ \_|      \ |")
    print(" |                 /_/_/_/ |  _____  \======/______\_\_\_\_\        \|")
    print(" |                 /       |_/     \_|     \/      |\                |")
    print(" |                /        |   [}    |      \  ]]}   \               |")
    print("  \\_____________/_________|__{]_____|_______\{]______\______________/")
    input()
    os.system("cls")
    print(f"| |=================================================================| |")
    print(f"| |=================================================================| |")
    print(f"| |                                                                 | |")
    print(f"| |                           GAME OVER                             | |")
    print(f"| |                                                                 | |")
    print(f"| |                                                                 | |")
    print(f"| |                                                                 | |")
    print(f"| |                                                                 | |")
    print(f"| |                                                                 | |")
    print(f"| |                    TIP FROM FAZBEAR MANUAL:                     | |")   
    tip = random.randint(1, 5)
    if tip == 1:
        print(f"| |      Bonnie is faster than Chica so you should proriterize      | |")
        print(f"| |                  dealing with him over her.                     | |")    
    elif tip == 2:
        print(f"| |      When Chica is in Kitchen you can hear her roumbling        | |")
        print(f"| |                   around with pans and pots.                    | |")    
    elif tip == 3:
        print(f"| |  Endo does not care about direct conections as he uses vents    | |")
        print(f"| |    to roam around. That makes him quait dangerous be aware!     | |")    
    elif tip == 4:
        print(f"| | Foxy cant progress through his phases when you looking on cams. | |")
        print(f"| |           Check on him regulary to keep him at bay.             | |")    
    elif tip == 5: 
        print(f"| |           If Freddy is online you are truly f****d.             | |")
        print(f"| |                                                                 | |")

    print(f"| |                                                                 | |")
    print(f"| |                                                                 | |")
    print(f"| |                                                                 | |")
    print(f"| |                                                                 | |")
    print(f"| |                                                                 | |")
    print(f"| |                                                                 | |")
    print(f"| |=================================================================| |")
    print(f"| |=================================================================| |")
    input("Press Enter to continue...")
    os.system("color 0A")
    menu()

def menu():
    global power, total_actions, usage, Ldoor, Rdoor, Bonnie_POS, Chica_POS, Freddy_POS, Endo_POS, night, CustomNight
    total_actions = 0
    score_to_get = 0
    usage = 0
    power = 200  
    Ldoor = 0
    Rdoor = 0
    CustomNight = 0
    Bonnie_POS = 0
    Chica_POS = 0
    Freddy_POS = 0
    Endo_POS = 0
    t = True
    while t:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("| |=================================================================| |")
        print("| |=================================================================| |")
        display_score = min(max(highscore, 0), 10000)
        score_line = f"High Score: {display_score:<5d}"
        print(f"| |{score_line:<65}| |")
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
            print("| |  2. Custom Night                                                | |")
            print("| |  3. Exit Game                                                   | |")
            print("| |                                                                 | |")
            print("| |                                                                 | |")
            print("| |                                                                 | |")            
            print("| |                                                                 | |")
            print("| |                                                                 | |")
            print("| |                                                                 | |")
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
                Custom_Night()
            elif wybor == 4:
                Loading(5)
                print('')
                input("Save cleared.")
                clear_save()
                menu()
            elif wybor == 5:
                os.system("cls")
                print("Exiting...")
                time.sleep(0.5)
                Loading(5)
                os.system("cls")
                exit()
        else:
            if wybor == 2:
                Custom_Night()
            elif wybor == 3:
                os.system("cls") 
                print("Exiting...")
                time.sleep(1)
                Loading(5)
                exit()

def Custom_Night():
    global Bonnie_AI, Chica_AI, Freddy_AI, Foxy_AI, Endo_AI,CustomNight, score_to_get
    s = True
    CustomNight = 1
    animatronic = "Bonnie"
    score_to_get = 0
    while s:
        i = 0
        for i in range(0,5):            
            os.system("cls")
            if i == 0:
                animatronic = "Bonnie"
            elif i == 1:
                animatronic = "Chica "
            elif i == 2:
                animatronic = "Foxy  "
            elif i == 3:
                animatronic = "Freddy"
            elif i == 4:
                animatronic = "Endo  "            
            print("| |=================================================================| |")
            print("| |=================================================================| |")
            print("| |                                                                 | |")
            print("| |                       CUSTOM NIGHT                              | |")
            print(f"| |              Chose AI value of {animatronic} (0-20)                    | |")
            print("| |                                                                 | |")
            print("| |=================================================================| |")
            print("| |=================================================================| |")
            if animatronic == "Bonnie":
                Bonnie_AI = get_int_input(f"Enter AI value for {animatronic}: ", range(0, 21))
                score_to_get += Bonnie_AI * 100 
            elif animatronic == "Chica ":
                Chica_AI = get_int_input(f"Enter AI value for {animatronic}: ", range(0, 21))
                score_to_get += Chica_AI * 100
            elif animatronic == "Foxy  ":
                Foxy_AI = get_int_input(f"Enter AI value for {animatronic}: ", range(0, 21))
                score_to_get += Foxy_AI * 100
            elif animatronic == "Freddy":
                Freddy_AI = get_int_input(f"Enter AI value for {animatronic}: ", range(0, 21))
                score_to_get += Freddy_AI * 100
            elif animatronic == "Endo  ":
                Endo_AI = get_int_input(f"Enter AI value for {animatronic}: ", range(0, 21))
                score_to_get += Endo_AI * 100
        chose = get_int_input("If you want to reset values, enter 1. To start night, enter 2: ", [1, 2])
        if chose == 1:
            continue
        elif chose == 2:
            night_start()
            s = False

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
            if s.strip() == '1987':
                exit()
            else:
                print("Invalid input. Please enter a number.")
                continue
        if valid_options is not None and val not in valid_options:
            print("Invalid option.")
            continue
        return val  
            
#Główna pętla
os.system("cls") 
#clear_save()
night = load_save()
highscore = load_score()
Loading(10)
print("")
input("Ready!")
os.system("cls")
menu()
