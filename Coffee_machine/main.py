from source_data import MENU
from source_data import resources

# >>> Basic settings <<<


# >>> Function <<<
def report(data):
    print(f"Water: {data['water']}")
    print(f"Milk: {data['milk']}")
    print(f"Coffee: {data['coffee']}")

def coins():
    print("Prosím vložte mince 1, 2, 5, 10, 20, 50")

# >>> Machine code <<<
user_choice = input("Co byste dal/a? (espresso/latte/cappuccino): ")

if user_choice == "report":
    report(resources)
