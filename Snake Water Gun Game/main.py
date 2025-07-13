import random

won = "You won!"
lost = "You lost!"
computer = random.choice([1, 2, 3])

youDict = {"s": 1, "w": 2, "g": 3}
reverseDict = {1: "Snake", 2: "Water", 3: "Gun"}

print("Send s for Snake\nw for water\ng for gun")
youStr = input("Enter your choice: ")

if (len(youStr) == 1 and (youStr.lower()=="s" or youStr.lower()=="w" or youStr.lower()=="g")):
    you = youDict[youStr.lower()]
    print(f"You chose {reverseDict[you]} and Computer chose {reverseDict[computer]}")
    if (computer==you):
        print("Its a draw!")
    elif (computer==1 and you==2) or (computer==2 and you==3) or (computer==3 and you==1):
        print(lost)
    elif (computer==1 and you==3) or (computer==2 and you==1) or (computer==3 and you==2):
        print(won)
    else:
        print("Something went wrong")

else:
    print("Your input is invalid! Run the program again and play correctly as instructed.")
