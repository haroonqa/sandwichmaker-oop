class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        
        print("Please insert coins.")
        total = int(input("How many quarters?: ")) * 0.25
        total += int(input("How many nickels?: ")) * 0.05
        total += int(input("How many half dollars?: ")) * 0.50
        total += int(input("How many dollars?: ")) * 1.00
        return total

        
    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
    

        if coins >= cost:
            change = coins - cost
            print(f"Here is ${change} in change")
            return True
        else:
            print("Sorry, you do not have enough money.")
            return False
