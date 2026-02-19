number = int(input("Please type in a number: "))
if number > 100 :
    print("The number was greater than one hundred ")
    number = number - 100
    print("Now its value has decreased by one hundred ")
    print(f"Its value is now {number}")
print(f"{number} must be my lucky number!")
print("Have a nice day!")

'''Number of characters'''
print("                 .                      ")

word = input("give a word: ")
if word != "" :
    print(f"There are {len(word)} letters in the word {word}")
print("thank you!")


#Typecasting

"""Typecasting"""
fnum = float(input("Please type in a number: "))
print(F"integer part: {int(fnum)}")
print(f"Decimal part: {float(fnum)}")

#Age of maturity
age = int(input("How old are you? "))

if age >= 18:
    print("You are of age!")
else:
    print("You are not of age!")


#Please write a program which asks for the names and ages of two persons. The program should then print out the name of the elder.

print("""Please write a program which asks for the names and ages of two persons. 
      The program should then print out the name of the elder.""")
print("person1: ")
name = input("name: ")
age = int(input("age: "))
print("person2:")
name1 = input("name: ")
age1 = int(input("age: "))
if age1 < age:
    print(f"The elder is {name}.")
elif age1 > age:
    print(f"The elder is {name1}.")
elif age1 == age:
    print(f"{name} and {name1} are the same age")

#ALPHABETICAL LAST
word1 = input("Please type in the 1st word: ")s
word2 = input("Please type in the 2nd word: ")

if word1 > word2:
    print(f"{word1} comes alphabetically last.")
elif word2 > word1:
    print(f"{word2} comes alphabetically last.")
else:
    print("You gave the same word twice.")

#Age check:
print("""Please write a program which asks for the user's age. 
      If the age is not plausible, that is, it is under 5 or 
      something that can't be an actual human age, the program 
      should print out a comment""")
age =int(input("what is your age? "))
if age >= 5 :
    print(f"Ok, you're {age} years old ")
elif age < 5 :
    print("i suspect you can't write quite yet...")
elif age < 1 :

    print("That must be a mistake")

