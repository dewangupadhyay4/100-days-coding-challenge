# def decorator_func(func):
#     def wrapper():
#         print("Before func runs")
#         func()
#         print("After func runs")
#     return wrapper

# def say_hello():
#     print("Hello this is say_hello function")

# # decorated=decorator_func(say_hello)
# # decorated()

# @decorator_func
# def say_bye():
#     print("Hello this bye function")

# say_bye()

#-------------------------------------------------------------------------------------------------------

def decorated_func(func):
    def wrapper(*args, **kwargs):
        print("Before func runs")
        result=func(*args, **kwargs)
        print("After func runs")
        return result
    return wrapper

@decorated_func
def greet(name):
    print(f"Hello {name}")

greet("dewang")