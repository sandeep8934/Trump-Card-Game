import random

cards = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
             "8": 8, "9": 9, "10": 10, "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}

print(f"\nWelcome to Trump Card Game. All the best.\n")
name = input("Enter your name to start the game: ")
name = name.capitalize()

human_points = 0
bot_points = 0

chances = 10

while True:

    chances = chances - 1

    if chances >= 0:
        play_again = input(f"Press enter to shuffle cards: ")
        if play_again == "":

            human_choice = random.choice(list(cards.keys()))
            bot_choice = random.choice(list(cards.keys()))
            print(f"\nYour choice is = {human_choice}")
            print(f"Bot choice is = {bot_choice}")

            if cards.get(human_choice) < cards.get(bot_choice):
                bot_points = bot_points + 1
                print("You Loose")

            elif cards.get(human_choice) > cards.get(bot_choice):
                human_points = human_points + 1
                print("You Win")

            elif cards.get(human_choice) == cards.get(bot_choice):
                print("Tie")

            print(f"\nYou have left {chances} more chances.")

    else:
        print("\n..Game over..")
        print(f"\nYour Total Points = {human_points}\nBot Total Points= {bot_points}")
        if human_points > bot_points:
            print(f"Congratz {name}. You win this game.")
        elif human_points < bot_points:
            print("You Loss. Better Luck Next Time.")
        else:
            print(f"It's Tie..Neither You Win Nor You Lost.")

        break



