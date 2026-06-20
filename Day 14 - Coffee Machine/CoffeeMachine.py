# . Process coins. 
# a. If there are sufficient resources to make the drink selected, then the program should 
# prompt the user to insert coins.  
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01 
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2 
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52 


# Stocks
stocks = {
            'water': 100, 
            'milk': 50,
            'coffee': 76, 
            'money': 3,
        }


# Espresso
espresso = {
        'water': 50, 
        'coffee': 18, 
        'milk': 0,
        'price': 2.5,
    }

# Late
latte = {
        'water': 200,  
        'coffee': 24, 
        'milk': 150,
        'price': 3,
    }


# Cappuccino
cappuccino = {
        'water': 250, 
        'coffee': 24, 
        'milk': 100,
        'price': 3.5,
    }


coffee_machine_is_on = True



while coffee_machine_is_on:
    try:
        select_option = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if select_option != 'espresso' and select_option != 'latte' and select_option != 'cappuccino' and select_option != 'off' and select_option != 'report':
            raise ValueError

    except ValueError:
        print("Please choose a valid answer!")
        continue

    def check_stocks():
        if select_option == 'espresso': 
            if stocks['water'] < espresso['water']: 
                print("​Sorry there is not enough water.")
            if stocks['coffee'] < espresso['coffee']:
                print("​Sorry there is not enough coffee.")
            if stocks['milk'] < espresso['milk']:
                print("​Sorry there is not enough milk.")
            else:
                print(f"Please insert ${espresso['price']} in coins")
                check_payment()

        if select_option == 'latte':
            if stocks['water'] < latte['water']: 
                print("​Sorry there is not enough water.")
            if stocks['coffee'] < latte['coffee']:
                print("​Sorry there is not enough coffee.")
            if stocks['milk'] < latte['milk']:
                print("​Sorry there is not enough milk.")
            else:
                print(f"Please insert ${latte['price']} in coins")
                check_payment()
               

        if select_option == 'cappuccino':
            if stocks['water'] < cappuccino['water']: 
                print("​Sorry there is not enough water.")
            if stocks['coffee'] < cappuccino['coffee']:
                print("​Sorry there is not enough coffee.")
            if stocks['milk'] < cappuccino['milk']:
                print("​Sorry there is not enough milk.")
            else:
                print(f"Please insert ${cappuccino['price']} in coins")
                check_payment()

    def check_payment():

        # Money Pot
        money_total = 2.5
        quarters_value = 0.25
        quarters_count = 6
        dimes_value = 0.10
        dimes_count = 5
        nickles_value = 0.05
        nickles_count = 8
        pennies_value = 0.01
        pennies_count = 10

        # Payment
        quarters_inserted = int(input("How many quarters have you inserted?"))
        dimes_inserted = int(input("How many dimes have you inserted?"))
        nickles_inserted = int(input("How many nickles have you inserted?"))
        pennies_inserted = int(input("How many pennies have you inserted?"))

        total_paid = (quarters_inserted * quarters_value) + (dimes_inserted * dimes_value) + (nickles_inserted * nickles_value) + (pennies_inserted * pennies_value)
        quarters_count = quarters_count + quarters_inserted
        dimes_count = dimes_count + dimes_inserted
        nickles_count = nickles_count + nickles_inserted
        pennies_count = pennies_count + pennies_inserted

        money_total = money_total + total_paid

        print(total_paid)
        print(money_total)

        if espresso['price'] <= total_paid and select_option == 'espresso':
            print("Preparing your espresso")
            stocks['money'] = stocks['money'] + total_paid
            change_total = total_paid - espresso['price']
            stocks['money'] = stocks['money']  - change_total
            print(f"Please take your {change_total}")

        if cappuccino['price'] <= total_paid and select_option == 'cappuccino':
            print("Preparing your cappuccino")
            stocks['money'] = stocks['money'] - cappuccino['price']
            change_total = total_paid - cappuccino['price']
            print(f"Please take your {change_total}")
        if latte['price'] <= total_paid and select_option == 'latte':
            print("preparing your latte")
            stocks['money'] = stocks['money'] - latte['price']
            change_total = total_paid - latte['price']
            print(f"Please take your {change_total}")



    if select_option == 'espresso':
        check_stocks()
        
        # print("Espresso")
    elif select_option == 'latte':
        check_stocks()
        # print("Latte")
    elif select_option == 'cappuccino':
        check_stocks()
        # print("Cappuccino")
    elif select_option == 'report':
        print(f"Report:\n Water: {stocks['water']} ml\n Milk: {stocks['milk']} ml \n Coffee: {stocks['coffee']} g \n Money: ${stocks['money']}")
    elif select_option == 'off':
        print("Machine is turning off, bye!")
        coffee_machine_is_on = False