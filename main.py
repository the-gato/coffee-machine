from decimal import Decimal

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

money = Decimal('0') # US dollars ($)


def handle_transaction(num_total, num_cost):
    """

    Args:
        num_total: total in USD ($) from customer
        num_cost: cost of coffee in USD($)

    Returns:
        change in USD ($)

    """

    if num_total > num_cost:

        return  calculate_change(num_total, num_cost)

    elif num_total == num_cost:
        return Decimal('0')

    else:
        raise ValueError(f"Insufficient payment. Cost: ${cost:.2f}. Payment: ${total:.2f}")


def determine_cost_and_consumption(coffee_choice, coffee_key=None):
    """

    Args:
        coffee_choice: a dict containing ingredients and cost of menu selection
        coffee_key: coffee name

    Returns:
        tuple
            cost
            milk
            water
            coffee beans
            list
                the key (coffee)

    """
    cost_float = coffee_choice["cost"]
    cost_str = str(cost_float)
    cost = Decimal(cost_str)

    water = coffee_choice["ingredients"]["water"]
    milk = 0 if coffee_key == "espresso" else coffee_choice["ingredients"]["milk"]
    coffee = coffee_choice["ingredients"]["coffee"]
    key_list = list(coffee_choice)
    return (cost, water, milk, coffee, key_list)

def insert_coins():
    """asks user to insert coins.

    Returns: sum of coins

    """
    print("Please insert coins.")
    num_quarters = int(input("How many quarters?: "))
    num_dimes = int(input("How many dimes?: "))
    num_nickles = int(input("How many nickles?: "))
    num_pennies = int(input("How many pennies?: "))

    return sum_coins(num_quarters, num_dimes, num_nickles, num_pennies)


def add_money(current_total, amount_to_add):
    """
    Adds a specified amount of money to a current total and returns the new total.

    Args:
        current_total (Decimal): The initial total amount.
        amount_to_add (Decimal): The amount of money to add.

    Returns:
        Decimal: The new total after adding the amount.
    """
    new_total = current_total + amount_to_add
    return new_total

def print_report(current_money):
    """
    Args:
        current_money:
            The current amount of money in the coffee maker.
    """

    print(f"Water: {resources["water"]}")
    print(f"Milk: {resources["milk"]}")
    print(f"Coffee: {resources["coffee"]}")
    print(f"Money: {current_money}")


def consume_resources(water, milk, coffee):
    """Deducts resources to simulate making coffee.

    Args:
        water_needed: Amount of water required.
        milk_needed: Amount of milk required.
        coffee_needed: Amount of coffee required.
    """
    current_water = resources["water"]
    current_milk = resources["milk"]
    current_coffee = resources["coffee"]

    resources["water"] = current_water - water
    resources["milk"] = current_milk - milk
    resources["coffee"] = current_coffee - coffee


def sum_coins(num_quarters=None, num_dimes=None, num_nickels=None, num_pennies=None):
    """ calculate the sum of the coins

    Args:
        num_quarters:
            number of quarters
        num_dimes:
            number of dimes
        num_nickels:
            number of nickels
        num_pennies:
            number of pennies

    Returns:
        Sum of the coins.

    """

    # define the coin values using Decimal
    # strings are used to avoid initial floating-point inaccuracies

    quarter_dec = Decimal('0.25')
    dime_dec = Decimal('0.10')
    nickel_dec = Decimal('0.05')
    penny_dec = Decimal('0.01')

    # Convert None counts to 0 for calculation
    actual_quarters = num_quarters if num_quarters is not None else 0
    actual_dimes = num_dimes if num_dimes is not None else 0
    actual_nickels = num_nickels if num_nickels is not None else 0
    actual_pennies = num_pennies if num_pennies is not None else 0

    return (actual_quarters * quarter_dec) +  (actual_dimes * dime_dec) + (actual_nickels * nickel_dec) + (
        actual_pennies * penny_dec)


