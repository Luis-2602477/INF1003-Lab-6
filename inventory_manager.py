from product import Product
from file_handler import load_inventory, save_inventory, INVENTORY_FILE
LINE = "-" * 48


def get_int(prompt):
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            return int(value)
        print(f"Error: '{value}' is not a valid whole number.")


def get_price(prompt):
    while True:
        value = input(prompt).strip()
        try:
            price = float(value)
            if price >= 0:
                return price
            print("Error: Price cannot be negative.")
        except ValueError:
            print(f"Error: '{value}' is not a valid price.")




def add_product(inventory):
    print("Add New Product")
    product_id = input("Product ID: ").strip().upper()
    if inventory.search_product(product_id) is not None:
        print(f"Error: A product with ID {product_id} already exists.")
        return

    name = input("Product Name: ").strip()
    price = get_price("Price: ")
    stock = get_int("Stock Quantity: ")

    product = Product(product_id, name, price, stock)
    inventory.add_product(product)
    print("Product added successfully!")

def update_stock(inventory):
    print("Update Stock")
    product_id = input("Enter Product ID: ").strip().upper()
    product = inventory.search_product(product_id)
    if product is None:
        print("Product not found.")
        return

    print("Product Found:")
    print(f"Name: {product.get_name()}")
    print(f"Current Stock: {product.get_stock()}")
    product.update_stock(get_int("New Stock Quantity: "))  # the Product changes its own stock
    print("Stock updated successfully!")


def search_product(inventory):
    print("Search Product")
    product_id = input("Enter Product ID: ").strip().upper()
    product = inventory.search_product(product_id)
    if product is None:
        print("Product not found.")
        return

    print("Product Found")
    print(LINE)
    product.display_information()
    print(LINE)

def show_menu():
    print("----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")


def main():
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)
    inventory = load_inventory()
    show_menu()

    while True:
        choice = input("Enter option: ").strip()

        if choice == "1":
            inventory.display_all()
        elif choice == "2":
            add_product(inventory)
        elif choice == "3":
            update_stock(inventory)
        elif choice == "4":
            search_product(inventory)
        elif choice == "5":
            print("Saving inventory...")
            save_inventory(inventory)
            print(f"Inventory saved successfully to {INVENTORY_FILE}.")
        elif choice == "6":
            print("Saving inventory before exit...")
            save_inventory(inventory)
            print("Inventory saved successfully.")
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("Invalid option. Please enter a number from 1 to 6.")
        print()


if __name__ == "__main__":
    main()