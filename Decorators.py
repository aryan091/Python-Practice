#  Write a Python decorator that prints "Function execution started" before the function call and "Function execution finished" after the function call.


def logging(func):
    def wrapper(*args, **kwargs):
        print("Function execution started")
        result = func(*args, **kwargs)
        print("Function execution finished")
        return result
    
    return wrapper

@logging
def chai(name):
    print(f"{name} is drinking Chai")
    
chai("Aryan") 
    