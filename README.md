# Fishing Game

This project is a simple text-based fishing game where the player buys a fishing rod and attempts to catch fish in order to earn money.

## Table of Contents

- [Introduction](#introduction)
- [Game Mechanics](#game-mechanics)
- [Data Source](#data-source)
- [Conclusion](#conclusion)

## Introduction

Fishing is a popular pastime, and this game aims to simulate the experience of catching fish in a fun and interactive way. The player starts with a certain amount of money and must buy a fishing rod before they can begin fishing. After buying a rod, the player can go fishing and attempt to catch different types of fish. Each fish has a different value, and the player can sell the fish they catch to earn money. The game ends when the player runs out of money.

## Game Mechanics

The player can perform the following actions:

- `buy`: purchase a new fishing rod
- `fish`: attempt to catch a fish
- `sell`: sell caught fish to earn money
- `inventory`: view the types and quantities of fish in the player's inventory
- `exit`: end the game

The player can buy one of three types of fishing rods, each with a different price and a different chance of catching a fish:

- Bamboo Rod: $50
- Stone Rod: $200
- Metal Rod: $500

The player can attempt to catch a fish by using the `fish` action. The type of fish that is caught is determined randomly by reading from a CSV file that contains the names of different types of fish. Each fish has a different value, and the value of the fish that is caught is added to the player's inventory.

The player can sell their caught fish to earn money by using the `sell` action. The value of the fish that is sold is added to the player's currency.

## Data Source

The names of the different types of fish that can be caught in the game are stored in CSV files, one for each type of fishing rod. The CSV files are stored in a GitHub repository and are read into the game using the Pandas library.

## Conclusion

In conclusion, this project provides a fun and interactive way for players to experience the thrill of fishing in a text-based game. The game mechanics are simple and easy to understand, making it accessible to a wide range of players. Players can use the insights gained from playing the game to better understand the value of different types of fish and the importance of choosing the right fishing rod.
