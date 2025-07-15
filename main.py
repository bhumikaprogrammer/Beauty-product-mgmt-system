"""
WeCare Skin Care Products Management System
Main module for product display and sales operations.
"""

from datetime import datetime
from read import read_products_file
from write import update_product_file
from operation import (display_products, sell_product, restock_product, 
                      add_new_product, generate_purchase_invoice, compare_strings_case_insensitive)

def check_digit_(string):
    is_digit=False
    for each in string:
        try:
            int(each)
            is_digit = True
        except ValueError:
            pass
    return is_digit

def main():
    """
    Main function to run the WeCare product management system.
    Handles product display, sales, and inventory operations.
    
    Returns:
        None
    """
    filename = 'products.txt'
    products = read_products_file(filename)

    if not products:
        print("Error: No products found. Kindly check the products.txt file.")
        return

    while True:
        print("\nOptions:")
        print("1. Display Products")
        print("2. Sell Product")
        print("3. Restock Existing Product")
        print("4. Add New Product")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("\nThank you for using WeCare Skin Care Products System!")
            break
            
        elif choice == '1':
            display_products(products, filename)
            
        elif choice == '2':
            # Get and validate product name
            while True:
                product_name = input("Enter product name to sell: ")
                
                # Check if product name is only numbers
                if check_digit_(product_name):
                    print("Error: Product name cannot be just numbers.")
                    continue
                
                # Check if product exists before asking for more details
                product_exists = False
                for product in products:
                    if compare_strings_case_insensitive(product['name'], product_name):
                        product_exists = True
                        break
                        
                if not product_exists:
                    print("\nError: Product not found.")
                    continue
                
                break  # Valid product name, exit the loop
                
            # Get and validate quantity
            while True:
                try:
                    quantity = int(input("Enter quantity to sell: "))
                    if quantity <= 0:
                        print("Invalid quantity! Please enter a positive number.")
                        continue
                    
                    # Check if sufficient stock is available
                    sufficient_stock = False
                    for product in products:
                        if compare_strings_case_insensitive(product['name'], product_name):
                            if product['quantity'] >= quantity:
                                sufficient_stock = True
                            else:
                                print("\nError: Insufficient stock. Available:", product['quantity'])
                            break
                    
                    if not sufficient_stock:
                        continue
                    
                    break  # Valid quantity, exit the loop
                    
                except ValueError:
                    print("Invalid input! Please enter a number.")
            
            # Get and validate customer name
            while True:
                customer_name = input("Enter customer name: ")
                if not customer_name.strip():
                    print("Customer name cannot be empty!")
                    continue
                
                # Check if customer name is only numbers
                if check_digit_(customer_name):
                    print("Error: Customer name cannot be just numbers.")
                    continue
                
                break  # Valid customer name, exit the loop

            success, products = sell_product(products, product_name, quantity, customer_name)
            if success:
                update_product_file(products, filename)
                
        elif choice == '3':
            # Get and validate product name
            while True:
                product_name = input("Enter product name to restock: ")
                
                # Check if product name is only numbers
                if check_digit_(product_name):
                    print("Error: Product name cannot be numbers.")
                    continue
                
                # Check if product exists
                product_exists = False
                for product in products:
                    if compare_strings_case_insensitive(product['name'], product_name):
                        product_exists = True
                        break
                
                if not product_exists:
                    print("\nError: Product not found.")
                    continue
                
                break  # Valid product name, exit the loop
            
            # Get and validate quantity
            while True:
                try:
                    quantity = int(input("Enter quantity to purchase: "))
                    if quantity <= 0:
                        print("Invalid quantity! Please enter a positive number.")
                        continue
                    
                    break  # Valid quantity, exit the loop
                    
                except ValueError:
                    print("Invalid input! Please enter a number.")
            
            # Get and validate supplier name
            while True:
                supplier_name = input("Enter supplier name: ")
                if not supplier_name.strip():
                    print("Supplier name cannot be empty!")
                    continue
                
                # Check if supplier name is only numbers
                if check_digit_(supplier_name):
                    print("Error: Supplier name cannot be just numbers.")
                    continue
                
                break  # Valid supplier name, exit the loop

            success, products = restock_product(products, product_name, quantity, supplier_name)
            if success:
                update_product_file(products, filename)

        elif choice == '4':
            print("\nAdd New Product")
            print("-" * 20)
            
            # Get and validate product name
            while True:
                product_name = input("Enter product name: ").strip()
                if not product_name:
                    print("Product name cannot be empty!")
                    continue
                
                # Check if product name is only numbers
                if check_digit_(product_name):
                    print("Error: Product name cannot be just numbers.")
                    continue
                
                # Check if product already exists
                product_exists = False
                for product in products:
                    if compare_strings_case_insensitive(product['name'], product_name):
                        product_exists = True
                        break
                
                if product_exists:
                    print("\nError: Product already exists. Use restock option instead.")
                    continue
                
                break  # Valid product name, exit the loop
            
            # Get and validate brand name
            while True:
                brand = input("Enter brand name: ").strip()
                if not brand:
                    print("Brand name cannot be empty!")
                    continue
                
                # Check if brand name is only numbers
                if check_digit_(brand):
                    print("Error: Brand name cannot be just numbers.")
                    continue
                
                break  # Valid brand name, exit the loop
            
            # Get and validate quantity
            while True:
                try:
                    quantity = int(input("Enter quantity: "))
                    if quantity <= 0:
                        print("Invalid quantity! Please enter a positive number.")
                        continue
                    
                    break  # Valid quantity, exit the loop
                    
                except ValueError:
                    print("Invalid input! Please enter a number.")
            
            # Get and validate cost price
            while True:
                try:
                    cost_price = int(input("Enter cost price (Rs.): "))
                    if cost_price <= 0:
                        print("Invalid cost price! Please enter a positive number.")
                        continue
                    
                    break  # Valid cost price, exit the loop
                    
                except ValueError:
                    print("Invalid input! Please enter a number.")
            
            # Get and validate origin
            while True:
                origin = input("Enter country of origin: ").strip()
                if not origin:
                    print("Origin cannot be empty!")
                    continue
                
                # Check if origin is only numbers
                if check_digit_(origin):
                    print("Error: Country of origin cannot be just numbers.")
                    continue
                
                break  # Valid origin, exit the loop
            
            # Get and validate supplier name
            while True:
                supplier_name = input("Enter supplier name: ").strip()
                if not supplier_name:
                    print("Supplier name cannot be empty!")
                    continue
                
                # Check if supplier name is only numbers
                if check_digit_(supplier_name):
                    print("Error: Supplier name cannot be just numbers.")
                    continue
                
                break  # Valid supplier name, exit the loop

            success, products = add_new_product(products, product_name, brand, quantity, 
                                              cost_price, origin, supplier_name)
            if success:
                update_product_file(products, filename)
                print("\nProduct added successfully!")

        else:
            print("Invalid choice! Please sct 1-5.")


if __name__ == "__main__":
    main()
