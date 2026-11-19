
# Python Functions

# 1. Basic Function
def greet():
    print("Welcome to Python Programming!")

greet()


# 2. Function with Parameters
def greet_user(name):
    print("Hello,", name)

greet_user("Vansh")


# 3. Function with Return Value
def add(a, b):
    return a + b

result = add(10, 20)
print("Sum:", result)


# 4. Function with Default Arguments
def introduce(name, course="Computer Science"):
    print(name, "is studying", course)

introduce("Vansh")
introduce("Rahul", "Artificial Intelligence")


# 5. Function with Multiple Return Values
def calculate(a, b):
    return a + b, a - b

sum_result, difference = calculate(20, 10)

print("Addition:", sum_result)
print("Subtraction:", difference)
