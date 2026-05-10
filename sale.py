class Sale:
    def __init__(self, product_id, quantity, total_price):
        self.product_id = product_id
        self.quantity = quantity
        self.total_price = total_price

    def __str__(self):
        return f"Product ID: {self.product_id}, Quantity: {self.quantity}, Total: ₹{self.total_price}"
