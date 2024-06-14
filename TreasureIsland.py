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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
game_over =False
while not game_over:
    choice = input('you are at crossroad where you want to go,"left" or "right".').lower()
    if choice == 'left':
        while not game_over:
            choice2 = input('you are near to the forest island is behind the forest, type "wait" to wait for vehicle. or "walk" walk through forest".').lower()
            if choice2 =="wait":
                while not game_over:
                    choice3 = input('you have came across the forest the island is in centre of ocean, type"wait" for boat or "swim" for swiming').lower()
                    if choice3 == "wait":
                        while not game_over:
                           choice4 = input("you have reached the island unharmed, so there are house with four doors one red, one yellow one green,and one blue which color you want to chose")
                           if choice4=="red":
                               print("the room is full of fire you died game over.....!")
                               print("TRAIN AGAIN.....!")
                           elif choice3 =="blue":
                               print("the room is full of beast the game is over.....!")
                               print("TRAIN AGAIN.....!")
                           elif choice4=="yellow":
                               print("YOU FOUND THE TRESURE AND YOU WON THE GAME CONGRATULATIONS.....!")
                               game_over = True
                           elif choice4 == "green":
                                print("the room is full of tigers game is over.....!")
                                print("TRAIN AGAIN.....!")
                           else:
                              print("the door you chose doesnt exit game over. TRY AGAIN....!")  
                    else:
                     print("game is over you were swiming and got attacked by shark")
                     print("TRAIN AGAIN.....!")
            else:
              print("the game is over you walk throug forest and got attacked by animal")
              print("TRAIN AGAIN.....!")
    else:
        print("game is over you fall into the hole")
        print("TRAIN AGAIN.....!")

