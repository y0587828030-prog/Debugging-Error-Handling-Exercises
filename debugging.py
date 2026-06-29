##Python Debugging + Error Handling Exercises
# #step 1
# age = input("Enter your age: ")
# try:
#     next_year = int(age) + 1
#     print("Next year you will be", next_year)
# except:
#     print("Age must be a number.")
# #ValueError:


#step 2
a = int(input("First number: "))
b = int(input("Second number: "))
try:
    print(a / b)
except:
    print("Cannot divide by zero.")
#ZeroDivisionError