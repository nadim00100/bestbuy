from typing import List, Tuple
import products  # Import the Product class from the products module


class Store:
    """
    A class to represent a store that holds a list of products.

    Attributes:
        products (List[Product]): A list of Product objects in the store.
    """

    def __init__(self, products: List[products.Product]):
        """
        Initializes a store with a list of products.

        Args:
            products (List[Product]): A list of products to be added to the store.
        """
        self.products = products

    def add_product(self, product: products.Product):
        """
        Add a product to the store's inventory.

        Args:
            product (Product): The product to be added to the store.
        """
        self.products.append(product)

    def remove_product(self, product: products.Product):
        """
        Removes a product from the store's inventory.

        Args:
            product (Product): The product to be removed from the store.

        Raises:
            ValueError: If the product is not found in the store.
        """
        if product in self.products:
            self.products.remove(product)
        else:
            raise ValueError("Product not found in store.")

    def get_total_quantity(self) -> int:
        """
        Calculate the total quantity of all products in the store.

        Returns:
            int: The total quantity of items in the store.
        """
        total_quantity = sum(product.quantity for product in self.products)
        return total_quantity

    def get_all_products(self) -> List[products.Product]:
        """
        Get all active products in the store (products with quantity > 0).

        Returns:
            List[Product]: A list of active products in the store.
        """
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[Tuple[products.Product, int]]) -> float:
        """
        Process an order and calculate the total price.

        Args:
            shopping_list (List[Tuple[Product, int]]): A list of tuples where each tuple
                                                      contains a Product and the quantity to be bought.

        Returns:
            float: The total cost of the order.

        Raises:
            ValueError: If there's not enough stock for any of the products in the order.
        """
        total_price = 0
        for product, quantity in shopping_list:
            if quantity > product.quantity:
                raise ValueError(
                    f"Not enough stock for {product.name}. Available: {product.quantity}, Requested: {quantity}")
            total_price += product.buy(quantity)
        return total_price
