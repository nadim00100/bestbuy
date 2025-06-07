
import store
import products

def start(store_obj):
    while True:
        print("\n=== Store Menu ===")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("\n--- Products in Store ---")
            for i, product in enumerate(store_obj.get_all_products(), 1):
                print(f"{i}. {product.show()}")

        elif choice == "2":
            total_quantity = store_obj.get_total_quantity()
            print(f"\nTotal quantity in store: {total_quantity}")

        elif choice == "3":
            available_products = store_obj.get_all_products()
            if not available_products:
                print("No products available to order.")
                continue

            shopping_list = []

            while True:
                print("\nAvailable products:")
                for i, product in enumerate(available_products, 1):
                    print(f"{i}. {product.show()}")

                try:
                    product_choice = int(input("\nEnter product number from the list above to buy (or 0 to finish): "))
                    if product_choice == 0:
                        break
                    if product_choice < 1 or product_choice > len(available_products):
                        raise ValueError("Invalid product number.")
                    selected_product = available_products[product_choice - 1]

                    quantity = int(input(f"Enter quantity of '{selected_product.name}': "))
                    if quantity <= 0 or quantity > selected_product.get_quantity():
                        raise ValueError(f"Only {selected_product.get_quantity()} units available.")

                    shopping_list.append((selected_product, quantity))

                except ValueError as e:
                    print(f"\n❌ Error: Please enter an integer ")
                    print("⚠️  Please choose an available product and valid quantity from the list above.")

            if shopping_list:
                try:
                    total_cost = store_obj.order(shopping_list)
                    print(f"\n✅ Order successful! Total cost: ${total_cost:.2f}")
                except ValueError as e:
                    print(f"\n❌ Order failed: {e}")
            else:
                print("No items ordered.")

        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


def main():
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250)
    ]
    best_buy = store.Store(product_list)
    start(best_buy)
if __name__ == "__main__":
    main()
