import sys

products_list = []

products_list.append({"name":"Ibufen", "quantity":20, "unit":"kg", "unit_price":13})
products_list.append({"name":"Devicap", "quantity":13, "unit":"kg", "unit_price":42.5})
products_list.append({"name":"Pirolam", "quantity":15, "unit":"op", "unit_price":17})


welcome = ''
while welcome != 'exit':
    welcome = input("What would You like to do? ")
print("Exiting...Bye")
exit(0)

def get_items():
    if welcome == 'show':
        print(products_list)

showing = get_items(products_list)
print(showing)

#print("Name\tQuantity\tUnit\tUnit Price (PLN)")