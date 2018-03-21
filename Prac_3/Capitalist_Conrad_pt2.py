"""
CP1404/CP5632 - Practical
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 10%, and
a 50% chance that it decreases by 0 to 5%.
If the price rises above $1000, or falls below $0.01, the program should end.
The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901)
"""


#PRAC_3 DEBUGGING

import random

MAX_INCREASE = 0.1  # 10%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 0.01
MAX_PRICE = 1000.0
INITIAL_PRICE = 10.0

output_file = "conrad_output.txt"

new_file = open(output_file, "w")

price = INITIAL_PRICE
print("${:,.2f}".format(price), file=new_file)

current_day = 0
while price >= MIN_PRICE and price <= MAX_PRICE:

new_file.close()

