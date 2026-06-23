# Coffee machine program
# The machine checks ingredients, accepts coins, gives change,
# keeps track of stock, and prints a report.


# Machine stock
stocks = {
    'water': 100,
    'milk': 50,
    'coffee': 76,
    'money': 3,
    'quarters_count': 6,
    'dimes_count': 5,
    'nickles_count': 8,
    'pennies_count': 10,
}


# Drinks available
espresso = {
    'water': 50,
    'coffee': 18,
    'milk': 0,
    'price': 2.5,
}

latte = {
    'water': 200,
    'coffee': 24,
    'milk': 150,
    'price': 3,
}

cappuccino = {
    'water': 250,
    'coffee': 24,
    'milk': 100,
    'price': 3.5,
}


def print_report():
    print(
            f"\nReport:"
            f"\nWater: {stocks['water']} ml"
            f"\nMilk: {stocks['milk']} ml"
            f"\nCoffee: {stocks['coffee']} g"
            f"\nDimes: {stocks['dimes_count']}"
            f"\nQuarters: {stocks['quarters_count']}"
            f"\nNickles: {stocks['nickles_count']}"
            f"\nPennies: {stocks['pennies_count']}"
            f"\nTotal: ${stocks['money']:.2f}\n"
    )



def check_resources(drink):
    """Checks whether the machine has enough ingredients."""

    if stocks['water'] < drink['water']:
        print("Sorry, there is not enough water.")
        return False

    if stocks['coffee'] < drink['coffee']:
        print("Sorry, there is not enough coffee.")
        return False

    if stocks['milk'] < drink['milk']:
        print("Sorry, there is not enough milk.")
        return False

    return True


def check_payment(drink, drink_name):
    """Collects payment, works out change, and completes the order."""

    # Coin values
    quarters_value = 0.25
    dimes_value = 0.10
    nickles_value = 0.05
    pennies_value = 0.01

    try:
        # Ask the user how many coins they inserted
        quarters_inserted = int(input("How many quarters have you inserted? "))
        dimes_inserted = int(input("How many dimes have you inserted? "))
        nickles_inserted = int(input("How many nickles have you inserted? "))
        pennies_inserted = int(input("How many pennies have you inserted? "))

        # Prevent negative numbers
        if (
            quarters_inserted < 0
            or dimes_inserted < 0
            or nickles_inserted < 0
            or pennies_inserted < 0
        ):
            print("Please enter a positive number of coins.")
            return

    except ValueError:
        print("Please enter whole numbers only.")
        return

    # Calculate how much the customer paid
    total_paid = round(
        (quarters_inserted * quarters_value)
        + (dimes_inserted * dimes_value)
        + (nickles_inserted * nickles_value)
        + (pennies_inserted * pennies_value),
        2
    )

    # Temporarily add the customer's coins to the machine
    stocks['quarters_count'] += quarters_inserted
    stocks['dimes_count'] += dimes_inserted
    stocks['nickles_count'] += nickles_inserted
    stocks['pennies_count'] += pennies_inserted

    # Refund the customer if they did not pay enough
    if total_paid < drink['price']:
        print(f"Sorry, that is not enough money. ${total_paid:.2f} refunded.")

        stocks['quarters_count'] -= quarters_inserted
        stocks['dimes_count'] -= dimes_inserted
        stocks['nickles_count'] -= nickles_inserted
        stocks['pennies_count'] -= pennies_inserted
        return

    # Work out the amount of change needed
    change_total = round(total_paid - drink['price'], 2)

    print(f"Payment received: ${total_paid:.2f}")
    print(f"Change due: ${change_total:.2f}")

    # Counters used to show which coins are returned
    change_number_quarters = 0
    change_number_dimes = 0
    change_number_nickles = 0
    change_number_pennies = 0

    # Give the largest coins first while the machine has them
    while change_total > 0:
        if change_total >= quarters_value and stocks['quarters_count'] > 0:
            change_total = round(change_total - quarters_value, 2)
            stocks['quarters_count'] -= 1
            change_number_quarters += 1

        elif change_total >= dimes_value and stocks['dimes_count'] > 0:
            change_total = round(change_total - dimes_value, 2)
            stocks['dimes_count'] -= 1
            change_number_dimes += 1

        elif change_total >= nickles_value and stocks['nickles_count'] > 0:
            change_total = round(change_total - nickles_value, 2)
            stocks['nickles_count'] -= 1
            change_number_nickles += 1

        elif change_total >= pennies_value and stocks['pennies_count'] > 0:
            change_total = round(change_total - pennies_value, 2)
            stocks['pennies_count'] -= 1
            change_number_pennies += 1

        else:
            print("Sorry, the machine cannot provide exact change.")

            # Put back any coins already selected as change
            stocks['quarters_count'] += change_number_quarters
            stocks['dimes_count'] += change_number_dimes
            stocks['nickles_count'] += change_number_nickles
            stocks['pennies_count'] += change_number_pennies

            # Return the customer's inserted coins
            stocks['quarters_count'] -= quarters_inserted
            stocks['dimes_count'] -= dimes_inserted
            stocks['nickles_count'] -= nickles_inserted
            stocks['pennies_count'] -= pennies_inserted
            return

    # The purchase is successful, so update machine money and ingredients
    stocks['money'] += drink['price']
    stocks['water'] -= drink['water']
    stocks['milk'] -= drink['milk']
    stocks['coffee'] -= drink['coffee']

    print(f"Preparing your {drink_name}.")
    print(f"Please take your {drink_name}.")

    print(
        f"Return change:\n"
        f"Quarters: {change_number_quarters}\n"
        f"Dimes: {change_number_dimes}\n"
        f"Nickles: {change_number_nickles}\n"
        f"Pennies: {change_number_pennies}"
    )


coffee_machine_is_on = True

while coffee_machine_is_on:
    select_option = input(
        "What would you like? (espresso/latte/cappuccino): "
    ).lower()

    # Turn off the machine
    if select_option == 'off':
        print("Machine is turning off, bye!")
        coffee_machine_is_on = False

    # Print the current machine stock
    elif select_option == 'report':
        print_report()

    # Espresso order
    elif select_option == 'espresso':
        if check_stocks(espresso):
            print(f"Please insert ${espresso['price']:.2f} in coins")
            check_payment(espresso, 'espresso')

    # Latte order
    elif select_option == 'latte':
        if check_stocks(latte):
            print(f"Please insert ${latte['price']:.2f} in coins")
            check_payment(latte, 'latte')

    # Cappuccino order
    elif select_option == 'cappuccino':
        if check_stocks(cappuccino):
            print(f"Please insert ${cappuccino['price']:.2f} in coins")
            check_payment(cappuccino, 'cappuccino')

    # Invalid menu choice
    else:
        print("Please choose a valid answer!")