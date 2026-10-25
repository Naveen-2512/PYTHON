
def display_inventory(inventory):

    for item, quantity in inventory.items():
        print(item, ":", quantity)


def merge_inventory(store1, store2):
    # Merge the inventories of two stores
    merged = store1.copy()

    for item, quantity in store2.items():
        merged[item] = merged.get(item, 0) + quantity

    return merged


def low_stock_items(inventory, limit):
    # Find items with stock below the limit
    return {
        item: quantity
        for item, quantity in inventory.items()
        if quantity < limit
    }


def main():
    store1 = {
        "Pen": 50,
        "Notebook": 30,
        "Pencil": 40
    }

    store2 = {
        "Pen": 20,
        "Notebook": 15,
        "Eraser": 25
    }

    print("Store 1 Inventory:")
    display_inventory(store1)

    print("\nStore 2 Inventory:")
    display_inventory(store2)

    inventory = merge_inventory(store1, store2)

    print("\nMerged Inventory:")
    display_inventory(inventory)

    item = input("\nEnter item to check: ")

    if item in inventory:
        print(item, "stock:", inventory[item])
    else:
        print("Item not found in inventory.")

    limit = int(input("Enter minimum stock limit: "))
    low_stock = low_stock_items(inventory, limit)

    print("\nLow Stock Items:")
    if low_stock:
        display_inventory(low_stock)
    else:
        print("No low-stock items found.")


if __name__ == "__main__":
    main()
