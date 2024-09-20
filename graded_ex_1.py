products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}

def display_categories():
    """Display the available product categories and return the selected category index."""
    categories = list(products.keys())
    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category}")
    category_choice = input("Select a category number (or 'q' to quit): ")
    if category_choice.lower() == 'q':
        return None
    try:
        category_index = int(category_choice) - 1
        if 0 <= category_index < len(categories):
            return category_index
        else:
            print("Invalid category number. Please try again.")
            return None
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

def display_products(products_list):
    for i, (product_name, price) in enumerate(products_list, start=1):
        print(f"{i}. {product_name} - ${price}")

def display_sorted_products(products_list, sort_order):
    """Sort products by price and display them based on the sort order."""
    if sort_order == '1' or sort_order.lower() == 'asc':
        sorted_list = sorted(products_list, key=lambda x: x[1])
    elif sort_order == '2' or sort_order.lower() == 'desc':
        sorted_list = sorted(products_list, key=lambda x: x[1], reverse=True)
    else:
        print("Invalid sort order. Please choose 1 for ascending or 2 for descending.")
        return None
    display_products(sorted_list)
    return sorted_list

def add_to_cart(cart, product, quantity):
    cart.append((product[0], product[1], quantity))

def display_cart(cart):
    total_cost = 0
    for product_name, unit_price, quantity in cart:
        total = unit_price * quantity
        print(f"{product_name} - ${unit_price} x {quantity} = ${total}")
        total_cost += total
    print(f"Total cost: ${total_cost}")

def generate_receipt(name, email, cart, total_cost, address):
    """Generate and display a receipt with customer details and cart summary."""
    print("\n--- Receipt ---")
    print(f"Name: {name}")
    print(f"Email: {email}")
    for product_name, unit_price, quantity in cart:
        total = unit_price * quantity
        print(f"{product_name} - Quantity: {quantity}, Total: ${total}")
    print(f"Total Cost: ${total_cost}")
    print(f"Delivery Address: {address}")
    print("Your items will be delivered in 3 days. Payment will be accepted after successful delivery.")

def validate_name(name):
    parts = name.split()
    return len(parts) == 2 and all(part.isalpha() for part in parts)

def validate_email(email):
    return '@' in email

def main():
    name = input("Enter your name (first and last): ")
    while not validate_name(name):
        print("Invalid name. Please enter a valid first and last name.")
        name = input("Enter your name (first and last): ")

    email = input("Enter your email address: ")
    while not validate_email(email):
        print("Invalid email. Please enter a valid email address.")
        email = input("Enter your email address: ")

    cart = []
    while True:
        print("\nAvailable Categories:")
        category_index = display_categories()
        if category_index is None:
            break

        category = list(products.keys())[category_index]
        products_list = products[category]

        while True:
            print(f"\nProducts in {category}:")
            display_products(products_list)
            print("Options:")
            print("1. Select a product to buy")
            print("2. Sort products by price")
            print("3. Go back to category selection")
            print("4. Finish shopping")
            option = input("Select an option: ")

            if option == '1':
                product_choice = input("Enter the product number: ")
                try:
                    product_index = int(product_choice) - 1
                    product = products_list[product_index]
                    quantity = int(input("Enter quantity: "))
                    if quantity <= 0:
                        print("Quantity must be greater than 0.")
                        continue
                    add_to_cart(cart, product, quantity)
                    print(f"{product[0]} has been added to your cart.")
                except (ValueError, IndexError):
                    print("Invalid product number.")

            elif option == '2':
                sort_order = input("Sort by price (1: Ascending, 2: Descending): ")
                if sort_order in ['1', '2']:
                    display_sorted_products(products_list, sort_order)
                else:
                    print("Invalid choice.")

            elif option == '3':
                break

            elif option == '4':
                if cart:
                    total_cost = sum(item[2] * item[1] for item in cart)
                    address = input("Enter delivery address: ")
                    display_cart(cart)
                    generate_receipt(name, email, cart, total_cost, address)
                else:
                    print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day.")
                return

            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
