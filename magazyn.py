import sys

items = []

sold_items = []

items.append({"name": "Ibufen", "quantity": 20.0, "unit": "kg", "unit_price": 13})
items.append({"name": "Devicap", "quantity": 13.9, "unit": "kg", "unit_price": 42.5})
items.append({"name": "Pirolam", "quantity": 155.6, "unit": "op", "unit_price": 17})

menu_list = ['add', 'show', 'sell', 'sold', 'exit']


def get_item_by_name(product_name):
    for product in items:
        i_a = (product["name"])
        print(i_a)
        if i_a == product_name:
            print("found")
            return product
    return None


def show_items(products):
    # header
    print("{:<10} {:<10} {:<10} {:<10}".format("Name", "Quantity", "Unit", "Unit Price (PLN)"))
    print("{:<10} {:<10} {:<10} {:<10}".format("__________", "__________", "__________", "__________"))
    for product in products:
        print("{:10} {:>10} {:>10} {:>10}".format(product["name"], "{:.2f}".format(product["quantity"]), product["unit"],
                                                  product["unit_price"]))


def add_item():
    p_name = input("Name: ")
    p_quantity = input("Quantity: ")
    product = get_item_by_name(p_name)
    if product is not None:
        product["quantity"] = float(product["quantity"] + p_quantity)
    else:
        p_unit = input("Unit: ")
        p_unit_price = input("Unit_price: ")
        items.append({"name": p_name, "quantity": p_quantity, "unit": p_unit, "unit_price": p_unit_price})


def sell_item():
    sold_product_name = input("Item name:")
    sold_product = get_item_by_name(sold_product_name)
    if sold_product is not None:
        quantity_s = float(input("Quantity required:"))
        if quantity_s <= sold_product["quantity"]:
            sold_product['quantity'] = float(sold_product["quantity"] - quantity_s)
            sold_items.append({"name": sold_product_name, "quantity": quantity_s, "unit": sold_product["unit"],
                               "unit_price": sold_product["unit_price"]})
        else:
            print("Not enough in the storage")
    else:
        print("Product not available")


welcome = ''
while welcome != 'exit':
    print("Choose from menu: ", menu_list)
    welcome = input("What would You like to do? ")
    if welcome == "show":
        show_items(items)
    if welcome == "sold":
        show_items(sold_items)
    if welcome == "add":
        add_item()
    if welcome == "sell":
        sell_item()

print("Exiting...Bye")
exit(0)
