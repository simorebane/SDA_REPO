#example of a function with return statement
from numpy.ma.extras import average


def calculate_discounted_price(original_price, discount_percentage):
    discounted_price = original_price - (original_price*discount_percentage/100)
    return discounted_price

final_price = calculate_discounted_price(100, 20)
print("final price:", final_price)



#empty return clause

def check_stock(item_stock):
    if item_stock == 0:
        return #no value returned
    return f"stock avaliable:  {item_stock}"

print(check_stock(0))

#function termination with return clause

def check_bank_balance(balance):
    if balance < 0:
        return "insufficent funds"
    return "transaction successful"
    print("this will never print") # this line will never print, because it is afer reutrn

print(check_bank_balance(-20))


# multiple outputs with return clause

def get_product_details():
    product_name = "laptop"
    price = 1200
    stock = 5
    return product_name, price, stock

name, cost, available_stock = get_product_details()
print(f"Product: {name}, Price: {cost}, Available stock: {available_stock}")


#example with lists and dictionaries

def restaurant_menu():
    menu_items = ["burger", "salad", "pasta", "soup"]
    prices = {"burger": 8, "salad": 12, "pasta": 10, "soup": 6}
    most_expensive = max(prices, key=prices.get)
    return menu_items, prices, most_expensive

items, price_list, expensive_item = restaurant_menu()
print("Menu items:", items)
print("Menu price list:", price_list)
print("Menu most expensive item:", expensive_item)


#modularity examples  -  not modular, wrong way

def process_data(data):#function name is not clear
    total = 0
    for number in data:
        total += number
    average = total / len(data)
    print(total)
    print(average)
    return data

#modularity examples  -  modular, correct way

def calculate_sum(data):
    total = sum(data)
    return total

def calculate_average(data):
    total = calculate_sum(data)
    average = total/len(data)
    return average

# parameters instead of global variables

#example without parameters (bad practice) Global variable

cofffee_type = "black coffee"


def make_coffee():
    print("Making", cofffee_type)


make_coffee()

#example with parameters instead fo global variable

def make_coffee(coffee_type):
    print("Making", coffee_type)

make_coffee("latte")


# bad practice
discount = 10
def apply_discount():
    price = 100
    final_price = price - discount
    print(final_price)

apply_discount()


# Good practice

def apply_discount2(price, discount):
    final_price = price - discount
    print("final price", final_price)

apply_discount2(100, 10)

#example of long function, bad practice

#def process_user_data(data, user_name, age, email, address):
    # ...

#example of shorter (good practice)
#def get_user_data(user_id):
    # ..



