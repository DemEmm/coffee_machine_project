import os

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

RESOURCE = {
    "water": 1000,
    "coffee": 1000,
    "milk": 1000,
    "money": 10,
}


def check_price(preference, MENU, RESOURCE):
    print(f'''{preference} cost {MENU[preference]["cost"]}''')
    quarters = input("how many quarters?")
    os.system("cls")
    print(f"your total is :{int(quarters) * 0.25 }$")
    dimes = input("how many dimes?")
    os.system("cls")
    print(f"your total is :{ int(quarters) * 0.25 + int(dimes) * 0.1 }$")
    nickles = input("how many nickles?")
    os.system("cls")
    print(f"your total is :{int(quarters) * 0.25 + int(dimes) * 0.1 + int(nickles) * 0.05}$")
    pennies = input("how many pennies?")
    os.system("cls")
    total = int(quarters) * 0.25 + int(dimes) * 0.1 + int(nickles) * 0.05 + int(pennies) * 0.01
    print(f"you give {total}$")

    if total < MENU[preference]["cost"]:
        print(f'''
    Sorry that's not enough money, the cost of the product is {MENU[preference]["cost"]}$.
    Money refunded...
    ''')
        return [0, total]
    else:
        return [1, total]


def chek_drink_resource(drink, MENU, RESOURCE):
    if MENU[drink]["ingredients"]["water"] >= RESOURCE["water"]:
        return "Sorry there is not enough water"
    elif MENU[drink]["ingredients"]["milk"] >= RESOURCE["milk"]:
        return "Sorry there is not enough Milk"
    elif MENU[drink]["ingredients"]["coffee"] >= RESOURCE["coffee"]:
        return "Sorry there is not enough coffee"
    else:
        return 1


while 1:

    preference = input('''
    What would you like espresso, latte or cappuccino?
    please type:
    1 for espresso or "espresso"
    2 for latte or "latte"
    3 for cappuccino or "cappuccino"
    4 to report the resources or "report"
    5 to turn off the machine or "off"
    
    i am happily waiting for your choose:
    ''')

    os.system("cls")

    if preference == '1' or preference == 'espresso':

        preference = "espresso"

        drink_resource = chek_drink_resource(preference, MENU, RESOURCE)

        if drink_resource == 1:
            payment = check_price(preference, MENU, RESOURCE)
            if payment[0] == 1:
                RESOURCE["money"] = RESOURCE["money"] + MENU[preference]["cost"]
                RESOURCE["water"] = RESOURCE["water"] - MENU[preference]["ingredients"]["water"]
                RESOURCE["milk"] = RESOURCE["milk"] - MENU[preference]["ingredients"]["milk"]
                RESOURCE["coffee"] = RESOURCE["coffee"] - MENU[preference]["ingredients"]["coffee"]
                if payment[1]-MENU[preference]["cost"]>0 : print(f'''Here is ${payment[1]-MENU[preference]["cost"]} dollars in change''')
                print(f"“Here is your {preference}. Enjoy!”")
            elif payment[0] == 1: print(f"there is not enough money for this product you give{payment[1]} and it costs {MENU[preference]["cost"]}")
        elif drink_resource != 1:

            print(f'''{drink_resource}''')

    elif preference == '2' or preference == "latte":

        preference = "latte"
        drink_resource = chek_drink_resource(preference, MENU, RESOURCE)

        if drink_resource == 1:
            payment = check_price(preference, MENU, RESOURCE)
            if payment[0] == 1:
                RESOURCE["money"] = RESOURCE["money"] + MENU[preference]["cost"]
                RESOURCE["water"] = RESOURCE["water"] - MENU[preference]["ingredients"]["water"]
                RESOURCE["milk"] = RESOURCE["milk"] - MENU[preference]["ingredients"]["milk"]
                RESOURCE["coffee"] = RESOURCE["coffee"] - MENU[preference]["ingredients"]["coffee"]
                if payment[1]-MENU[preference]["cost"]>0 : print(f'''Here is ${payment[1]-MENU[preference]["cost"]} dollars in change''')
                print(f"“Here is your {preference}. Enjoy!")
            elif payment[0] == 1: print(f"there is not enough money for this product you give{payment[1]} and it costs {MENU[preference]["cost"]}")
        elif drink_resource != 1:

            print(f'''{drink_resource}''')

    elif preference == '3' or preference == 'cappuccino':

        preference = "cappuccino"
        drink_resource = chek_drink_resource(preference, MENU, RESOURCE)

        if drink_resource == 1:
            payment = check_price(preference, MENU, RESOURCE)
            if payment[0] == 1:
                RESOURCE["money"] = RESOURCE["money"] + MENU[preference]["cost"]
                RESOURCE["water"] = RESOURCE["water"] - MENU[preference]["ingredients"]["water"]
                RESOURCE["milk"] = RESOURCE["milk"] - MENU[preference]["ingredients"]["milk"]
                RESOURCE["coffee"] = RESOURCE["coffee"] - MENU[preference]["ingredients"]["coffee"]
                if payment[1]-MENU[preference]["cost"]>0 : print(f'''Here is ${payment[1]-MENU[preference]["cost"]} dollars in change''')
                print(f"Here is your {preference}. Enjoy!")
            elif payment[0] == 1: print(f"there is not enough money for this product you give{payment[1]} and it costs {MENU[preference]["cost"]}")
        elif drink_resource != 1:
            print(f'''{drink_resource}''')
    elif preference == '4' or preference == 'report':
        print(f'''
    the current resource values of the machine is:
    Water: {RESOURCE["water"]}ml
    Milk: {RESOURCE["milk"]}ml
    Coffee: {RESOURCE["coffee"]}g
    Money: {RESOURCE["money"]}$
    ''')
        input("press any key to return to main menu")
        os.system("cls")
    elif preference == '5' or preference == 'off':
        break
    else:
        print("sorry choose one of the proper choices")
