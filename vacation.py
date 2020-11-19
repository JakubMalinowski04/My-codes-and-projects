# trip planner, code will be updating...

# 350 is the price per night. You can change this value according to your needs.
def cost_per_night(nights):
    return 350 * nights

# the value after "return" is a price per one-way flight. I've given you random values. You can change this value according to your needs.
def flight_cost(city):
    if (city == "Los Angeles"):
        return 600
    elif (city == "New York"):
        return 400
    elif (city == "Tampa"):
        return 350
    elif (city == "Miami"):
        return 700
    elif (city == "Seattle"):
        return 860

# this is function for renting cars and discounts.
def car_rental(days):
#                 \/ this value is rental price for one day
    rent = days * 44
# the if...elif statement below is created in order to substract the discount from rental price. As you can see here, my if...elif statement says that if you rent car for 7 or more days, you get -$30 discount and so on...
    if days >= 7:
        rent -= 35
    elif days >= 14:
        rent -= 60
    elif days >= 21:
        rent -= 99
    return rent
# the function defined below calls all the functions defined before + spending which is the array of total_cost function
def total_cost(city, days, spendings):
    return (cost_per_night(days - 1) + flight_cost(city) + car_rental(days) + spendings)

print (total_cost("Seattle", 14, 2000))