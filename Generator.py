# Question: Write a generator function to generate the Fibonacci sequence up to n terms.


def fib(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b
        

n = 10

for i in fib(n):    
    print(i)     