def hotel_cost(nights):
    return nights * 140

def plane_ride_cost(city):
    if city == "Dhaka":
        return 120
    elif city == "moscow":
        return 320
    elif city == "Berlin":
        return 280
    elif city == "Beijing":
        return 180
def rental_car_cost(days):
    cost = days *40
    if days >= 7:
        return cost - 50
    elif days >= 3:
        return cost - 30
    else:
        return cost
    
def trip_cost(city, days, spending_money):

    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

print("Total trip cost:", trip_cost("Dhaka", 5, 600))