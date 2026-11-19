# BASIC IF/ELSE STATEMENTS

# ========== EASY ==========

# Example 1: Check Age
age = 18

if age >= 18:
    print("Adult")
else:
    print("Minor")

# Example 2: Positive or Negative
number = -5

if number >= 0:
    print("Positive")
else:
    print("Negative")

# Example 3: Even or Odd
number = 8

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# ========== INTERMEDIATE ==========

# Example 4: Passing or Failing
grade = 85

if grade >= 75:
    print("Passed")
else:
    print("Failed")

# Example 5: Compare Two Numbers
a = 20
b = 15

if a > b:
    print("A is greater")
else:
    print("B is greater or equal")

# Example 6: Check Temperature
temperature = 35

if temperature >= 30:
    print("Hot")
else:
    print("Cold")


# ========== HARD ==========

# Example 7: Grade Classification
grade = int(input("Enter your grade: "))

if grade >= 90:
    print("Excellent")
elif grade >= 85:
    print("Very Good")
elif grade >= 75:
    print("Passed")
else:
    print("Failed")

# Example 8: Simple Login
username = input("Enter username: ")
password = input("Enter password: ")

if username == "student" and password == "12345":
    print("Login successful!")
else:
    print("Invalid username or password.")
