# 🔐 Password Strength Cheaker

A simple command-line tool built using Python to **check the strength of a password**.

This project is great for practicing Python fundamentals such as string operations, conditionals, user input, and logical flow.

---

## 🧪 How It Works

- The user is prompted to enter a password.
- The password is then checked against **4 strength criteria**:
  1. Contains both **uppercase** and **lowercase** letters
  2. Contains **digits**
  3. Is **8 or more characters long**
  4. Contains **special characters** (punctuation)

Each criterion adds **1 point** to the password strength.

---

## 📊 Strength Rating System

| Score | Strength   |
|-------|------------|
| 0-1   | Weak       |
| 2-3   | Moderate   |
| 4     | Strong     |

You’ll also see the numeric rating out of 4 along with the strength level.

---

## 🚀 Running the Tool

1. Make sure you have Python installed.
2. Open your terminal and navigate to the project directory:
   ```bash
   cd "Password Strength Cheaker"
   ```
3. Run the script:
   ```bash
   python main.py
   ```

---

## 📁 File Structure
```nginx
Password Strength Cheaker/
├── main.py       # Contains the password strength checking logic
└── README.md     # You're reading it
```

---

## ✅ Features
- Checks multiple aspects of password strength
- Simple and clear feedback for users
- Beginner-friendly logic and easy to modify
- Encourages good password practices

> **Note:** This project is designed for beginners learning Python. You can enhance it later with advanced checks, GUI support, or integrations.
