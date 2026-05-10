#To create a Product class to represent products in the inventory
#This will give product details like ID, name, price, and stock quantity
#---> Next create exceptions.py module to define custom exceptions.

class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} (₹{self.price}) — Stock: {self.stock}"
