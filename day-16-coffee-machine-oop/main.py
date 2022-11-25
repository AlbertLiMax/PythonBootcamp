from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_list = Menu()
coffee_maker = CoffeeMaker()
cashier = MoneyMachine()

is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
        break
    if choice == "report":
        coffee_maker.report()
        cashier.report()
        continue
    drink = menu_list.find_drink(choice)
    if drink:
        if coffee_maker.is_resource_sufficient(drink):
            if cashier.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
