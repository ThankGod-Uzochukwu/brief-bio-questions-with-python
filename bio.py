print("Bio")
name = input("Please Enter Your Name: ")
print("Hello " + name)
greetings = input("How Are You? ")
if greetings != ("am not fine"):
    print("Good to know")
else :
    print("Oh, so sorry about that ")
age = input("Please how old are you? : ")
print("So, ", name, "is ", age, "Years old right?: " )
answer = input("Please answer the above question: ")
if age <= ("17"):
    print("You're too young")
else:
    print("Thats great")
print("Bio Confirmed!")