from pyscript import display

restaurant_name = "Moon & Milk Coffee"  # string
owner_name = "Alexander Rain Co"  # string

year_established = 2025  # integer

tax_rate = 0.08  # float (8% tax)
popular_item_price = 150.00  # float (menu item price)

has_delivery = True  # boolean

product_names = ["Matcha Latte", "Caramel Frappuccino", "Taro Milk Tea"]  # list

business_hours = ("11:00 AM", "10:00 PM")  # tuple

menu_prices = {  # dictionary
    "Matcha Latte": 150.00,
    "Taro Milk Tea": 120.00,
    "Caramel Frappuccino": 185.00,
    "Hazelnut Dark Mocha": 125.00,
    "Chocolate Chip Cream Frappuccino": 210.00
}

common_allergens = {"gluten", "dairy", "nuts"}  # set

# Resto Info
display(restaurant_name, target="name1")
display(f"Owner: {owner_name}", target="owner")
display(f"Since {year_established}", target="since")
display("Menu Pricelist", target="heading1")

# Menu
display(product_names[0], target="prod1")
display(f"₱{menu_prices['Matcha Latte']:.2f}", target="price1")
display(product_names[1], target="prod2")
display(f"₱{menu_prices['Caramel Frappuccino']:.2f}", target="price2")
display(product_names[2], target="prod3")
display(f"₱{menu_prices['Taro Milk Tea']:.2f}", target="price3")
display("Hazelnut Dark Mocha", target="prod4")
display(f"₱{menu_prices['Hazelnut Dark Mocha']:.2f}", target="price4")
display("Chocolate Chip Cream Frappuccino", target="prod5")
display(f"₱{menu_prices['Chocolate Chip Cream Frappuccino']:.2f}", target="price5")

# Openinng hours
display(f"Open: {business_hours[0]} - {business_hours[1]}", target="openingHours")

# Delivery
if has_delivery:
    display("Delivery Available", target="orderType")
else:
    display("Dine-in Only", target="orderType")

# Allergens
display(f"Common Allergens: {', '.join(common_allergens)}", target="allergens")

# Best seller
display(f"Best Seller Price: ₱{popular_item_price:.2f}", target="popularItem")