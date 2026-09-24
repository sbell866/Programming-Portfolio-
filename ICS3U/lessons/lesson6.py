place = (input("enter any place: "))
#stores user input for place in the variable 'place'.
adjective = (input("enter any adjective: "))
#stores user input for adjective in the variable 'adjective'.
name = (input("enter any name: "))
#stores user input for name in the variable 'name'.
othername = (input("enter another name: "))
#stores user input for othername in the variable 'othername'. used for the second character in the story.
animal = (input("enter any animal: "))
#stores user input for animal in the variable 'animal'.
number = int(input("enter any number: "))
#stores user input for number in the variable 'number'. converts the input to an integer.
othernumber = int(input("enter another number: "))
#stores user input for othernumber in the variable 'othernumber'. converts the input to an integer.
print("Once upon a time, " + name + " and " + othername + " took a walk to " + place + ".")
print("While at " + place + ", they saw " + str(number) + " " + animal + "s.")
print("They were shocked at the amount of " + adjective + " " + animal + "s they saw.")
print(name + " told " + othername + " That if there were " + str(othernumber) + " more " + animal + "s, there would be" + " " + str(number + othernumber) + " " + animal + "s.")
print(othername + " said that if there were that many " + animal + "s, they would have to run away.")
print(name + " and " + othername + " spent a bit more time at " + place + " and then went home.")
#prints the madlib.