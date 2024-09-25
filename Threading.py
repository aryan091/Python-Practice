import threading

# Function to print even numbers
def print_even():
    for i in range(1, 11):
        if i % 2 == 0:
            print(f"Even: {i}")

# Function to print odd numbers
def print_odd():
    for i in range(1, 11):
        if i % 2 != 0:
            print(f"Odd: {i}")

# Creating two threads
even_thread = threading.Thread(target=print_even)
odd_thread = threading.Thread(target=print_odd)

# Starting the threads
even_thread.start()
odd_thread.start()

# Waiting for both threads to finish
even_thread.join()
odd_thread.join()

print("Both threads have finished execution.")
