
# Python Loops

# 1. For Loop
print("For Loop:")
for i in range(1, 6):
    print(i)


# 2. While Loop
print("\nWhile Loop:")
count = 1

while count <= 5:
    print(count)
    count += 1


# 3. Loop through a List
print("\nIterating through a List:")
languages = ["Python", "Java", "C", "SQL"]

for language in languages:
    print(language)


# 4. Break Statement
print("\nBreak Statement:")
for i in range(1, 10):
    if i == 5:
        break
    print(i)


# 5. Continue Statement
print("\nContinue Statement:")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
