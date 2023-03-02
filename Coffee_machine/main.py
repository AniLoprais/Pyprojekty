from source_data import MENU
from source_data import resources

# >>> Basic settings <<<
espresso_price = MENU["espresso"]["cost"]
latte_price = MENU["latte"]["cost"]
cappuccino_price = MENU["cappuccino"]["cost"]

# >>> Function <<<
def report(data):
    print(f"Water: {data['water']}")
    print(f"Milk: {data['milk']}")
    print(f"Coffee: {data['coffee']}")

def coins():
    print("Prosím vložte mince 1, 2, 5, 10, 20, 50")
    kc1 = int(input("Kolik 1 kč chcete vložit? "))
    kc2 = int(input("Kolik 2 kč chcete vložit? ")) * 2
    kc5 = int(input("Kolik 5 Kč chcete vložit? ")) * 5
    kc10 = int(input("Kolik 10 Kč chcete vložit? ")) * 10
    kc20 = int(input("Kolik 20 Kč chcete vložit? ")) * 20
    kc50 = int(input("Kolik 50 Kč chcete vložit? ")) * 50
    suma = kc1 + kc2 + kc5 + kc10 + kc20 +kc50
    print(f"Celkem jste vložili: {suma} Kč")
    return suma

def calculate_change(user_sum_coins, price):
    refund = user_sum_coins - price
    if refund >= 0:
        print("Nápoj se připravuje.")
        if refund > 0:
            print(f"Zde jsou peníze navíc zpět: {refund} Kč")

    else:
        print(f"Nevhodili jste dostatek mincí. Ještě je zapotřebí vložit {price - user_sum_coins} Kč")

def fill_in_ingredients():
    return resources

def consumption_ingredients(name_of_drink, ingredients):
    ingredients["water"] = ingredients["water"] - MENU[name_of_drink]["ingredients"]["water"]
    ingredients["milk"] = ingredients["milk"] - MENU[name_of_drink]["ingredients"]["milk"]
    ingredients["coffee"] = ingredients["coffee"] - MENU[name_of_drink]["ingredients"]["coffee"]
    print(f"Zbylé ingredience: {ingredients}")


def calculate_ingredients(drink_name):
    if drink_name == "espresso":
       consumption_ingredients(drink_name, rest_of_ingredients)
    elif drink_name == "latte":
        consumption_ingredients(drink_name, rest_of_ingredients)
    elif drink_name == "cappuccino":
        consumption_ingredients(drink_name, rest_of_ingredients)


def ingredients_checker(in_water, in_milk, in_coffee):
    if in_water < 0:
        print("Nedostatek ingrediencí. Zavolejte servis.")
        return False
    elif in_milk < 0:
        print("Nedostatek ingrediencí. Zavolejte servis.")
        return False
    elif in_coffee < 0:
        print("Nedostatek ingrediencí. Zavolejte servis.")
        return False
    else:
        print("Na váš nápoj máme dostatek ingrediencí.")
        return True


# >>> Machine code <<<

# We load the original amount of ingredients
rest_of_ingredients = fill_in_ingredients()

lets_continue = True

while(lets_continue):
    # User choice - what kind of drink he wants
    user_choice = input("Co byste si dal/a? (espresso/latte/cappuccino): ")

    # Calculating how many ingredients are left
    calculate_ingredients(user_choice)

    # Ingredients check in machine
    if user_choice != "report":
        lets_continue = ingredients_checker(rest_of_ingredients["water"], rest_of_ingredients["milk"], rest_of_ingredients["coffee"])

    # Should the code continue?
    if lets_continue == False:
        break

    # Control report
    if user_choice == "report":
        report(rest_of_ingredients)

    # The main code of the machine
    if user_choice == "espresso":
        print(f"Cena espressa je: {espresso_price} Kč")
        sum = coins()
        calculate_change(sum, espresso_price)

    elif user_choice == "latte":
        print(f"Cena latte je: {latte_price} Kč")
        sum = coins()
        calculate_change(sum, latte_price)

    elif user_choice == "cappuccino":
        print(f"Cena cappuccina je: {cappuccino_price} Kč")
        sum = coins()
        calculate_change(sum, cappuccino_price)
