products = [
    {
    
        "name": "RTX 5070",
        "price": 1499.98,
        "retailer": "Canada Computers"
    },
    {
        "name": "Ryzen 7 9800x3d",
        "price": 599.99,
        "retailer": "Canada Computers"
    },
    {
        "name": "Corsair Vengence ram 32gb DDR5",
        "price": 399.99,
        "retailer": "Canada Computers"
    }
]

def search_products(products, search):
    for product in products:
        if search.lower() in product["name"].lower():
            print()
            print(product["name"])
            print(f"Price: ${product["price"]}")
            print(f"Retailer: {product["retailer"]}")

def add_product(products):

    name = input("\nEnter product name: ")
    price = input("Enter price of product: ")
    retailer = input("Enter retailer of this product: ")
    new_product = {
        "name": name,
        "price": price,
        "retailer": retailer
    }
    products.append(new_product)
    print("Product added")

def display_products(products):
    for product in products:
        print()
        print(f"Product: {product['name']}")
        print(f"Product: {product['price']}")
        print(f"Product: {product['retailer']}")

while True:
    print()
    print("-----------------------")
    print("   PC Price Tracker")      
    print("-----------------------")
    print("1. Search all products")
    print("2. Add a product")
    print("3. View all products")
    print("4. Exit")

    choice = input("Provide an input: ")

    if choice == 1:
        search = input("What product are you looking for?: ")
        search_products(search)

    elif choice == 2:
        add_product(products)

    elif choice == 3:
        display_products(products)

    elif choice == 4:
        break

    else:
        print("Invalid input please re-enter: ")
