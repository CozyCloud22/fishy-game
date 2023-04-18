import csv
import random

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

#REMEMBER FOR FINAL VERSION TO PUT THE ALTERNATE PATH DOWN

#function for the fish action
def fish(rod):
    
    #routing the CSV files to the code
    allFiles = {
        "Bamboo Rod": "C:\\Users\\dcnat\\OneDrive\\Desktop\\fishy-game\\data\\BambooRod.csv",
        "Stone Rod": "C:\\Users\\dcnat\\OneDrive\\Desktop\\fishy-game\\data\\StoneRod.csv",
        "Metal Rod": "C:\\Users\\dcnat\\OneDrive\\Desktop\\fishy-game\\data\\MetalRod.csv",
    }
    
    #opens the CSV files and adds them to a list
    with open(allFiles[rod], newline = '') as csvfile:
        fishreader = csv.reader(csvfile)
        bigList = [fish.strip() for row in fishreader for fish in row]

    #chooses a random fish
    randomFish = random.choice(bigList)

    return randomFish

def inventory():
    fishHolder = []

    #self note. f" is a string literal {} <-- contains the string. Very useful
    print(f"You have: {currency} dollars and these fishies: ")
    
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
    if fishName in fishInventory:
        fishInventory[fishName] += 1

def storeContent():
    print("Hello and welcome to Cloudy's fish shop where you can sell your fish and buy fishing rods!")
    #create a messagepost sell fish

    while(True):
        global currency
        global rod

        question = input("\nWhat would you like to do in the store? You can sell or buy: ")
        if(question == "sell"):
            totalValue = 0
            secondQuestion = input("\nWhat would you like to sell (You can click enter 'all' as well): ")
            
            if(secondQuestion in fishInventory):
                thirdQuestion = int(input("\nHow many would you like to sell? "))
                if(thirdQuestion <= fishInventory[secondQuestion]):
                    tempVal = fishPrices[secondQuestion]
                    totalValue += tempVal
                    fishInventory[secondQuestion] -= thirdQuestion
                else:
                    print("You don't have enough fishies")
                
                currency += totalValue
            elif(secondQuestion == "all"):
                allZeroes = True
                for temp, count in fishInventory.items():
                    if(count > 0):
                        tempVal = fishPrices[temp]
                        totalValue += tempVal
                        fishInventory[temp] = 0
                    if(count != 0):
                        allZeroes = False
                if(allZeroes == True):
                    print("You have nothing to sell :(")


                currency += totalValue
            elif(secondQuestion == "exit"):
                break
            else:
                print("That's not a valid response, please try again.")
        elif(question == "buy"):
            storage = ""
            storageList = []
            for rods, prices in rodPrices.items():
                storageList.append(f"{rods}: {prices}")
            storage = "\n".join(storageList)
            print(f"You can currently buy: \n{storage}")
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
                #make a function
                print(storeContent())
            elif(userInput == "achievements"):
                #make an achievements list
                print("achievements")
            elif(userInput == "exit"):
                gameContinue = False;
            else:
                print("That was an invalid response. Please try again.")
            

if __name__ == "__main__":
    main()