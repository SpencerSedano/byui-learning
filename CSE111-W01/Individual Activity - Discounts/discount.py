"""
Problem Statement
You work for a retail store that wants to increase sales on Tuesday and Wednesday, which are the store’s slowest sales days. On Tuesday and Wednesday, if a customer’s subtotal is $50 or greater, the store will discount the customer’s subtotal by 10%.

If the subtotal is $50 or greater and today is Tuesday or Wednesday, your program must subtract 10% from the subtotal. Your program must then compute the total amount due by adding sales tax of 6% to the subtotal. Your program must print the discount amount if applicable, the sales tax amount, and the total amount due.

"""

from datetime import datetime

d = datetime.now()
""" print(datetime.weekday(d)) """

tax = 0.06

number = 1

while number != 0:
    user_input = float(input("Please enter the subtotal: "))
    if user_input >= 50:
        if datetime.weekday(d) == 1 or datetime.weekday(d) == 2:
            user_discount = user_input * 0.10
            user_subtotal = user_input - user_discount
            user_tax = user_subtotal * tax
            user_total = user_subtotal + user_tax
            print(f"Discount amount: {user_discount:.2f}")
            print(f"Sales tax amount: {user_tax:.2f}")
            print(f"Total: {user_total:.2f}")
    else:
        remaining = 50 - user_input
        user_tax = user_input * tax
        user_total = user_input + user_tax
        print(f"If you buy {remaining} more, you can get 10% discount!")
        print(f"Sales tax amount: {user_tax:.2f}")
        print(f"Total: {user_total:.2f}")
    number = user_input
