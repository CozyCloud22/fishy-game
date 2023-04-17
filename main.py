#account for spelling (autocorrect)
def main():
    currency = 0;
    gameContinue = True;
    print("Welcome to Cloudy's fishing village! There are 4 commands in the game. You can 'fish', 'inventory', 'store', or 'achievements'. \nThe commands will let you fish, check your inventory, check the store, or go to the achievements page respectively. Have fun!")
    print("To exit the game, type 'exit'.")
    
    while(gameContinue == True):
            userInput = input("\n\nWhat would you like to do?")

            if(userInput == "fish"):
                #make a definition
                print("fish")
            elif(userInput == "inventory"):
                #make a function
                print ("inventory")
            elif(userInput == "store"):
                #make a function
                print("store")
            elif(userInput == "achievements"):
                #make an achievements list
                print("achievements")
            elif(userInput == "exit"):
                gameContinue = False;
            else:
                print("That was an invalid response. Please try again.")
            
            
            


if __name__ == "__main__":
    main()


#csv file of fish data (Pandas?)
#csv file of fishing rods
#User input that takes in 4 inputs "Fish" "Inventory" "Store" "Achievements"
#fish dataset is random chance
#assign value to each string value of fish