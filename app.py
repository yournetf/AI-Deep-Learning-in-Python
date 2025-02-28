# ##Asks the user for name then says hello
# name = input("What is your name?\n")
# print("Hello " + name)
#
# ##Asks the user for their birth year then calculates their age
# birthYear = input("Enter your birth year\n")
# age = 2025 - int(birthYear)
# print(name + " is " + str(age) + " years old!\n")
#
# ##Gets the sum of two inputs
# first = input("Enter the first number here: \n")
# second = input("Enter the second number here: \n")
# sum = int(first) + int(second)
#
# print("The sum of your inputs is: \n" + str(sum))
#
#
# ##String manipulation
# phrase = "Python for beginnners"
# phrase = phrase.replace("for", "4")
# phrase = phrase.upper()
# print(phrase)

#Classes
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

node1 = ListNode(1)
print(node1.val)

node2 = ListNode(2)
print(node2.val)
print()

#Loops
arr = [1, 10, 3, 4]
for i in range (len(arr)):
    print(arr[i])
print()

index = len(arr)-1
while index >= 0:
    print(arr[index])
    index -= 1
print()

#Booleans

#True
result = True or False
#False
result = True and (False and False)
#False
result = 2 == 1
#True
result = 1 == 1
print(result)
print()

#max/min
result = max(5,2)
print(result)
result = min(5,2)
print(result)
print()

#Dictionaries

dictionary = {}

dictionary[10] = "hello"
dictionary["A"] = 10
print(dictionary)

if "10" in dictionary:
    print(True)
else:
    print(False)

dictionary["A"] += 1
print(dictionary)

dictionary["A"] -= 1
print(dictionary)

dictionary.setdefault("A", 0)
dictionary.setdefault("B", 0)

dictionary["B"] += 1
print(dictionary)

for key, value in dictionary.items():
    print(str(key), str(value))

while dictionary["A"] > 0:
    dictionary["A"] -= 1
    print(dictionary)

#Strings
str = "AB CD E"
splitStr = str.split(" ")
print(splitStr)

for arrayString in splitStr:
    print(arrayString)

resultString = "".join(splitStr)
print(resultString)

str = "hello"
strArr = list(str)
print(strArr)
strArr[0], strArr[1] = strArr[1], strArr[0]
print(strArr)
result = "".join(strArr)
print(result)

resultArr = list([5, 4, 3, 2, 1])
resultArr.sort()
print(resultArr)