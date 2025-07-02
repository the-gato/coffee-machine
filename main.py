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

money = 0 # US dollars ($)

# TODO 4. Check that the money inserted >= cost of product.
# TODO 6. off command terminates while loop


def print_report():
    # Prints coffee machine resources

    print(f"Water: {resources["water"]}")
    print(f"Milk: {resources["milk"]}")
    print(f"Coffee: {resources["coffee"]}")
    print(f"Money: {money}")


def consume_resources(water, milk, coffee):
    """Deducts resources to simulate making coffee.

    Args:
        water_needed: Amount of water required.
        milk_needed: Amount of milk required.
        coffee_needed: Amount of coffee required.

    Raises:
        InsufficientResourceError: If any required resource is not available.
    """
    current_water = resources["water"]
    current_milk = resources["milk"]
    current_coffee = resources["coffee"]

    if current_water - water < 0:
        raise ValueError(f"Not enough water. Required: {water}ml, Available: {current_water}ml.")
    else:
        resources["water"] = current_water - water
    if current_milk - milk < 0:
        raise ValueError(f"Not enough milk. Required: {milk}ml, Available: {current_milk}ml.")
    else:
        resources["milk"] = current_milk - milk
    if current_coffee - coffee < 0:
        raise ValueError(f"Not enough coffee beans. Required: {coffee}ml, Available: {current_coffee}ml.")
    else:
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


done = False
while not done:
    answer = input("What would you like? (espresso/latte/cappuccino): ")
    coffee_selection = {}
    if answer == "espresso":
        coffee_selection = MENU["espresso"]
    elif answer == "latte":
        coffee_selection = MENU["latte"]
    elif answer == "cappuccino":
        coffee_selection = MENU["cappuccino"]
    else:
        print("Invalid input. Options are 'espresso', 'latte', 'cappuccino'")

    print("Please insert coins.")
    num_quarters = int(input("How many quarters?: "))
    num_dimes = int(input("How many dimes?: "))
    num_nickles = int(input("How many nickles?: "))
    num_pennies = int(input("How many pennies?: "))

    total = sum_coins(num_quarters, num_dimes, num_nickles, num_pennies)
    cost_float = coffee_selection["cost"]
    cost_str = str(cost_float)
    cost = Decimal(cost_str)

    water = coffee_selection["ingredients"]["water"]
    milk = coffee_selection["ingredients"]["milk"]
    coffee = coffee_selection["ingredients"]["coffee"]

    if total > cost:
        consume_resources(water, milk, coffee)
        change = calculate_change(total, cost)
        print(f"Here is ${change} in change.")
    elif total == cost:
        consume_resources(water, milk, coffee)
    else:
        print(f"Insufficient payment. Cost: ${cost:.2f}. Payment: ${total:.2f}")
