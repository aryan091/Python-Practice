# Write a Python program using map() that converts a list of strings to uppercase.

def up(string_list):
    upp = list(map(str.upper , string_list))
    return upp

string_list = ["apple", "banana", "cherry"]
uppList = up(string_list)

print(uppList)