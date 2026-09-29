number = input("Enter a number: ")
#asks for number and stores it in the number variable
othernumber = input("Enter a second number: ")
#asks for a new number and stores it in the othernumber variable
if number > othernumber:
    print(number + " is larger than " + othernumber + ".")
#prints that the first number is larger than the second when the first number is larger than the second
if number < othernumber:
    print(othernumber + " is larger than " + number + ".")
#prints that the second number is larger than the first when the second number is larger than the first
if number == othernumber:
    print(number + " is equal to " + othernumber + ".")
#prints that the numbers are equal