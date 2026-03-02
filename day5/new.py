class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, amount):
        self.quantity += amount

    def __str__(self):
        return f"ID: {self.product_id}, Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"


class Inventory:
    def __init__(self):
        self.products = {}  # Dictionary 

    def add_product(self):
        try:
            product_id = int(input("Enter Product ID: "))
            if product_id in self.products:
                print("Product ID already exists!")
                return

            name = input("Enter Product Name: ")
            price = float(input("Enter Price: "))
            quantity = int(input("Enter Quantity: "))

            if price < 0 or quantity < 0:
                print("Price and Quantity cannot be negative!")
                return

            product = Product(product_id, name, price, quantity)# create an object
            self.products[product_id] = product
            print("Product added successfully!")

        except ValueError:
            print("Invalid input! Please enter correct data types.")

    def view_products(self):
        if not self.products:
            print("Inventory is empty.")
            return
        for product in self.products.values():
            print(product)

    def search_product(self):
        product_id = int(input("Enter Product ID to search: "))
        product = self.products.get(product_id)
        if product:
            print(product) # object
        else:
            print("Product not found.")

    def delete_product(self):
        product_id = int(input("Enter Product ID to delete: "))
        if product_id in self.products:
            del self.products[product_id]
            print("Product deleted successfully.")
        else:
            print("Product not found.")

    def restock_product(self):
        product_id = int(input("Enter Product ID to restock: "))
        product = self.products.get(product_id)
        if product:
            amount = int(input("Enter quantity to add: "))
            if amount > 0:
                product.update_quantity(amount)
                print("Stock updated successfully.")
            else:
                print("Invalid quantity.")
        else:
            print("Product not found.")

    def sell_product(self):
        product_id = int(input("Enter Product ID to sell: "))
        product = self.products.get(product_id)
        if product:
            amount = int(input("Enter quantity to sell: "))
            if 0 < amount <= product.quantity:
                product.update_quantity(-amount)
                print("Sale recorded successfully.")
            else:
                print("Insufficient stock or invalid quantity.")
        else:
            print("Product not found.")

    def low_stock_alert(self):
        threshold = int(input("Enter low stock threshold: "))
        print("Low Stock Products:")
        found = False
        for product in self.products.values():
            if product.quantity <= threshold:
                print(product)
                found = True
        if not found:
            print("No low stock products.")
         

def main():
    inventory = Inventory()

    while True:
        print("\n==== Warehouse Inventory Menu ====")
        print("1. Add Product")
        print("2. View Products")
        print("3. Search Product")
        print("4. Delete Product")
        print("5. Restock Product")
        print("6. Sell Product")
        print("7. Low Stock Alert")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            inventory.add_product()
        elif choice == "2":
            inventory.view_products()
        elif choice == "3":
            inventory.search_product()
        elif choice == "4":
            inventory.delete_product()
        elif choice == "5":
            inventory.restock_product()
        elif choice == "6":
            inventory.sell_product()
        elif choice == "7":
            inventory.low_stock_alert()
        elif choice == "8":
            print("Exiting system...")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()