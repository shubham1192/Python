customers = ["Linda", "Jack", "Zoran"]
products = ["apple", "banana", "cake"]
sellingPrice = [3.5, 6.82, 23]
stocks = [134, 52, 5]


def customer_name(n):
    if n in customers:
        print("Return customer!")
    else:
        print("New customer!")


def product_name(prod_name):
    if prod_name not in products:
        print("Sorry, no such product. Quit...")
        exit()


def check_quantity(quantity, prod_name):
    index = products.index(prod_name)
    if stocks[index] < quantity:
        print("Sorry, not enough stock. Quit...")
        exit()


def print_details(cust_name, prod_name, quantity):
    print()
    index = products.index(prod_name)
    print(cust_name+" purchased "+str(quantity)+" x "+prod_name)
    print("Unit price: $"+str(sellingPrice[index]))
    if cust_name not in customers:
        print("Total price: $"+str(sellingPrice[index]*quantity))
    else:
        print("Total price: $" + str((sellingPrice[index] * quantity)-(sellingPrice[index] * quantity)*10/100))


name = input("Enter customer name: ")
customer_name(name)
prod = input("Enter product name: ")
product_name(prod)
unit = int(input("Enter quantity: "))
check_quantity(unit, prod)
print_details(name, prod, unit)
