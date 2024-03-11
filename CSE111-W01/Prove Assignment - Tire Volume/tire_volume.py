"""
Problem Statement
Many companies wish to understand the needs and wants of their customers more deeply so the company can create products that fill those needs and wants. One way to understand customers more deeply is to record the values entered by customers while they are using a program and then to analyze those values. One common way to record values is for a program to store them in a file.
"""

import math
from datetime import datetime

tire_width = float(input("Enter the width of the tire in mm (ex 205):"))
tire_ratio = float(input("Enter the aspect ratio of the tire (ex 60):"))
tire_diameter = float(input("Enter the diameter of the wheel in inches (ex 15):"))

volume_calc = (
    math.pi
    * tire_width**2
    * tire_ratio
    * (tire_width * tire_ratio + 2540 * tire_diameter)
    / 10000000000
)

date_now = datetime.now()

""" print(f"{date_now:%Y-%m-%d}") """
print(f"The approximate volume is {volume_calc:.2f} liters.")

with open("volumes.txt", "at") as volume_file:
    print(
        f"{date_now:%Y-%m-%d}, {tire_width}, {tire_ratio}, {tire_diameter}, {volume_calc:.2f}",
        file=volume_file,
    )


user_buy = input(
    f"Would you like to buy tires with {tire_width} width, aspect ratio of {tire_ratio}, and a diameter of {tire_diameter}? (yes/no)  "
)

if user_buy.lower() == "yes":
    user_phone = input("Please write your phone number\n")
    with open("volumes.txt", "at") as phone_number:
        print(f"{user_phone}", file=phone_number)
else:
    print("Thank you for your time")
