def countdown(num):
    print("Countdown starting")
    while num > 0:
        yield num
        num -= 1
    print("Countdown finished")

# Using the countdown generator
cd = countdown(5)

for i in cd:
    print(i)


# yield is often used when reading large files line by line without loading the entire file into memory.