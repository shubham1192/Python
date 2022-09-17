customers = ["Linda", "Jack", "Zoran"]
products = ["apple", "banana", "cake", "ice"]
sellingPrice = [3.5, 6.82, 0, 000]
stocks = [134, 52, 5, 0]
data = {}


def customer_name(n):
    data[n] = [0, 0, 0, 0, 0]
    print(data)
    if n in customers:
        print("Return customer!")
    else:
        print("New customer!")


def product_name(prod_name):
    if prod_name not in products:
        print("Sorry, no such product. Try again.")
        return 0
    else:
        return 1


def check_quantity(quantity, prod_name):
    index = products.index(prod_name)
    if stocks[index] < quantity:
        print("Sorry, not enough stock. Try again.")
        return 0
    else:
        return 1


def print_details(cust_name, prod_name, quantity):
    print()
    index = products.index(prod_name)
    if sellingPrice[index] == 000:
        print("NOT AVAILABLE(HIDDEN PRODUCT)")
        return 0
    else:
        print(cust_name + " purchased " + str(quantity) + " x " + prod_name)
        print("Unit price: $" + str(sellingPrice[index]))
        if cust_name not in customers:
            # print("Total price: $"+str(sellingPrice[index]*quantity))
            return str(sellingPrice[index]*quantity)
        else:
            # print("Total price: $" + str((sellingPrice[index] * quantity)-(sellingPrice[index] * quantity)*10/100))
            return str((sellingPrice[index] * quantity)-(sellingPrice[index] * quantity)*10/100)


def show_inventory():
    for i in range(len(products)):
        print(products[i], end=" ")
        if sellingPrice[i] == 000:
            print("---", end=" ")
        else:
            print("$"+str(sellingPrice[i]), end=" ")
        print(str(stocks[i]))


def purchase(n):
    ans = 0
    price = 0
    f3 = 'Y'
    while f3 != 'N':
        f1 = 0
        f2=0
        while f2 != 1:
            while f1 != 1:
                prod = input("Enter product name: ")
                f1 = product_name(prod)

            f1 = 0
            idx = products.index(prod)

            unit = int(input("Enter quantity: "))
            f2 = check_quantity(unit, prod)
        data[n][idx] += unit
        price = print_details(name, prod, unit)
        if price == 0:
            return price
        ans = float(ans) + float(price)
        print("Total price: $" + str(ans))
        data[n][4] = ans
        f3 = input("Continue?(Y/N)")
        if f3 == 'N':
            customers.append(n)
            return 1


def replenish_bulk(size):
    for j in range(len(stocks)):
        stocks[j] = size
    print("Bulk Update", end=" ")
    print(stocks)


def replenish_one():
    flag = 0
    while flag != 1:
        nam = input("Enter product name: ")
        flag = product_name(nam)
        if flag == 1:
            idx = products.index(nam)
            print("Available Stock: "+str(stocks[idx]))
            flag1 = 0
            while flag1 != 1:
                sz = int(input("Enter the amount to add: "))
                if sz == 0:
                    print("Sorry, not a reasonable amount. Try again.")
                    continue
                else:
                    stocks[idx] = stocks[idx]+sz
                    print("Stock of apple is now "+str(stocks[idx]))
                    flag1 = 1


def show_data():
    for x in data:
        print(x, end=" ")
        print(' '.join(map(str, data[x])))


ex = 0
while ex != 1:
    print("1 Show all the customers")
    print("2 Show all the products")
    print("3 Purchase")
    print("4 Add products")
    print("5 Show inventory")
    print("6 Replenish in bulk")
    print("7 Replenish in one")
    print("8 Show all the data")
    n = int(input())
    match n:
        case 1:
            for x in customers:
                print(x)
        case 2:
            for x in products:
                print(x)
        case 3:
            name = input("Enter customer name: ")
            customer_name(name)
            f = 0
            while f != 1:
                f = purchase(name)
        case 4:
            f = 0
            newList = []
            while f != 1:
                item = input("Enter product name:")
                newList.append(item)
                f = int(input("wanna add more -> 0, No-> 1: "))
            products = newList
            newPrice = []
            print()
            for i in range(len(products)):
                print("Enter 000 if the product has no price, i.e A Hidden product")
                price = int(input("price for "+products[i]+": "))
                newPrice.append(price)
            sellingPrice = newPrice
            print()
            newStock = []
            for i in range(len(products)):
                stock = int(input("stock for "+products[i]+": "))
                newStock.append(stock)
            stocks = newStock
        case 5:
            show_inventory()
        case 6:
            n = int(input("Enter stock size: "))
            replenish_bulk(n)
        case 7:
            replenish_one()
        case 8:
            show_data()
    print("Enter 0 for main menu, 1 to exit: ")
    ex = int(input())
