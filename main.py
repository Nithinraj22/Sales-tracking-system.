from inventory_manager import InventoryManager
from sales_manager import SalesManager
from reports import generate_inventory_report, generate_sales_report
from exceptions import OutOfStockError

def main():
    inventory = InventoryManager()
    sales = SalesManager(inventory)

    print("Welcome to the Sales Tracking System")

    while True:
        print("\nMenu:")
        print("1. Add Product")
        print("2. Update Product")
        print("3. Remove Product")
        print("4. List Inventory")
        print("5. Record Sale")
        print("6. View Sales")
        print("7. Reports")
        print("0. Exit")

        choice = input("Enter choice: ").strip()

        try:
            if choice == "1":
                pid = input("Product ID: ").strip()
                name = input("Name: ").strip()
                price_input = input("Price: ").strip()
                stock_input = input("Stock: ").strip()

                if not price_input.replace('.', '', 1).isdigit() or not stock_input.isdigit():
                    print("Invalid price or stock value.")
                    continue

                price = float(price_input)
                stock = int(stock_input)
                inventory.add_product(pid, name, price, stock)

            elif choice == "2":
                pid = input("Product ID to update: ").strip()
                name = input("New Name (or leave blank): ").strip()
                price = input("New Price (or leave blank): ").strip()
                stock = input("New Stock (or leave blank): ").strip()

                inventory.update_product(
                    pid,
                    name=name if name else None,
                    price=float(price) if price else None,
                    stock=int(stock) if stock else None
                )

            elif choice == "3":
                pid = input("Product ID to remove: ").strip()
                inventory.remove_product(pid)

            elif choice == "4":
                inventory.list_products()

            elif choice == "5":
                pid = input("Product ID to sell: ").strip()
                qty_input = input("Quantity: ").strip()

                if not qty_input.isdigit():
                    print("Invalid quantity.")
                    continue

                qty = int(qty_input)
                try:
                    sales.record_sale(pid, qty)
                except OutOfStockError as e:
                    print(f"Sale Error: {e}")

            elif choice == "6":
                sales.list_sales()

            elif choice == "7":
                generate_inventory_report(inventory)
                generate_sales_report(sales)

            elif choice == "0":
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please enter a number from 0 to 7.")

        except Exception as e:
            print(f"Unexpected error: {type(e).__name__} - {e}")

if __name__ == "__main__":
    main()
