"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

askAge = input("How old are you? ")

heart_range = 220 - int(askAge)

lowest_percent = heart_range * 0.65
highest_percent = heart_range * 0.85

lowest_percent = int(lowest_percent)
highest_percent = int(highest_percent)

print(
    f"When you exercise to strengthen your heart, you should keep your heart rate between {lowest_percent} and {highest_percent} per minute."
)
