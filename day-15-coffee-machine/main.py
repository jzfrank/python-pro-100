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


def generate_report(resources, money):
    print("The report of the machine:")
    print(f"water: {resources['water']}ml")
    print(f"milk: {resources['milk']}ml")
    print(f"coffee: {resources['coffee']}g")
    print(f"money: ${money}")


def resource_is_sufficient(coffee, resources):
    """Return a boolean: if the resource is enough to make coffee"""
    is_sufficient = True
    for key, val in coffee["ingredients"].items():
        if val > resources[key]:
            is_sufficient = False
            print(f"Sorry there is not enough {key}")
    return is_sufficient


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


def reduce_from(coffee, resources):
    for key, val in coffee["ingredients"].items():
        resources[key] -= val

if __name__ == "__main__":
    money = 0
    while True:
        user_request = input("​What would you like? (espresso/latte/cappuccino): ")
        if user_request == "off":
            print("Machine stops.")
            break
        elif user_request == "report":
            generate_report(resources, money)
        else:
            coffee = MENU[user_request]
            # check resources sufficient
            if not resource_is_sufficient(coffee, resources):
                continue
            # process coins
            coin = get_coins()
            if coin < coffee['cost']:
                print("Sorry that's not enough money. Money refunded.")
                continue
            else:
                change = round(coin - coffee['cost'], 2)
                print(f"Here is ${change} dollars in change")
                reduce_from(coffee, resources)
                money += coffee['cost']
                print(f"Here is your coffee ☕️ {user_request}")