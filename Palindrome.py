# Question: Write a Python program to check if a given string is a palindrome or not.

str = "nitini";

start = 0;
end = len(str) - 1;

while start < end:
    if (str[start] != str[end]):
        print("Not a palindrome");
        exit();
    else:
        start = start + 1;
        end = end - 1;
       
print("Palindrome")        