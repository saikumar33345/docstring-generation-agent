import datetime

def greet(name):
    return f"Hello, {name}"

def get_current_year():
    return datetime.datetime.now().year

user_name = input("Enter your name: ")
print(greet(user_name))

current_year = get_current_year()
print("Current year:", current_year)
