age = int(input("Enter your age: "))
if age < 18:
    print ("You are not an adult.")
else:
    print ("You are an adult.")
number = int(input("Enter any number: "))
if number % 2 == 0:
    print ("The number is even.")
else:
    print ("The number is odd.")
grade = int(input("Enter your grade: "))
if grade >= 80:
    print ("You got a Level 4.")
if grade >= 70 and grade < 80:
    print ("You got a Level 3.")   
if grade >= 60 and grade < 70:
    print ("You got a Level 2.")
if grade < 60:
    print ("You got a Level 1.")
temp = int(input("Enter the temperature in Celsius: "))
if temp > 25:
    print ("It's hot outside.")
else:
    print ("It's cold outside.")
password = input("Enter your password: ")
if password == "tiger123":
    print ("Access granted.")
else:
    print ("Access denied.")