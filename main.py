cart = {}

while True:
    print("\n1. Add item")
    print("2. Remove item")
    print("3. View cart")
    print("4. Checkout")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        item = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))

        if item in cart:
            cart[item]['quantity'] += quantity
        else:
            cart[item] = {'quantity': quantity, 'price': price}

        print("Item added to cart.")

    elif choice == '2':
        item = input("Enter item to remove: ")

        if item in cart:
            del cart[item]
            print("Item removed.")
        else:
            print("Item not found.")

    elif choice == '3':
        if cart:
            print("Shopping Cart:")
            for item, details in cart.items():
                quantity = details['quantity']
                price = details['price']
                print(f"{item} - Quantity: {quantity}, Price: ${price}")
        else:
            print("Your cart is empty.")

    elif choice == '4':
        if cart:
            total_price = sum(details['quantity'] * details['price'] for details in cart.values())
            print("Shopping Cart:")
            for item, details in cart.items():
                quantity = details['quantity']
                price = details['price']
                print(f"{item} - Quantity: {quantity}, Price: ${price}")

            print(f"Total Price: ${total_price}")
            break
        else:
            print("Cart is empty.")

    elif choice == '5':
        break

    else:
        print("Invalid choice. Please enter (1-5).")
