import random

with open("hs.txt", "r") as s:
    ss = s.read()
    
    if (ss == ""):
        with open("hs.txt", "w") as main:
            main.write("0")

def get_computer_choice():
    return random.choice([1, 2, 3])

def result(player, computer):
    if player == computer:
        return 1  # draw
    elif (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
        return 2  # win
    else:
        return 0  # loss

youDict = {"s": 1, "w": 2, "g": 3}
reverseDict = {1: "Snake", 2: "Water", 3: "Gun"}

print("Welcome to Snake Water Gun Game!")
print("Send 's' for Snake, 'w' for Water, 'g' for Gun")
score = 0

for round_num in range(1, 6):
    print(f"\nRound {round_num}")
    youStr = input("Enter your choice: ").lower()
    
    if youStr not in youDict:
        print("Invalid input! Try again with s/w/g.")
        continue

    you = youDict[youStr]
    computer = get_computer_choice()

    print(f"You chose {reverseDict[you]} and Computer chose {reverseDict[computer]}")

    points = result(you, computer)

    if points == 2:
        print("You won this round! (+2)")
    elif points == 1:
        print("It's a draw. (+1)")
    else:
        print("You lost this round. (+0)")

    score += points

print(f"\n🎯 Total Score after 5 rounds: {score}")


with open("hs.txt", "r") as h:
    hs = h.read()
    high = int(hs)

    if (high <= score):
        with open("hs.txt", "w") as file:
            file.write(str(score))
        print(f"Your current score is a high score. \nYour High Score: {score}")
    else:
        print(f"Your Current score: {score}\nYour High Score: {high}")