'''
Iliyana Iskarova Iskarova
125752501
started - 03/02/2026, ended - 08/02/2026
1st step of building inventory management system for Murphy's General Store
'''


#STEP 1: Constants & Initialisati
IDX_NAME = 0
IDX_CATEGORY = 1
IDX_PRICE = 2
IDX_QTY = 3
IDX_MIN = 4

inventory = [["Milk", "Dairy", 1.50, 20, 10],
        ["Bread", "Bakery", 0.85, 15, 5],
        ["Tea", "Beverages", 3.20, 30, 8]]

#STEP 4: Create input validation helper functions
#I needed a little help to figure out the try - exception syntax
#https://www.w3schools.com/python/python_try_except.asp
#link to the conversation - https://chatgpt.com/share/6988c649-dd90-8008-b704-5f817d99866f
def get_valid_int(intVar, min_value=0):
    while True:
        try:
            value = int(input(intVar))
            if value < min_value:
                print(f"Value must be at least {min_value}")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_valid_float(floatVar, min_value=0):
    while True:
        try:
            value = float(input(floatVar))
            if value < min_value:
                print(f"Value must be at least {min_value}")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a floating point number.")

#STEP 2: Create a menu function

def menu():
    print("\n=== Murphy's General Store - Inventory System ===")
    print("1. View Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Remove Product")
    print("5. Low Stock Alert")
    print("6. Total Inventory Value")
    print("7. Exit")
    return get_valid_int("Enter your choice (1-7): ", 1)

#STEP 3: Implement each menu option as a function

def viewAllItems(list):
    if list == []:
        print("Inventory is empty")
        return
    else: print("\n--- All Products ---")
    print(f"{'Product':15}{'Category':15}{'Price':10}{'Stock':10}{'Min':10}")
    print("-"*55)
    for item in list:
        print(f"{item[IDX_NAME]:15}"
              f"{item[IDX_CATEGORY]:15}"
              f"€{item[IDX_PRICE]:.2f}     "
              f"{item[IDX_QTY]:5}"
              f"{item[IDX_MIN]:8}") #went through a lot tril and error to figure out the spacing

def addItem(list):
    print("\n--- Add Item ---")

    name = input('Enter product name: ')
    for product in inventory:
        if product[IDX_NAME].lower() == name.lower():
            return print("Product already exists.")

    category = input('Enter product category: ')
    price = get_valid_float("Enter product price: ")
    quantity = get_valid_int("Enter product quantity: ")
    minQty = get_valid_int("Enter product minimum quantity: ")

    list.append([name, category, price, quantity,minQty])
    return print("Item",name,"added sucesfully!")

def updateStocka(list):

    print("\n--- Update Stock ---")

    name = input("Enter product name: ")
    for item in list:
        if item[IDX_NAME] == name:
            status = input("Is this a (S)ale or (D)elivery?").lower()
            if status=="s":
                sold = get_valid_int("Enter quantity sold: ")
                item[IDX_QTY] = item[IDX_QTY] - sold
            elif status == "d":
                delivered=get_valid_int("Enter quantity delivered: ")
                item[IDX_QTY] = item[IDX_QTY] + delivered
            else :
                print("Invalid input. Please enter a valid option (s/d).")
                return
            print("Item successfully updated!")
            return
print("Item not found.")

def removeItem(list):
    print("\n--- Remove Item ---")
    name=input("Enter product name that you want to remove: ")
    for item in list:
        if item[IDX_NAME] == name:
            decision = input("Are you sure you want to remove this item? (y/n): ").lower()
            if decision == "y":
                list.remove(item)
                print("Item",item[IDX_NAME],"removed!")
            elif decision == "n":
                print("Item was not deleted.")
            else:
                print("Invalid input. Please enter a valid option y/n.")

    return print("Item not found.")


def lowStock(list):
    print("\n--- Low Stock Alert ---")
    counter = 0
    found = False
    print(f"{'Product':15}{'Stock':15}{'Min':10}{'Order':10}")
    print("-"*50)
    for item in list:
        if item[IDX_QTY] <= item[IDX_MIN]:
            order = item[IDX_MIN] - item[IDX_QTY]
            print(f"{item[IDX_NAME]:10}{item[IDX_QTY]:10}"
                  f"{item[IDX_MIN]:15}{order:10}")
            counter += 1
            found = True
    if found == False:
        print("No items found for restock")
    print("-"*50)
    print("Items needing restock:",counter)


def totalInventory(list):
    print("\n--- Total Inventory Value ---")
    total = 0
    for item in list:
        total = total + (item[IDX_QTY]*item[IDX_PRICE])
    print(f"Total inventory value: €{total:.2f}")
    return

def main():
#STEP 5: Build the main programme loop

    while True:
     choice = menu()
     match choice:
        case 1:
            viewAllItems(inventory)

        case 2:
            addItem(inventory)

        case 3:
            updateStocka(inventory)

        case 4:
            removeItem(inventory)

        case 5:
            lowStock(inventory)

        case 6:
            totalInventory(inventory)

        case 7: exit()

        case _:
            print("Invalid input. Please enter a valid option 1-7")

main()
'''Self reflection: 
I learned that you have to return earlier in the function for it to stop itterating through the whole for loop 
- went through trail and error. Also finally figured out how to use try - catch exception in Python
 and the difference between NameError and ValueError- withe the little help of W3S and AI'''