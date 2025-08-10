import random
from abc import ABC, abstractmethod

# Base abstract class for any character in the game


class Character(ABC):

    def __init__(self, name, health):
        self.name = name
        self.health = health

    # This method must be defined in all subclasses
    @abstractmethod
    def attack(self):
        pass


# Player class (inherits from Character)
class Player(Character):

    def __init__(self, name, health=100):
        super().__init__(name, health)
        self.inventory = []  # Stores collected items

    def attack(self):
        # Player attack damage is between 5 and 15
        return random.randint(5, 15)


# Enemy class (inherits from Character)
class Enemy(Character):

    def __init__(self, name, health):
        super().__init__(name, health)

    def attack(self):
        # Enemy attack damage is between 5 and 10
        return random.randint(5, 10)


# Save game state to a file
def save_game(player):
    with open("save.txt", "w") as f:
        # Format: name,health,item1,item2,...
        f.write(f"{player.name},{player.health},{','.join(player.inventory)}")


# Load game state from a file
def load_game():
    with open("save.txt", "r") as f:
        data = f.read().split(",")
        p = Player(data[0], int(data[1]))  # Create player from saved data
        p.inventory = data[2:]  # Remaining data is inventory
        return p


# Main game loop
def main():
    print("Welcome to Python Adventure Game : ")
    choice = input("Do you wanna load the game (y/n) : ")

    # Load existing game or start new
    if choice.lower() == "y":
        player = load_game()
        print(f"Welcome, Back {player.name}")
    else:
        player = Player(input("Enter your Name : "))

    # Game loop continues until break
    while True:
        action = input("Do you wanna (s)earch or (m)ove ?")

        # Searching for items
        if action.lower() == "s":
            item = random.choice(["Potion", "Shield", "Sword"])
            print(f"You found a {item}")
            player.inventory.append(item)

        # Moving and possibly encountering enemies
        elif action.lower() == "m":
            if random.choice([True, False]):  # 50% chance of enemy
                enemy = Enemy("Goblin", 30)
                print(f"A Wild Goblin Appears🧌")

                # Fight until one is dead
                while enemy.health > 0 and player.health > 0:
                    player.health -= enemy.attack()
                    enemy.health -= player.attack()
                    print(
                        f"Player HP : {player.health} and Enemy HP : {enemy.health}")

                    if player.health <= 0:
                        print("You died! Goblin killed you💀")
                    else:
                        print("You Defeated the Goblin🧌")
            else:
                print("You moved safely🕸️")

        # If player dies, exit loop
        if player.health <= 0:
            break

        # Option to save and quit
        if input("Do you wanna quit and save (yes/no) :").lower() == "yes":
            save_game(player)
            print("Game Saved, GoodBye!👺⚔️")
            break


# Run the game
if __name__ == "__main__":
    main()
