##Asks the user for name then says hello
name = input("What is your name?\n")
print("Hello " + name)

##Asks the user for their birth year then calculates their age
birthYear = input("Enter your birth year\n")
age = 2025 - int(birthYear)
print(name + " is " + str(age) + " years old!\n")

##Gets the sum of two inputs
first = input("Enter the first number here: \n")
second = input("Enter the second number here: \n")
sum = int(first) + int(second)

print("The sum of your inputs is: \n" + str(sum))


##String manipulation
phrase = "Python for beginnners"
phrase = phrase.replace("for", "4")
phrase = phrase.upper()
print(phrase)



