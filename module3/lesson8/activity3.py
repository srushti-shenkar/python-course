#define a function called hotel_cost with one arguement night as input 
def hotel_cost(nights):
    return 140*nights
#define a fucntion called plane_ride_cost that takes a string,city as input
def plane_ride_cost(city):
    if "Charlotte"==city:
        return 183
    elif "Tampa"==city:
        return 220
    elif"Pittsburgh"==city:
        return 222
    elif"Los Angeles"==city:
        return 475
    
#Define a function called rental_car_cost with an arguement called days
def rental_car_cost(days):
    if days>=7: 
        return 40*days-50
    elif days>=3:
        return 40*days-20
    else:
        return 40*days
    
#define a fucntion called trip cost with arguement day,money and city
def trip_cost(city,days,spending_money):
    return rental_car_cost(days)+hotel_cost(days)+plane_ride_cost(city)+spending_money
print(" cost of car rental:",rental_car_cost(5))
print("cost of plane ride:",plane_ride_cost("Los Angeles"))
print("cost of a hotel room:",hotel_cost(7))
print("total cost of the trip:",trip_cost("Los Angeles",7,500))
print(trip_cost("Tampa",6,500))

    
    