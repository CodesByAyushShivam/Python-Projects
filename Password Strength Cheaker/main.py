import string

password = input("Enter Your Password: ")

strength = 0

if any(a.islower() for a in password) and any(a.isupper() for a in password):
    strength += 1

if any(a.isdigit() for a in password):
    strength += 1

if len(password) >= 8:
    strength += 1

if any(char in string.punctuation for char in password):
    strength += 1

if strength <= 1:
    print("Your password is weak")
elif strength == 2 or strength == 3:
    print("Your password is moderate")
else:
    print("Your password is strong")

print(f"Your Password Strength rating is {{strength}/4}")
