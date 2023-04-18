import csv
import random

#account for spelling (autocorrect)
def fish(rod):
    
    allFiles = {
        1: "C:\\Users\\dcnat\\OneDrive\\Desktop\\fishy-game\\data\\BambooRod.csv",
        2: "C:\\Users\\dcnat\\OneDrive\\Desktop\\fishy-game\\data\\StoneRod.csv",
        3: "C:\\Users\\dcnat\\OneDrive\\Desktop\\fishy-game\\data\\MetalRod.csv",
        #4: "data/Tasty Rod.csv",
        #5: "data/God Rod.csv"
    }
    
    with open(allFiles[rod], newline = '') as csvfile:
        fishreader = csv.reader(csvfile)
        bigList = [fish for row in fishreader for fish in row]

    randomFish = random.choice(bigList)

    return randomFish


def main():
    currency = 0;
    gameContinue = True;
    
    '''print("Welcome to Cloudy's fishing village! There are 4 commands in the game. You can 'fish', 'inventory', 'store', or 'achievements'. \nThe commands will let you fish, check your inventory, check the store, or go to the achievements page respectively. Have fun!")
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
            '''
    print(fish(1))
            
            


if __name__ == "__main__":
    main()


#csv file of fish data (Pandas?)
#csv file of fishing rods
#User input that takes in 4 inputs "Fish" "Inventory" "Store" "Achievements"
#fish dataset is random chance
#assign value to each string value of fish