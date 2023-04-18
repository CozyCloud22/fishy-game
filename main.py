import csv
import random

currency = 0

fishInventory = {"trout": 0, "salmon": 0, "bass": 3, "tuna": 0, "marlin": 0, "swordfish": 0, "pike": 0, "catfish": 0, }

#REMEMBER FOR FINAL VERSION TO PUT THE ALTERNATE PATH DOWN

#account for spelling (autocorrect)

#function for the fish action
def fish(rod):
    
    #routing the CSV files to the code
    allFiles = {
        1: "C:\\Users\\dcnat\\OneDrive\\Desktop\\fishy-game\\data\\BambooRod.csv",
        2: "C:\\Users\\dcnat\\OneDrive\\Desktop\\fishy-game\\data\\StoneRod.csv",
        3: "C:\\Users\\dcnat\\OneDrive\\Desktop\\fishy-game\\data\\MetalRod.csv",
        #4: "data/Tasty Rod.csv",
        #5: "data/God Rod.csv"
    }
    
    #opens the CSV files and adds them to a list
    with open(allFiles[rod], newline = '') as csvfile:
        fishreader = csv.reader(csvfile)
        bigList = [fish for row in fishreader for fish in row]

    #chooses a random fish
    randomFish = random.choice(bigList)

    return randomFish

def inventory():
    print(f"You have: {currency} dollars and these items: ")
    for fishies, count in fishInventory.items():
        if count > 0:
            #self note. f" is a string literal {} <-- contains the string. Very useful
            #need to edit this into a for loop that gives all fishes
            return(f"{fishies}: {count}")
    

#main function
def main():
    currency = 0;
    gameContinue = True;
    
    #print("Welcome to Cloudy's fishing village! There are 4 commands in the game. You can 'fish', 'inventory', 'store', or 'achievements'. \nThe commands will let you fish, check your inventory, check the store, or go to the achievements page respectively. Have fun!")
    #print("To exit the game, type 'exit'.")

    print(inventory())
    
    '''while(gameContinue == True):
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

if __name__ == "__main__":
    main()


#csv file of fish data (Pandas?)
#csv file of fishing rods
#User input that takes in 4 inputs "Fish" "Inventory" "Store" "Achievements"
#fish dataset is random chance
#assign value to each string value of fish