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