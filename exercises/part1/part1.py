#first printout exersice 
print("Row, row, row, your boat,")
print("Gently down the stream.")
print("Merrily, merrily, merilly, merrily,")
print("Life is but a dream.")


#program the tell us how many minutes in a year
print("Minuetes in a year: ")
print(60 * 24 * 365) #minutes in a years





#information input
name = input("what is your name ")
print("!" + name + "!" + name +  "!" )


#exactly program 

name = input("NAME: ")
age = int(input("AGE: "))
skill1 = input("SKILL1 ")
level1 = input("level1 ")
skill2 = input("SKILL2 ")
level2 = input("level2 ")
skill3 = input("skill3 ")
level3 = input("level3 ")
lower = int(input("lower "))
upper = int(input("upper "))

print(f"My name is {name}, I am {age} years old")
print("My are ")
print(f"- {skill1} ({level1})")
print(f"- {skill2} ({level2})")
print(f"- {skill3} ({level3})")
print(f"I am looking for a job with a salary of {lower}-{upper} euros per month")


#Order of magnitude
print("  ")

number = int(input("Please type in a number: "))

if number < 1000 :
    print("Number smaller than 1000")
if number < 100 :
    print("This number is smaller than 100")
if number < 10 :
    print("This number is smaller than 10")
    
print("Thank you!")