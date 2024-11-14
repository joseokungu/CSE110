'''
Author: Jose Okitandende Okungu

Purpose: Write a program that uses variables and expressions to accomplish a meaningful task.
'''
#These is for both meal prices and stores in variables using the proper data type (for example: float).
#These for both quantities of people and stores in variables using the proper data type (for example. int).

child_meal = float(input("What is the price of a child's meal? "))
adult_meal = float(input("What is the price of a adult's meal? "))
num_of_children = int(input ("How many children are there? "))
num_of_adult = int(input ("How many adults are there? "))
print()

#All computed values are displayed with proper formatting (currency symbol $ and 2 decimal places)
sub_total = num_of_children * child_meal + adult_meal * num_of_adult
print((f"Subtotal: ${sub_total:.2f}"))
print()

tax_rate = float(input("What is the sales tax rate? "))
sales_tax = sub_total * tax_rate /100
Total = sub_total + sales_tax

print((f"Sales Tax: ${sales_tax}"))
print((f"Total is: ${Total}"))
print()

payment_amount = float(input("What is the payment amount? "))
change = payment_amount - Total
print((f"Change: ${change:.2f}"))