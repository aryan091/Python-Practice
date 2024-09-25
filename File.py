# Write a Python program to read a file and count the number of words in it.

f =open("Prime.py","r")
totalWord=0
for line in f:
    words=  line.split()
    totalWord += len(words)
    
print("Number of words in the file:",totalWord)
    
f.close()