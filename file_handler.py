import json
import os

from product import Product
from inventory import Inventory

INVENTORY_FILE = "inventory.json"


def load_inventory(filename=INVENTORY_FILE):
    inventory = Inventory()

    if not os.path.exists(filename):
        print(f"{filename} not found. Starting with an empty inventory.")
        return inventory

    print(f"{filename} found.")
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        for item in data:
            product = Product(item["id"], item["name"], item["price"], item["stock"])
            inventory.add_product(product)
        print("Inventory loaded successfully.")
    except (json.JSONDecodeError, KeyError, TypeError, ValueError):
        print("Inventory file is unreadable. Starting with an empty inventory.")
        inventory = Inventory()

    return inventory


def save_inventory(inventory, filename=INVENTORY_FILE):
    data = [product.to_dict() for product in inventory.get_products()]
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)