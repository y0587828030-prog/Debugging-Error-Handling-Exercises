#Python Debugging + Error Handling Exercises
# #step 1
# age = input("Enter your age: ")
# try:
#     next_year = int(age) + 1
#     print("Next year you will be", next_year)
# except ValueError:
#     print("Age must be a number.")



# #step 2
# a = int(input("First number: "))
# b = int(input("Second number: "))
# try:
#     print(a / b)
# except ZeroDivisionError:
#     print("Cannot divide by zero.")

#step 3
numbers = [10, 20, 30]
index = int(input("Choose index: "))
try:
    print(numbers[index])
except IndexError:
    print("Index not found.")