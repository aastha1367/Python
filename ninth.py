print("Welcome to the Interactive Personal Data Collector!\n")

name = str(input("Please enter your name: "))
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
favnumber = int(input("Please enter your favourite number: "))

print("Thank you! Here is the information we collected:")

print("Your name is", name, "(Type:", type(name), ", id(name), ")
print("Your age is", age, "(Type:", type(age), ", id(age), ")
print("Your height is:", height, "(Type:", type(height), ", id(height), ")
print("Your fav number is :", favnumber, "(Type:", type(favnumber), ", id(favnumber), ")

print("Thank you for using the Personal Data Collector. Goodbye!")

