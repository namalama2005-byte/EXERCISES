    
#example
print( )
sentence = input('write an sentence: ')
index = 0
word = 1
while index < len(sentence):
    char = sentence[index]

    if char == " " :
        word += 1
    index += 1
print(f"there are {word} words in the sentence.")

#Exercise1
#Hello Visual Studio Code

print("    ")
while True :
    Editor = input("Editor: ")
    real = "visual studio code"
    if Editor.lower() == real :
        print("visual studio code")
        break
    else :
        print("Not good")




#EXERCISE1 PART4
#LINE
print("             ")
def line(num, string):
    print(f'{string * num}')
        

line(7, "%")
line(10, "LOL")
line(3, "")


#EXERCISE 
#A BOX OF HASHES
print()
def hashe(hash):
    print("##########")


def box_of_hashes(time):
    while time > 0:
        hashe(hash)
        time -= 1
        

box_of_hashes(5)
print()
box_of_hashes(2)


print()
def shape(int, str, int1, str1):
    for i in range(1, int + 1):
        print(str*i)


    for _ in range(int1):
        print(str1* int)


shape(5, 'x', 3, "*")
print()
shape(2, "o", 4, "+")
print()
shape(3, ".", 0, ",")


#exercise in part 4
print( )
def greatest_number(a, b, c):
    if a > b :
        return a
    elif b > c :
        return b
    else : 
        return c
    

print(greatest_number(3, 4, 1)) # 4
print(greatest_number(99, -4, 7)) # 99
print(greatest_number(0, 0, 0)) # 0

print( )
#exercise
def same_chars(name, d, e):
    if d < 0 or e < 0 or d >= len(name) or e >= len(name):
     return False
    return name[d] == name[e]

# same characters m and m
print(same_chars("programmer", 6, 7)) # True

# different characters p and r
print(same_chars("programmer", 0, 4)) # False

# the second index is not within the string

print(same_chars("programmer", 0, 12)) # False


#Change the value of an item
print(" ")


Lists = [1, 2, 3, 4, 5]
while True :
    index = int(input("index. "))
    if index < 0:
        break
    new_value = int(input("New Value. "))

    Lists[index] = new_value
    print(Lists)






#Add items to a list
ITEM = int(input("how many items? "))
ITEM_1 = int(input("ITEM 1: "))
ITEM_2 = int(input("ITEM 2: "))
ITEM_3 = int(input("ITEM 3: "))

ITEMS = [ITEM_1, ITEM_2, ITEM_3 ]
print(ITEMS)



#Addition and removal  
items = []

print(f"The list is now {items}")

while True:
    choice = input("add, remove or exit: ")

    if choice == "add":
        if items:
            items.append(items[-1] + 1)
        else:
            items.append(1)
        print(f"The list is now {items}")

    elif choice == "remove":
        items.pop()
        print(f"The list is now {items}")

    elif choice == "x":
        print("Bye!")
        break
        

#Addition and removal
List = []
while True :

    word = input("WORD: ")
    
    if word in List:
        print(f'you write {len(List)} difference word')
        break

    List.append(word)




#Addition and removal
print('')
value = []
while True:
    new_item = int(input('NEW ITEM: '))
    if new_item == 0 :
        print('bye!')
        break

    value.append(new_item)
    
    print(f'the list now: {value}')
    print(f'the list in order: {sorted(value)}')
    