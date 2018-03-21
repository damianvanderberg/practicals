Menu_1 = """How many items do you have?"""
Menu_2 = """What are the price/s of your item/s?"""

print(Menu_1)
number_of_items = int(input("Number of items:  "))

if number_of_items > 0:
    print(Menu_2)

Total_price = 0

for i in range(number_of_items):
    Price_of_item = float(input("Price of item:  $"))
    New_price = Total_price + Price_of_item

    # sum of items in range of number of items
    # maybe make a list so the sum can be identified by multiple inputs

    if Total_price >= 100:
        Total_price = (Total_price * 0.1)
        print("The total price is $ ", Total_price)
        print('Cheers for shopping')
    else:
        print(Total_price)

