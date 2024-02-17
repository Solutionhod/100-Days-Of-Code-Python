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
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "profit": 0,
}


def is_transaction_successful(money_received, drink_cost):
    """Returns True whem the payment is accepted, or False is money is insufficient."""
    if money_received >= drink_cost:
        change_amount = money_received - drink_cost
        if change_amount > 0:
            print(f"Here is ${change_amount:.2f} in change.")
        resources["profit"] += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def check_resources_sufficient(order_ingredients):
    """Returns True when order can be made, False if the order ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total_coins = int(input("How many quarters?: ")) * 0.25
    total_coins += int(input("How many dimes?: ")) * 0.1
    total_coins += int(input("How many nickles?: ")) * 0.05
    total_coins += int(input("How many pennies?: ")) * 0.01
    return total_coins


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")


def get_current_resource():
    """Returns the current resources available"""
    return f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nProfit: ${resources['profit']}"


is_on = True
while is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "off":
        print("Turning off machine...\nGoodbye")
        is_on = False
    elif user_choice == "report":
        current_resource = get_current_resource()
        print(current_resource)
        is_on
    else:
        drink = MENU[user_choice]
        if check_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(user_choice, drink["ingredients"])
