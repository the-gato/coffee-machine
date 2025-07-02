# coffee-machine
A coffee machine program. This program prompts users to select a drink (espresso, latte, cappuccino), processes coin payments, checks for sufficient resources, and dispenses the chosen beverage.

---

## Getting Started

Follow these steps to get the coffee machine program up and running on your local machine.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YourUsername/coffee-machine.git](https://github.com/the-gato/coffee-machine.git)
    ```
2.  **Navigate into the project directory:**
    ```bash
    cd coffee-machine
    ```
3.  **Run the program:**
    ```bash
    python main.py
    ```

---

## Coffee Machine Operation

Once the program is running, it will continuously prompt you with "What would you like? (espresso/latte/cappuccino):".

### Drink Options

Choose from three delicious beverages:
* **espresso**
* **latte**
* **cappuccino**

The machine will check if it has enough ingredients before prompting for payment. If resources are insufficient, it will notify you.

### Payment Process

After selecting a drink (and if resources are sufficient), you will be prompted to insert coins. The machine accepts:
* **Pennies** ($0.01)
* **Nickels** ($0.05)
* **Dimes** ($0.10)
* **Quarters** ($0.25)

The program will calculate the total value of inserted coins and handle change or insufficient funds.

### Special Commands

* **Shutdown Machine:**
    Type `off` at the prompt to gracefully end program execution. This is a keyword for maintainers.

* **Print Report:**
    Type `report` at the prompt to display the current resource levels:
    * Water
    * Milk
    * Coffee
    * Money (accumulated profit from sales)

---
