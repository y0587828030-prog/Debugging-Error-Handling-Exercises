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

# #step 3
# numbers = [10, 20, 30]
# index = int(input("Choose index: "))
# try:
#     print(numbers[index])
# except IndexError:
#     print("Index not found.")

# #step 4
# prices = {
#     "apple": 3,
#     "banana": 5
# }

# item = input("Enter item: ")
# try:
#     print(prices[item])
# except KeyError:
#     print ("Item not found")

# #step 5
# numbers = [100, 200, 300]
# try:
#     index = int(input("Choose index: "))
#     divider = int(input("Choose divider: "))

#     result = numbers[index] / divider
#     print(result)
# except ZeroDivisionError:
#     print("Error - Cannot divide by 0")
# except ValueError:
#     print("Error - Enter a number.")
# except IndexError:
#     print("Error - Index does not exist")

# #step 6
# try:
#     score = int(input("Enter score: "))
#     print("Your score is", score)
# except ValueError:
#      print("Invalid score")
# finally:
#     print("Check finished")

# #step 7
# name = input("Enter your name: ")
# if name == "admin": #Syntax error - missing colon
#     print("Welcome admin")
# else:
#     print("Welcome user")

# price = 100
# discount = 20

# discount_amount = price * (discount / 100)
# print("discount amount", discount_amount)

# final_price = price - discount_amount
# print(final_price)


## 99.8
## 80
## Logical Error

#אופציה ב בלי פרינט נוסף
# (#step 8
# price = 100
# discount = 20

# x = price/100
# final_price = 100 - x *20
# print(final_price)

# #step 9
# password = "abc123"
# guess = input("Enter password: ")
# print(f"examination: '{guess}' The correct password: '{password}'")

# if guess == password:
#     print("Login successful")
# else:
#     print("Wrong password")

##Logical Error - The password is correct and prints an error, and vice versa.

# #step 10
# try:
#     num1 = int(input("Number 1: "))
#     op = input("Operator: ")
#     num2 = int(input("Number 2: "))

#     if op == "+":
#           print(num1 + num2)
#     elif op == "-":
#          print(num1 - num2)
#     elif op == "*":
#         print(num1 * num2)
#     elif op == "/":
#          print(num1 / num2)
# except ValueError:
#     print("Age must be a number.")
# except ZeroDivisionError:
#      print("Cannot divide by zero.")
# finally:
#     print("Calculator closed.")
# #ValueError
# #ZeroDivisionError


# 10 Extra Exercises
celsius = input("Celsius: ")
try:
    fahrenheit = int(celsius) * 9 / 5 + 32
    print(fahrenheit)
except ValueError:
    print("Only a number must be entered.")
