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
}

profit = 0
is_on = True


def report_resources():
    """report the remaining resources"""
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${profit}')


def check_resources(flavor, resource):
    """check if resources are enough to make coffee based on the chosen flavor"""
    if resources[resource] - MENU[flavor]["ingredients"][resource] < 0:
        print(f'Sorry there is not enough {resource}.')
        return False
    else:
        return True


def update_resources(flavor):
    """update remain resources based on the chosen flavor"""
    global profit
    for resource in resources:
        if MENU[flavor]["ingredients"].get(resource):
            resources[resource] -= MENU[flavor]["ingredients"][resource]

    profit += MENU[flavor]["cost"]


def transaction_processing(flavor):
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    if total < MENU[flavor]["cost"]:
        print("Sorry that's not enough money")
        return
    elif total > MENU[flavor]["cost"]:
        change = total - MENU[flavor]["cost"]
        print(f"Here is ${change:.1f} in change.")

    print(f"Here is your {flavor} ☕. Enjoy!")
    update_resources(flavor)


while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "report":
        report_resources()
    elif choice == "latte" or choice == "cappuccino" or choice == "espresso":
        result = True
        for resource in MENU[choice]["ingredients"]:
            if MENU[choice]["ingredients"].get(resource):
                result &= check_resources(choice, resource)
        if result:
            transaction_processing(choice)
    elif choice == "off":
        is_on = False
    else:
        print(f"There is no {choice} flavor")
