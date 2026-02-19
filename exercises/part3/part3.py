#print number in even
# exercise 1 

number = 1
while True:
    number += 1
    if number % 2 == 0:
        print(number)
        if number == 2000:
            break


#exercise 2
# fixing the code: countdown
print("     ")
print("are you ready? ")
number = int(input("please type in a number: "))
while number > 0 :
    print(number)
    number -= 1
print("now!")

#EXERCISE3
#power of two
print("     ")
limit = int(input("upper limit: "))
numbe = 1
while numbe <= limit:
    print(numbe)
    numbe *= 2


#EXERCISE 4
#string multiply
print("     ")
string = input("please type in string: ")
amount =int(input("please type in an amount: "))
a = 1
while a <= amount:
    print(string * amount)
    if True:
        break
    


#exercise 5
#end to beginning
print("     ")
word = input('Please type in a string: ')
print(word[len(word )-1])
print(word[2])
print(word[1])
print(word[0])


#EXERCISE 6
#underlining
print("     ")
sting = input("Please type in a string: ")
print(sting)
print("_" * len(sting))

sting2 = input("Please type in a string: ")
print(sting2)
print("_" * len(sting2))

sting3 = input("Please type in a string: ")
print(sting3)
print("_" * len(sting3))


#Exercise in part 3
#Powers of base n
print("    ")
upper_limit = int(input("Upper limit: "))
Base = int(input("Base: "))
num = 1
while num <= upper_limit:
    print(num)
    num *= Base