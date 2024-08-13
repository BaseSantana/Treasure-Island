print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
                        WELCOME TO TREASURE ISLAND!
      ''')
print(" ")
print("Your mission is to find the treasure.")
print("Tread carefully, one wrong move may be detrimental!")
print(" ")
choice1 = input("You're at a crossroad. Where do you want to go?\n      Type \"Left\" or \"Right\": ").lower()

if choice1 == "left":
    print(" ")
    choice2 = input('''You've come to a lake. There is an island in the middle of the lake.
    Type \"Wait\" to wait for a boat. Type \"Swim\" to swim across. ''').lower()
    print(" ")
    if choice2 == "wait":
            print(" ")
            print('''You\'ve made it to the castle. You found three doors colored RED, GREEN and YELLOW\n      Choose wisely, one of the three doors contains the treasure.''')
            choice3 = input("           Choose between RED, GREEN or YELLOW: ").lower()
            if choice3 == "yellow":
                 print(" ")
                 print("           !!!YOU WIN!!!")
            elif choice3 == "red":
                 print(" ")
                 print("       Burned by fire. GAMEOVER")
            elif choice3 == "green":
                 print(" ")
                 print("       Eaten by beasts. GAME OVER.")
            else:
                 print(" ")
                 print("          GAME OVER")
                 
    else:
        print("      Attacked by trout. GAME OVER.")
        print(" ")

else:
    print(" ")
    print("     You fell into a hole. GAME OVER")
    print(" ")