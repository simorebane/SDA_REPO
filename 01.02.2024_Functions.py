from operator import truediv

print("Hello AI")

#new function
def greet1(name):
    print("Hello, " + name)


greet1("function")


def add_numbers(a, b):
    print(a+b)

add_numbers(43, 23)


def multiply(x,y):
     return x * y       #return ends the function

operation = multiply
print(operation(4,5))


def greet(name: str):
    print("hello " + name)

greet("ilmes")


#changing global variable inside a function

count = 0

def increase_count():
    global count
    count +=1
    print(count)

increase_count()
increase_count()


#bank account simulation

def deposit(balance, amount):
    balance += amount
    print("new balance:", balance)

balance = 100
deposit(balance, 50)
print("My latest balance:", balance)


#defining lambda functions

square = lambda x: x**2
print(square(10))


# multiple arguments on lambda functions
add = lambda x, y: x + y
print(add(7,9))


# validating an email address
#simorebane@gmail.com

def is_valid_email(email):
    if "@" not in email or "." not in email:
        return False
    return True

email = "simo.rebane@gmail.com"
if is_valid_email(email):
    print(f"{email} is valid")
else:
    print(f"{email} is not valid")


#validating phone number
phone_number = "37256474897"

def is_valid_phone_number(phone_number):
    if len(phone_number) == 11 and phone_number.startswith("372") and phone_number.isdigit():
        return True
    return False

if is_valid_phone_number(phone_number):
    print("phone number it is valid")
else:
    print("phone number it is not valid")


#modify shopping list

shopping_list = ["bread", "milk", "eggs"]

def add_item_to_list(shopping_list, item):
    shopping_list.append(item)
    return shopping_list

shopping_list = add_item_to_list(shopping_list, "apple")
print(shopping_list)


def remove_item_from_list(shopping_list, item):
    if item in shopping_list:
        shopping_list.remove(item)
    return shopping_list

shopping_list = remove_item_from_list(shopping_list,"eggs")
print(shopping_list)


result = ""
def compute_bmi(weight, height):
    bmi = weight / height ** 2

    if bmi < 18.5:
        result = 'underweight'
    elif bmi > 25:
        result = 'overweight'
    else:
        result = 'normal'
    return result

result = compute_bmi(71, 178)
print(result)

