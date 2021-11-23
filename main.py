from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()
item = MenuItem
coffee_program = True

while coffee_program:
    drink = input(f"What would you like to drink? Type: {menu.get_items()}")

    if drink == "report":
        coffee.report()
        money.report()
    else:
        drink = menu.find_drink(drink)

        if coffee.is_resource_sufficient(drink):

            if money.make_payment(drink.cost):

                coffee.make_coffee(drink)
