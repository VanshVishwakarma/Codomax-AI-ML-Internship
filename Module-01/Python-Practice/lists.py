
# Python Lists

# 1. Creating a List
languages = ["Python", "Java", "C", "SQL"]
print("Languages:", languages)


# 2. Accessing Elements
print("First Element:", languages[0])
print("Last Element:", languages[-1])


# 3. Adding Elements
languages.append("JavaScript")
languages.insert(1, "C++")
print("After Adding:", languages)


# 4. Removing Elements
languages.remove("Java")
languages.pop()
print("After Removing:", languages)


# 5. Updating Elements
languages[0] = "Python Programming"
print("After Updating:", languages)


# 6. Slicing a List
numbers = [10, 20, 30, 40, 50]
print("Sliced List:", numbers[1:4])


# 7. Sorting a List
numbers.sort()
print("Sorted List:", numbers)


# 8. Iterating Through a List
for language in languages:
    print(language)


# 9. List Length
print("Total Elements:", len(languages))

