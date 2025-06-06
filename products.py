class Product:
    """
    A class to represent a product with a name, price, and quantity in stock.

    Attributes:
        name (str): The name of the product.
        price (float): The price of the product.
        quantity (int): The number of units of the product available in stock.
    """

    def __init__(self, name, price, quantity):
        """
        Initializes a new product with the given name, price, and quantity.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The number of units of the product in stock.
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def buy(self, amount):
        """
        Buy a specified amount of the product and reduce the stock.

        Args:
            amount (int): The number of units to buy.

        Returns:
            float: The total cost of the units bought.

        Raises:
            ValueError: If the amount requested is more than the available stock.
        """
        if amount > self.quantity:
            raise ValueError("Not enough in stock.")
        self.quantity -= amount
        return self.price * amount

    def is_active(self):
        """
        Check if the product is still active (i.e., if there is any stock left).

        Returns:
            bool: True if the product has stock available, False otherwise.
        """
        return self.quantity > 0

    def show(self):
        """
        Print the details of the product: its name, price, and remaining quantity.
        """
        print(f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}")

    def set_quantity(self, new_quantity):
        """
        Set the quantity of the product to a new value.

        Args:
            new_quantity (int): The new quantity of the product.
        """
        self.quantity = new_quantity
