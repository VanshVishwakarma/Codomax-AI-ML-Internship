
# Python Conditional Statements

# Example 1: If-Else
age = 20

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


# Example 2: If-Elif-Else
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


# Example 3: Nested If
number = 15

if number > 0:
    if number % 2 == 0:
        print("Positive Even Number")
    else:
        print("Positive Odd Number")
else:
    print("Negative or Zero")
