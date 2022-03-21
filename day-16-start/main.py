from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def get_coins():
    """returns the number of coins"""
    print("Please insert coins...")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    return (
        0.25 * quarters + 0.1 * dimes
        + 0.05 * nickles + 0.01 * pennies
    )


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