import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()

def main():
    is_on = True
    while is_on:
        choice = input("What size sandwich would you like? (small/medium/large): ").lower()
        
        if choice in recipes:
            sandwich = recipes[choice]
            ingredients = sandwich["ingredients"]
            cost = sandwich["cost"]

            # Check if there are enough resources to make the sandwich
            if sandwich_maker_instance.check_resources(ingredients):
                print(f"The cost of a {choice} sandwich is ${cost}.")
                
                # Process coins
                coins = cashier_instance.process_coins()
                
                # Check if the transaction was successful
                if cashier_instance.transaction_result(coins, cost):
                    sandwich_maker_instance.make_sandwich(choice, ingredients)
                else:
                    print("Transaction failed. Not enough money.")
                    
        else:
            print("Sorry, we don't have that size.")
        
        if input("Would you like another sandwich? (yes/no): ").lower() == "no":
            is_on = False

if __name__ == "__main__":
    main()