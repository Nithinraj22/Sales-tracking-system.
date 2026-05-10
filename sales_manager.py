from sale import Sale
from db_connection import get_connection
from exceptions import OutOfStockError

class SalesManager:
    def __init__(self, inventory_manager):
        self.inventory = inventory_manager

    def record_sale(self, product_id, quantity):
        product = self.inventory.get_product(product_id)

        if not product:
            print(f"Product ID '{product_id}' not found.")
            return

        current_stock = product["stock"]
        price = product["price"]

        if current_stock < quantity:
            raise OutOfStockError(f"Only {current_stock} items in stock.")

        total = price * quantity
        new_stock = current_stock - quantity

        try:
            conn = get_connection()
            if not conn:
                print("Failed to connect to database.")
                return

            cursor = conn.cursor()

            # Insert sale record
            cursor.execute(
                "INSERT INTO sales (product_id, quantity, total) VALUES (%s, %s, %s)",
                (product_id, quantity, total)
            )

            # Update product stock
            cursor.execute(
                "UPDATE products SET stock = %s WHERE id = %s",
                (new_stock, product_id)
            )

            conn.commit()
            conn.close()

            print(f"Sale recorded: Product ID: {product_id}, Quantity: {quantity}, Total: ₹{total:.2f}")

        except Exception as e:
            print(f"Error recording sale: {type(e).__name__} - {e}")

    def list_sales(self):
        try:
            conn = get_connection()
            if not conn:
                print("Failed to connect to database.")
                return

            cursor = conn.cursor()
            cursor.execute("SELECT product_id, quantity, total, timestamp FROM sales")
            sales = cursor.fetchall()
            conn.close()

            if not sales:
                print("No sales recorded yet.")
                return

            print("\nSales Records:")
            for s in sales:
                print(f"Product ID: {s[0]}, Quantity: {s[1]}, Total: ₹{s[2]:.2f}, Time: {s[3]}")

        except Exception as e:
            print(f"Error fetching sales: {type(e).__name__} - {e}")
