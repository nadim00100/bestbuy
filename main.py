import products


def main():
    """
    Main function to demonstrate the usage of the Product class.

    This function creates two product objects (Bose QuietComfort Earbuds and
    MacBook Air M2), buys a few units, checks their status, and updates the
    quantity of the Bose product.
    """
    bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = products.Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))  # Buys 50 units of Bose
    print(mac.buy(100))  # Buys 100 units of Mac (all stock)
    print(mac.is_active())  # Should be False, as stock is now 0

    bose.show()  # Show current state of Bose
    mac.show()  # Show current state of Mac

    bose.set_quantity(1000)  # Set Bose quantity to 1000
    bose.show()  # Show updated Bose


if __name__ == "__main__":
    """
    Entry point for the program. Runs the main function if the script is executed
    directly.
    """
    main()
