#class for adding, deleting, checking avaialability and displaying the products
class Product:
    products = []
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
        Product.products.append(self)
        
    #function for checking the availability of the product
    def check_availability(self, quantity):
        return self.stock >= quantity
    
    #function for adding the products
    def add_product(self, name, price, stock):
        Product(name, price, stock)
        
    #function for deleting the products
    def delete_product(self, name):
        Product.products = [product for product in Product.products if product.name != name]
        
    #fucntion for displaying the products
    def display_products(self):
        if not Product.products:
            print("No products available.")
        else:
            for product in Product.products:
                print(f'Name: {product.name}, Price: {product.price}, Stock: {product.stock}')

#main function 
def main():
    p = Product("", 0, 0)

    while True:
        print("\n1. Add Product")
        print("2. Delete Product")
        print("3. Display Products")
        print("4. Check Availability")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            stock = int(input("Enter product stock: "))
            p.add_product(name, price, stock)
            print(f'Product "{name}" added successfully!')
        elif choice == '2':
            name = input("Enter product name to delete: ")
            p.delete_product(name)
            print(f'Product "{name}" deleted successfully!')
        elif choice == '3':
            print("\nAvailable Products:")
            p.display_products()
        elif choice == '4':
            name = input("Enter product name to check availability: ")
            quantity = int(input("Enter quantity to check: "))
            found = False
            for product in Product.products:
                if product.name == name:
                    found = True
                    if product.check_availability(quantity):
                        print(f'Yes, {quantity} units of "{name}" are available.')
                    else:
                        print(f'Only {product.stock} units of "{name}" are available.')
            if not found:
                print(f'Product "{name}" not found.')
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
# Run the program
main()
