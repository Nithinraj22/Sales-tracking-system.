from db_connection import get_connection

class InventoryManager:
    def __init__(self):
        pass  # No in-memory dictionary needed

    def add_product(self, product_id, name, price, stock):
        conn = get_connection()
        if not conn:
            print("Failed to connect to database.")
            return
        cursor = conn.cursor()

        cursor.execute("SELECT id FROM products WHERE id = %s", (product_id,))
        if cursor.fetchone():
            print(f"Product ID '{product_id}' already exists.")
            conn.close()
            return

        cursor.execute(
            "INSERT INTO products (id, name, price, stock) VALUES (%s, %s, %s, %s)",
            (product_id, name, price, stock)
        )
        conn.commit()
        conn.close()
        print(f"Product '{name}' added successfully.")

    def update_product(self, product_id, name=None, price=None, stock=None):
        conn = get_connection()
        if not conn:
            print("Failed to connect to database.")
            return
        cursor = conn.cursor()

        updates = []
        values = []

        if name:
            updates.append("name = %s")
            values.append(name)
        if price:
            updates.append("price = %s")
            values.append(price)
        if stock is not None:
            updates.append("stock = %s")
            values.append(stock)

        if not updates:
            print("No updates provided.")
            conn.close()
            return

        query = f"UPDATE products SET {', '.join(updates)} WHERE id = %s"
        values.append(product_id)

        cursor.execute(query, tuple(values))
        conn.commit()
        conn.close()

        if cursor.rowcount > 0:
            print(f"Product '{product_id}' updated successfully.")
        else:
            print(f"Product ID '{product_id}' not found.")

    def remove_product(self, product_id):
        conn = get_connection()
        if not conn:
            print("Failed to connect to database.")
            return
        cursor = conn.cursor()

        cursor.execute("DELETE FROM products WHERE id = %s", (product_id,))
        conn.commit()
        conn.close()

        if cursor.rowcount > 0:
            print(f"Product '{product_id}' removed successfully.")
        else:
            print(f"Product ID '{product_id}' not found.")

    def list_products(self):
        conn = get_connection()
        if not conn:
            print("Failed to connect to database.")
            return
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, price, stock FROM products")
        products = cursor.fetchall()
        conn.close()

        if not products:
            print("Inventory is empty.")
            return

        print("\nCurrent Inventory:")
        for p in products:
            print(f"ID: {p[0]}, Name: {p[1]}, Price: ₹{p[2]:.2f}, Stock: {p[3]}")

    def get_product(self, product_id):
        conn = get_connection()
        if not conn:
            print("Failed to connect to database.")
            return None
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, name, price, stock FROM products WHERE id = %s", (product_id,))
        product = cursor.fetchone()
        conn.close()
        return product
