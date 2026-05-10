""" This is not just any class—it’s a special kind of error!
By inheriting from Exception, your class becomes part of Python’s exception hierarchy"""
"""
class OutOfStockError:
    pass  
    ---> It’s just a plain class—not an actual error
    ---> You can’t raise it with raise OutOfStockError("message")
    ---> You can’t catch it with except OutOfStockError
"""
# Next create inventory_manager.py module to manage products in inventory(all product details).

class OutOfStockError(Exception):    #Exception is a built-in class in Python, and it’s part of Python’s core error-handling system
    """Raised when trying to sell more stock than available."""
    pass
