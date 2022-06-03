from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


machine_on = True
while machine_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ")
    drink = menu.find_drink(choice)

    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        machine_on = False
    else:
        cost = drink.cost
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(cost):
            coffee_maker.make_coffee(drink)









