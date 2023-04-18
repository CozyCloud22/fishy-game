import csv
import random
import pandas as pd
import urllib

#defining global variables and dictionaries
currency = 0
rod = "Bamboo Rod"

fishInventory = {
    "Trout": 0,
    "Salmon": 0,
    "Bass": 0,
    "Tuna": 0,
    "Marlin": 0,
    "Swordfish": 0,
    "Pike": 0,
    "Catfish": 0,
    "Cod": 0
}

fishPrices = {
    "Trout": 10,
    "Salmon": 20,
    "Bass": 15,
    "Tuna": 50,
    "Marlin": 75,
    "Swordfish": 100,
    "Pike": 12,
    "Catfish": 45,
    "Cod": 8
}

rodPrices = {
    "Stone Rod": 200,
    "Metal Rod": 500
}

#function for the fish action
def fish(rod):
    
    #routing the CSV files to the code
    allFiles = {
        "Bamboo Rod": "https://raw.githubusercontent.com/CozyCloud22/fishy-game/main/data/BambooRod.csv",
        "Stone Rod": "https://raw.githubusercontent.com/CozyCloud22/fishy-game/main/data/StoneRod.csv",
        "Metal Rod": "https://raw.githubusercontent.com/CozyCloud22/fishy-game/main/data/MetalRod.csv"
    }
    url = allFiles[rod]

    #read the specified CSV file
    df = pd.read_csv(url)

    #extract the values from the DataFrame and add them to a list
    bigList = df.values.flatten().tolist()

    randomFish = random.choice(bigList)

    randomFish = randomFish.strip()
    
    return randomFish

def inventory():
    fishHolder = []

    #self note. f" is a string literal {} <-- contains the string. Very useful
    print(f"You have: {currency} dollar, a {rod}, and these fishies: ")
    
    #for loop to iterate the count based on the number of fishies. Iterates over every item in dictionary
    for fishies, count in fishInventory.items():
        if count > 0:
            fishHolder.append(f"{fishies}: {count}")
    
    #temp string to make the output a bit neater (creates a newline per fish)
    temp = "\n".join(fishHolder)
    
    return temp
    

#function that updates the global dictionary of fish inventory
def updateFishCount(fishName):
    global fishInventory
    
    #updates the global dictionary fish count if fish is caught
    if fishName in fishInventory:
        fishInventory[fishName] += 1

#function for store transactions
def storeContent():
    print("Hello and welcome to Cloudy's fish shop where you can sell your fish and buy fishing rods!")

    #while loop to continue user shopping until user wants to exit
    while(True):
        #defining global variables that will be used
        global currency
        global rod

        question = input("\nWhat would you like to do in the store? You can sell or buy: ")
        if(question == "sell"):
            totalValue = 0
            secondQuestion = input("\nWhat would you like to sell (You can click enter 'all' as well): ")
            
            #checks to see if the fish is a valid one
            if(secondQuestion in fishInventory):
                thirdQuestion = int(input("\nHow many would you like to sell? "))
                
                #checks to see if user has the correct amount
                if(thirdQuestion <= fishInventory[secondQuestion]):
                    tempVal = fishPrices[secondQuestion]
                    totalValue += tempVal
                    fishInventory[secondQuestion] -= thirdQuestion
                    print("Successfully sold!")
                else:
                    print("You don't have enough fishies")
                
                currency += totalValue

            #gives the user the option to sell all
            elif(secondQuestion == "all"):
                allZeroes = True

                #iterates through all the possible fish the user has to sell them
                for temp, count in fishInventory.items():
                    if(count > 0):
                        tempVal = fishPrices[temp]
                        totalValue += tempVal
                        fishInventory[temp] = 0
                        
                    if(count != 0):
                        allZeroes = False
                
                #sends a message to user that they have nothing in inventory
                if(allZeroes == True):
                    print("You have nothing to sell :(")
                else:
                    print("Successfully sold!")

                currency += totalValue
            elif(secondQuestion == "exit"):
                break
            else:
                print("That's not a valid response, please try again.")
        #sets the user up to buy a fishing rod
        elif(question == "buy"):
            storage = ""
            storageList = []
            for rods, prices in rodPrices.items():
                storageList.append(f"{rods}: {prices}")
            storage = "\n".join(storageList)
            print(f"You can currently buy: \n{storage}")
            
            #user input to buy rod
            questionFour = input("\nWhat would you like to buy?('exit' to leave) ")
            if(questionFour in rodPrices):
                if(currency >= rodPrices[questionFour]):
                    currency -= rodPrices[questionFour]
                    rod = questionFour
                    print(f"\nYou have successfully bought {rod}!")
                else:
                    print("You do not have enough money to buy this rod!")
            else:
                print("That is not a valid response")
            
        #allows user to leave
        elif(question == "exit"):
            return ""
        else:
            print("That is not a valid response. Please try again")

#main function
def main():
    gameContinue = True;
    #need to have a global variable for this somewhere
    global rod
    
    print("Welcome to Cloudy's fishing village! There are 3 commands in the game. You can 'fish', 'inventory', and 'store'. \nThe commands will let you fish, check your inventory, and shop at the store, respectively. Have fun!")
    print("To exit the game, type 'exit'.")
    
    while(gameContinue == True):
            userInput = input("\nWhat would you like to do? ")

            if(userInput == "fish"):
                tempVar = fish(rod)
                print(f"\nYou got: {tempVar}!")
                updateFishCount(tempVar)
            elif(userInput == "inventory"):
                print()
                print(inventory())
            elif(userInput == "store"):
                print(storeContent())
            elif(userInput == "exit"):
                print("\nThank you for playing! Made by Darrian Chen!")
                gameContinue = False;
            else:
                print("That was an invalid response. Please try again.")
            
if __name__ == "__main__":
    main()