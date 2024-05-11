
import random

class DiceRoller:
    def roll_dice(self):
        return random.randint(1, 6)

def main():
    dice_roller = DiceRoller()

    while True:
        print("\nMenu:")
        print("1. Roll Dice")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            result = dice_roller.roll_dice()
            print("You rolled:", result)
        elif choice == "2":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
