MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit= 0 
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingridients):
    for item in order_ingridients:
        if order_ingridients[item] >= resources[item]:
            print (f"Sorry there is not enough {item}")
            return False
    return True

def process_coin():
    """ask for coins and return the total"""
    print ("Please insert coin.")
    total = float(input("how many qurters: ")) * 0.25
    total += float(input("how many dimes: ")) * 0.1
    total += float(input("how many nickels: ")) * 0.05
    total += float(input("how many pennies: ")) * 0.01
    return total

def is_transaction_successful(money_recieved, drink_cost):
    """return True is money is sufficient and false if money is insufficient"""
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost , 2)
        print (f"Here's your change: {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print (f"Sorry not enough money \n") 
        return False

def make_coffe(drink_name, drink_ingredints):
    for item in drink_ingredints:
        resources[item] -= drink_ingredints[item]
    
    print (f"Here is your {drink_name} ☕ \n")


is_on = True

while is_on:
    choice = input("What would you like to have espresso, latte, cappuccino : ").lower()
    if choice == "off":
        is_on = False
    elif choice =="report":
        print (f"Water: {resources['water']}")
        print (f"Milk: {resources['milk']}")
        print (f"Coffee: {resources['coffee']}")
        print (f"Money: {profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffe(choice, drink["ingredients"])