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


search = input("What product are you looking for? ")

search_products(products, search)

add_product(products)
            

