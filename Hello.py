
userInput = input("Enter your age: ")
userAge = int(userInput)

if userAge < 13:
    print("You are too young")
elif userAge >= 13 and userAge <= 19:
    print("You are a teenager")
else:
    print("You are an Senior")