name = input("Type your name: ")
print("Welcome to the adventure ", name)

answer = input("you are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("you come to a river, you can walk around it or swim across? Type walk to walk and swim to swim across: ").lower()
         
    if answer == "swim":
            print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
            print("you walked for many miles, ran out of water and you lost the game.")
    else:
            print("Not a valid option. you lose.")

elif answer == "right":

    answer = input("you come to a bridge, it looks wobbly, do you want to cross it or head back? (cross/back) ").lower()
    
    if answer == "back":
          print("you go back and lose.")

    elif answer == "cross":
            answer = input("you cross the bridge and meet a stranger. Do you talk to them? (yes/no) ").lower()

            if answer == "yes":
                print("You talk to the stranger and they give you gold. You WIN!")
            elif answer == "no":
                answer = input("You ignore the stranger and they are offended and they want to fight with you. Do you want to fight? (yes/no) ").lower()
                if answer == "yes":
                      print("you fought bravely but they defeated you. You LOSE!")
                elif answer == "no":
                      print("The stranger takes advantage and defeats you. YOU LOSE!")
                else:
                      print("Not a valid option. you lose.")


            else:
                  print("Not a valid option. you lose.")
    
    else:
          print("Not a valid option. you lose.")
  

else:
    print("Not a valid option. you lose.")

print("Thank you for trying", name)