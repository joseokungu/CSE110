"""
Author Jose Okitandende
"""
print("Welcome to the Shopping Cart Program!")
print()
print("""
    Please select one of the followig:
    1. Add item
    2. View Cart
    3. Remove item
    4. Computer total
    5. Quit
""")

shopping_cart = []
prices = []

option = int(input("Please enter an action: "))

while option != 5 and option != "Quit":
    if option == 1:
        item = input("\nWhat item would you like to add? ")
        shopping_cart.append(item)
        print(f"\n'{item}' has been added to the cart.")
        print("""
    Please select one of the followig:
    1. Add item
    2. View Cart
    3. Remove item
    4. Computer total
    5. Quit
""")
        
    elif option == 2:
        print("\nThe contens of the shopping cart are: ")
        for item in range(len(shopping_cart)):
            print(f"\n {shopping_cart[item]} ")
        print("""
    Please select one of the followig:
    1. Add item
    2. View Cart
    3. Remove item
    4. Computer total
    5. Quit
""")
    elif option == 3:
        remove_item = int(input("\n Please, which item would you like to remove?")) -1
        del(shopping_cart[remove_item] )
        del(prices[remove_item])
        print(f"\n{remove_item}. Item removed")
        print("""
    Please select one of the followig:
    1. Add item
    2. View Cart
    3. Remove item
    4. Computer total
    5. Quit
""")
    elif option == 4:
        sum = 0
        for number in prices:
            sum += number
        print(f"\nThe total price of the items in the shopping cart is ${sum:.2f}")
        print("""
    Please select one of the followig:
    1. Add item
    2. View Cart
    3. Remove item
    4. Computer total
    5. Quit
""")
    option = int(input("\nPlease enter an action "))
else:
    print("\nThank you. Goodbye.")                        