##Python Debugging + Error Handling Exercises
#step 1
age = input("Enter your age: ")
try:
    next_year = int(age) + 1
    print("Next year you will be", next_year)
except:
    print("Age must be a number.")


#ValueError: