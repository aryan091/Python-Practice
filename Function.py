# Write a function that takes a list of integers and returns a new list with only the even numbers.

def evenList(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(evenList(numbers))