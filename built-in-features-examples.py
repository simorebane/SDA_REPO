#abs value
import math
import random

temperature = -5
print(abs(temperature))

# CALCULATE HOW MUCH MONEY YOU WILL HAVE AFTER 3 YEARS, 100 EUR, INTEREST RATE 2%
#WE WILL FIND FINAL AMOUNT

investment = 100
intrest_rate = 0.02
years = 3
final_amount = investment * pow(1 + intrest_rate, years)
print(final_amount)

#math cell

people = 7
pizza_needed = math.ceil(people/3)
print(pizza_needed)

#math sqrt
area = 16
side_lenght = math.sqrt(area)
print(side_lenght)

#random module functions

#flipping a coin, simulate this and check if it is above or below 0.5

flip = random.random()
print(flip)
if flip > 0.5:
    print("Heads")
else:
    print("Tails")

#boardgame roll a dice to get a random number between 1 to 6

dice_roll = random.randint(1, 6)
print(dice_roll)


url = "https://www.example.com"
domain = url.find(".com")
print(domain)

error_message = "401 not found"
fixed_message = error_message.replace("401", "500")
print(fixed_message)

email = "contact@company.com "
print(email.strip())

addresses = "baker street, tallinn; 742 city center"
addresses_list = addresses.split(";")
print(addresses_list)
