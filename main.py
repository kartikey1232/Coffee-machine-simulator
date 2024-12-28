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
money=0.0
def price():
    print(f"Espresso: {MENU['espresso']['cost']}\nLatte: {MENU['latte']['cost']}\nCappuccino: {MENU['cappuccino']['cost']}")
def isSuff_espresso(item):
        if resources["water"] < MENU[item]["ingredients"]["water"]:
            print("Sorry there is not enough water")
            return -1
        elif resources["coffee"] < MENU[item]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee")
            return -1
        else:
            resources["water"]=resources["water"]-MENU[item]["ingredients"]["water"]
            resources["coffee"] = resources["coffee"] - MENU[item]["ingredients"]["coffee"]
            return 0
def isSufficient(item):
    if resources["milk"] < MENU[item]["ingredients"]["milk"] :
        print("Sorry there is not enough milk")
        return -1
    elif resources["water"] < MENU[item]["ingredients"]["water"] :
        print("Sorry there is not enough water")
        return -1
    elif resources["coffee"] < MENU[item]["ingredients"]["coffee"] :
        print("Sorry there is not enough coffee")
        return -1
    else:
        resources["water"] = resources["water"] - MENU[item]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU[item]["ingredients"]["coffee"]
        resources["milk"]=resources["milk"]-MENU[item]["ingredients"]["milk"]
        return 0
def display_message(choice,sum):
    if MENU[choice]["cost"] > sum:
        print("Sorry that's not enough money. Money refunded.")
    else:
        change=sum-MENU[choice]["cost"]
        change=round(change,2)
        print(f"Here is ${change} in change.")
        print(f"Here is your {choice}.Enjoy!")
        return MENU[choice]["cost"]
def insert_coins(u_choice):
    print("Please insert coins")
    quarter=int(input("how many quarters?: "))*0.25
    dimes=int(input("how many dimes?: "))*0.10
    nickles=int(input("how many nickles?: "))*0.05
    penny=int(input("how many pennies: "))*0.01
    total_sum=quarter+dimes+nickles+penny
    return display_message(u_choice,total_sum)
def report():
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}")
while True:
    user_choice=input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        print("The machine is turned off! Thank you.")
        break
    elif user_choice == "report":
        report()
    elif user_choice == "espresso":
        check=isSuff_espresso(user_choice)
        if check == -1:
            continue
        else:
            money=money+insert_coins(user_choice)
    elif user_choice == "latte":
        check=isSufficient(user_choice)
        if check == -1:
            continue
        else:
            money=money+insert_coins(user_choice)
    elif user_choice == "cappuccino":
        check=isSufficient(user_choice)
        if check == -1:
            continue
        else:
            money=money+insert_coins(user_choice)
    elif user_choice == "price":
        price()
    else:
        print("Invalid choice! Try again")


































