import random

n = random.randint(1, 100) # randomly generates a number between 1 and 100
a=-1 # Initial placeholder value so the loop starts (since -1 is not the target)
guess = 0 # sets the initial number of guess as 0

while a != n:
    a = int(input("Guess the number: ")) # Gets the input from the user
    guess += 1 # increases the number of guess each time

    if a < n:
        print("📈 Guess a higher number!")

    elif a > n:
        print("📉 Guess a lower number!")

print(f"Congratulations! You have successfully guessed the number {n} in {guess} attempts.")

# The below logic makes the final output more user friendly, neet and clean for the user
if guess <= 5:
    print("🔥 Amazing! That was quick!")

elif guess <10:
    print("👍 Good job!")

else:
    print("😅 Took a while, but you made it!")
