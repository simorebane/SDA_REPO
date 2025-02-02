#example of a function with return statement

def calculate_discounted_price(original_price, discount_percentage):
    discounted_price = original_price - (original_price*discount_percentage/100)
    return discounted_price

final_price = calculate_discounted_price(100, 20)
print("final price:", final_price)
