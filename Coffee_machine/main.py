from source_data import MENU
from source_data import resources

# >>> Basic settings <<<


# >>> Function <<<
def report(data):
    print(f"Water: {data['water']}")
    print(f"Milk: {data['milk']}")
    print(f"Coffee: {data['coffee']}")

def coins():
    print("Please insert coins 1, 2, 5, 10, 20, 50")
    kc1 = int(input("How many CZK 1 do you want to deposit? "))
    kc2 = int(input("How many CZK 2 do you want to deposit? ")) * 2
    kc5 = int(input("How many CZK 5 do you want to deposit? ")) * 5
    kc10 = int(input("How many CZK 10 do you want to deposit? ")) * 10
    kc20 = int(input("How many CZK 20 do you want to deposit? ")) * 20
    kc50 = int(input("How many CZK 50 do you want to deposit? ")) * 50
    amount = kc1 + kc2 + kc5 + kc10 + kc20 +kc50
    print(f"Total insert amount: CZK {amount}")
    return amount


# >>> Machine code <<<
user_choice = input("Co byste dal/a? (espresso/latte/cappuccino): ")

if user_choice == "report":
    report(resources)
