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
    },
    "report": {
        "ingredients": {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        },
        "cost": 0,
    }
}


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

def is_enough(required):
    for key in required:
        if required[key] > resources[key]:
            print(f"Sorry there is not enough {key}.")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    amount = int(input("how many quarters?: ")) * 0.25
    amount += int(input("how many dimes?: ")) * 0.1
    amount += int(input("how many nickles?: ")) * 0.05
    amount += int(input("how many pennies?: ")) * 0.01
    return amount

def transaction(amount_collect, drink_cost):
    global money
    if amount_collect >= drink_cost:
        change = round(amount_collect - drink_cost, 2)
        print(f"Here is ${change} in change.")
        money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, drink):
    print(f"Here is your {drink_name} ☕️. Enjoy!")
    for key in drink:
        resources[key] -= drink[key]

def machine():
    turn_off = False
    while not turn_off:
        choice = input(' What would you like? (espresso/latte/cappuccino): ').lower()
        if choice == 'off':
            turn_off = True
        elif choice == 'report':
            print(f'Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${money}')
        else:
            drink = MENU[choice]
            if is_enough(drink["ingredients"]):
                amount_collect = process_coins()
                if transaction(amount_collect, drink["cost"]):
                    make_coffee(choice, drink["ingredients"])

machine()