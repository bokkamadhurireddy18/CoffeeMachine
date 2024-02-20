from menu import logo, MENU, resources, money
#print(logo)

def give_menu(resources, money):
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == 'off': #only for maintainers
        return False
    elif choice=='report': #only for maintainers
        report(resources, money)
        return True
    elif choice=='espresso':
        espresso(resources)
        return True
    elif choice=='latte':
        latte(resources)
        return True
    elif choice == 'cappuccino':
        cappuccino(resources)
        return True

def report(resources, money):
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}")

def espresso(resources):
    global money
    cost = MENU['espresso']['cost']
    for ingredient in MENU['espresso']['ingredients']:
        if resources[ingredient] < MENU['espresso']['ingredients'][ingredient]:
            print(f"Sorry there is no enough {ingredient}.")
            return False
    paid= count_coins(cost)
    if paid==True:
        for ingredient in MENU['espresso']['ingredients']:
            resources[ingredient]-=MENU['espresso']['ingredients'][ingredient]
        money+= cost
        print("Here is your espresso. Enjoy!")
    return (resources, money)

def latte(resources):
    global money
    cost = MENU['latte']['cost']
    for ingredient in MENU['latte']['ingredients']:
        if resources[ingredient] < MENU['latte']['ingredients'][ingredient]:
            print(f"Sorry there is no enough {ingredient}.")
            return False
    paid = count_coins(cost)
    if paid == True:
        for ingredient in MENU['latte']['ingredients']:
            resources[ingredient]-=MENU['latte']['ingredients'][ingredient]
        money+= cost
        print(f"Here is your latte. Enjoy!")
    return (resources, money)


def cappuccino(resources):
    global money
    cost = MENU['cappuccino']['cost']
    for ingredient in MENU['cappuccino']['ingredients']:
        if resources[ingredient] < MENU['cappuccino']['ingredients'][ingredient]:
            print(f"Sorry there is no enough {ingredient}.")
            return False
    paid = count_coins(cost)
    if paid == True:
        for ingredient in MENU['cappuccino']['ingredients']:
            resources[ingredient]-=MENU['cappuccino']['ingredients'][ingredient]
        money+= cost
        print("Here is your cappuccino. Enjoy!")
    return (resources, money)

def count_coins(cost):
    print(f"Please insert coins worth ${cost}:")
    quarters= int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    total_paid= quarters*0.25 + dimes*0.10 + nickels*0.05 + pennies*0.01
    if total_paid>cost:
        print(f"Here is your change ${total_paid-cost:.2f}")
        return True
    else:
        print(f"You didn't insert sufficient coins. Here is your refund ${total_paid}")
        return  False

order= True
while order:
    order = give_menu(resources, money)
