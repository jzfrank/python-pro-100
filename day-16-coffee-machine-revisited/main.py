from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


if __name__ == "__main__":
    coffee_maker = CoffeeMaker()
    my_menu = Menu()
    my_money_machine = MoneyMachine()
    while True:
        user_request = input("​What would you like? (espresso/latte/cappuccino): ")
        print(user_request)
        if user_request == "off":
            print("Machine stops.")
            break
        elif user_request == "report":
            coffee_maker.report()
            my_money_machine.report()
        else:
            coffee = my_menu.find_drink(user_request)
            # check resources sufficient
            if not coffee_maker.is_resource_sufficient(coffee):
                continue
            # process coins
            my_money_machine.make_payment(coffee.cost)