def calculate_change(payment, cost):
    """ calculates the change owned to the customer if they pay more than the menu item costs

    Args:
        payment:
            Decimal value in USD. eg 2.50
        cost:
            cost of the menu item in Decimal value (USD) eg 2.25

    Returns:
        The difference between payment and cost. eg .25

    Raises:
        ValueError: If the payment is not > cost

    """

    if payment > cost:
        return payment - cost
    elif payment == cost:
        return Decimal('0.00')
    else:
        raise ValueError("Payment is not greater than cost.")

def has_resources(current_water, current_milk, current_coffee, ingredients_dict, coffee_key=None):
    """check resources for making coffee

    Args:
        current_water:
            current water in mls
        current_milk:
            current milk in mls
        current_coffee:
            current coffee beans in grams
        ingredients_dict:
            dictionary of coffee ingredients
        coffee_key:
            The coffee key from the menu dict

        Returns:
            true if sufficient resources are present
    """
    required_water = ingredients_dict["water"]
    required_milk = 0 if coffee_key == "espresso" else ingredients_dict["milk"]
    required_coffee = ingredients_dict["coffee"]

    has_enough_water = current_water >= required_water
    if not has_enough_water:
        print(f"Not enough water. Available: {current_water}. Required: {required_water}")

    has_enough_coffee = current_coffee >= required_coffee
    if not has_enough_coffee:
        print(f"Not enough coffee beans. Available: {current_coffee}. Required: {required_coffee}")

    if coffee_key != "espresso":
        has_enough_milk = current_milk >= required_milk
        if not has_enough_milk:
            print(f"Not enough milk. Available: {current_milk}. Required: {required_milk}")

    if coffee_key != "espresso":
        return has_enough_milk and has_enough_coffee and has_enough_water

    else:
        return has_enough_water and has_enough_coffee

coffee_key = ""
done = False
while not done:
    answer = input("What would you like? (espresso/latte/cappuccino): ")
    coffee_selection = {}
    if answer == "espresso":
        coffee_selection = MENU["espresso"]
        coffee_key = "espresso"
        if not has_resources(current_water=resources["water"], current_milk=resources["milk"],
                             current_coffee=resources["coffee"], ingredients_dict=coffee_selection["ingredients"],
                             coffee_key="espresso"):
            continue

        total = insert_coins()

        cost_and_consumption = determine_cost_and_consumption(coffee_selection, coffee_key)
        cost = cost_and_consumption[0]
        water = cost_and_consumption[1]
        milk = cost_and_consumption[2]
        coffee = cost_and_consumption[3]

        try:
            change = handle_transaction(total, cost)
            consume_resources(water, milk, coffee)
            money = add_money(money, cost)
            if change > Decimal('0'):
                print(f"Here is ${change} in change.")

            print(f"Here is your {coffee_key} ☕ Enjoy!")
        except ValueError as e:
            print(f"{e}")

    elif answer == "latte":
        coffee_selection = MENU["latte"]
        coffee_key = "latte"
        total = insert_coins()
        cost_and_consumption = determine_cost_and_consumption(coffee_selection)
        cost = cost_and_consumption[0]
        water = cost_and_consumption[1]
        milk = cost_and_consumption[2]
        coffee = cost_and_consumption[3]

        change = handle_transaction(total, cost)
        consume_resources(water, milk, coffee)
        if change > Decimal('0'):
            print(f"Here is ${change} in change.")
            print(f"Here is your {coffee_key} ☕ Enjoy!")
        else:
            print(f"Here is your {coffee_key} ☕ Enjoy!")

    elif answer == "cappuccino":
        coffee_selection = MENU["cappuccino"]
        coffee_key = "capuccino"
        total = insert_coins()
        cost_and_consumption = determine_cost_and_consumption(coffee_selection)
        cost = cost_and_consumption[0]
        water = cost_and_consumption[1]
        milk = cost_and_consumption[2]
        coffee = cost_and_consumption[3]

        change = handle_transaction(total, cost)
        consume_resources(water, milk, coffee)
        if change > Decimal('0'):
            print(f"Here is ${change} in change.")
            print(f"Here is your {coffee_key} ☕ Enjoy!")
        else:
            print(f"Here is your {coffee_key} ☕ Enjoy!")

    elif answer == "done":
        break
    elif answer == "report":
        print_report(money)
    else:
        print("Invalid input. Options are 'espresso', 'latte', 'cappuccino'")





