"""
Operations Module
Handles core business operations like displaying products, sales, and invoice generation.
"""

from datetime import datetime

# Fixed VAT rate 13 %
VAT_RATE = 0.13 
SHOP_VAT_NUMBER = "NP12345678"  # Fixed VAT number for the shop to add when selling

def display_products(products, filename):
    """
    Display all products with their details in a nicely formatted table.
    
    Args:
        products (list): List of dictionaries containing product information
        filename (str): Name of the file containing product data
        
    Returns:
        None
    """
    if not products:
        print("\nNo products available.")
        return

    # Define column widths
    name_width = 20
    brand_width = 15
    quantity_width = 8
    cost_price_width = 12
    selling_price_width = 14
    origin_width = 15

    # Print header
    print("\n" + "=" * 92)
    print(" "*25,"WeCare Skin Care Products Inventory")
    print("=" * 92)
    
    # Print column headers using manual padding
    header = "Product Name" + " " * (name_width - len("Product Name")) + " |"
    header += "Brand" + " " * (brand_width - len("Brand")) + " |"
    
    # Right align quantity with manual padding
    quantity_spaces = quantity_width - len("Quantity")
    header += " " * quantity_spaces + "Quantity" + " |"
    
    # Right align cost price with manual padding
    cost_spaces = cost_price_width - len("Cost Price")
    header += " " * cost_spaces + "Cost Price" + " |"
    
    # Right align selling price with manual padding
    selling_spaces = selling_price_width - len("Selling Price")
    header += " " * selling_spaces + "Selling Price" + " |"
    
    header += "Origin" + " " * (origin_width - len("Origin")) + " "
    print(header)
    print("-" * 92)
    
    # Print each product using manual padding
    for product in products:
        # If name too long it slices and takes only the character that fits from the first
        name = product['name']
        if len(name) > name_width:
            name = name[:name_width]
        
        # Left align name with manual padding
        row = name + " " * (name_width - len(name)) + " |"
        
        # it also slices brand name same as name
        brand = product['brand']
        if len(brand) > brand_width:
            brand = brand[:brand_width]
            
        # Left align brand with manual padding
        row += brand + " " * (brand_width - len(brand)) + " |"
        
        # Right align quantity with manual padding
        quantity_str = str(product['quantity'])
        quantity_spaces = quantity_width - len(quantity_str)
        row += " " * quantity_spaces + quantity_str + " |"
        
        # Right align cost price with manual padding
        cost_str = "Rs." + str(product['cost_price'])
        cost_spaces = cost_price_width - len(cost_str)
        row += " " * cost_spaces + cost_str + " |"
        
        # Right align selling price with manual padding
        selling_str = "Rs." + str(product['selling_price'])
        selling_spaces = selling_price_width - len(selling_str)
        row += " " * selling_spaces + selling_str + " |"
        
        # If origin too long it slices and takes only the character that fits from the first
        origin = product['origin']
        if len(origin) > origin_width:
            origin = origin[:origin_width]
            
        # Left align origin with manual padding
        row += origin + " " * (origin_width - len(origin))
        
        print(row)
    
    print("-" * 92)
    print("Total Products: " + str(len(products)))
    print("=" * 92 + "\n")

def sell_product(products, product_name, quantity, customer_name):
    """
    Process a sale transaction with buy 3 get 1 free policy.
    
    Args:
        products (list): List of dictionaries containing product information
        product_name (str): Name of the product to sell
        quantity (int): Quantity of product to sell
        customer_name (str): Name of the customer making the purchase
        
    Returns:
        tuple: (bool, list) - Success status and updated products list
    """
    for product in products:
        if compare_strings_case_insensitive(product['name'], product_name):
            if product['quantity'] >= quantity:
                free_items = quantity // 3
                total_items = quantity + free_items
                
                if product['quantity'] < total_items:
                    print("\nError: Insufficient stock for free items. Available: " + str(product['quantity']))
                    return False, products

                total_price = product['selling_price'] * quantity
                product['quantity'] -= total_items

                # Generate invoice number manually
                now = datetime.now()
                # Manual padding with zeros
                year_str = str(now.year)
                month_str = str(now.month)
                if len(month_str) == 1:
                    month_str = "0" + month_str
                    
                day_str = str(now.day)
                if len(day_str) == 1:
                    day_str = "0" + day_str
                    
                hour_str = str(now.hour)
                if len(hour_str) == 1:
                    hour_str = "0" + hour_str
                    
                minute_str = str(now.minute)
                if len(minute_str) == 1:
                    minute_str = "0" + minute_str
                    
                second_str = str(now.second)
                if len(second_str) == 1:
                    second_str = "0" + second_str
                    
                invoice_number = year_str + month_str + day_str + hour_str + minute_str + second_str

                generate_invoice(product, quantity, free_items, total_price, invoice_number, customer_name)
                return True, products
            else:
                print("\nError: Insufficient stock. Available: " + str(product['quantity']))
                return False, products
    print("\nError: Product not found.")
    return False, products


def generate_invoice(product, quantity, free_items, total_price, invoice_number, customer_name):
    """
    Generate and save a sales invoice including free items and VAT.
    
    Args:
        product (dict): Dictionary containing product information
        quantity (int): Quantity of product sold
        free_items (int): Number of free items given
        total_price (int): Total price before VAT
        invoice_number (str): Unique invoice number
        customer_name (str): Name of the customer
        
    Returns:
        None
    """
    # Get current date and time
    now = datetime.now()
    
    # Manual padding with zeros for date and time
    year_str = str(now.year)
    month_str = str(now.month)
    if len(month_str) == 1:
        month_str = "0" + month_str
        
    day_str = str(now.day)
    if len(day_str) == 1:
        day_str = "0" + day_str
        
    hour_str = str(now.hour)
    if len(hour_str) == 1:
        hour_str = "0" + hour_str
        
    minute_str = str(now.minute)
    if len(minute_str) == 1:
        minute_str = "0" + minute_str
        
    second_str = str(now.second)
    if len(second_str) == 1:
        second_str = "0" + second_str
    
    # Format date manually
    date_str = year_str + "-" + month_str + "-" + day_str
    time_str = hour_str + ":" + minute_str + ":" + second_str
    datetime_str = date_str + " " + time_str
    
    # Calculate VAT
    vat_amount = total_price * VAT_RATE
    total_with_vat = total_price + vat_amount
    
    invoice = "\n=== WeCare SKINCARE SYSTEM ===\n"
    invoice += "        SALES INVOICE\n"
    invoice += "==============================\n\n"
    invoice += "Invoice No: " + invoice_number + "\n"
    invoice += "Date: " + datetime_str + "\n"
    invoice += "VAT No: " + SHOP_VAT_NUMBER + "\n"
    invoice += "Customer Name: " + customer_name + "\n\n"
    invoice += "Product Details:\n"
    invoice += "  Name: " + product['name'] + "\n"
    invoice += "  Brand: " + product['brand'] + "\n"
    invoice += "  Origin: " + product['origin'] + "\n"
    invoice += "  Quantity Purchased: " + str(quantity) + "\n"
    invoice += "  Free Items: " + str(free_items) + "\n"
    invoice += "  Total Items: " + str(quantity + free_items) + "\n"
    invoice += "  Price per item: Rs. " + str(product['selling_price']) + "\n"
    invoice += "------------------------------\n"
    invoice += "Subtotal: Rs. " + str(total_price) + "\n"
    invoice += "VAT (" + str(int(VAT_RATE * 100)) + "%): Rs. " + str(round(vat_amount, 2)) + "\n"
    invoice += "Total Amount: Rs. " + str(round(total_with_vat, 2)) + "\n"

    # Only add the promotional message if free items were given
    if free_items > 0:
        invoice += "\n*** Buy 3 Get 1 Free Applied! ***"
        
    invoice += "\nThank you for choosing WeCare Skincare SYSTEM!\n"
    invoice += "==============================\n"
    
    try:
        with open("invoices/invoice_" + invoice_number + ".txt", 'w') as f:
            f.write(invoice)
        print("\nInvoice generated successfully!")
        print(invoice)
    except:
        print("\nWarning: Could not save invoice to file.")
        print("\nInvoice details:")
        print(invoice)

def restock_product(products, product_name, quantity, supplier_name):
    """
    Restock an existing product and generate purchase invoice with VAT.
    
    Args:
        products (list): List of dictionaries containing product information
        product_name (str): Name of the product to restock
        quantity (int): Quantity to add to inventory
        supplier_name (str): Name of the supplier
        
    Returns:
        tuple: (bool, list) - Success status and updated products list
    """
    for product in products:
        # Compare strings without using .lower()
        product_name_input = product_name
        product_name_stored = product['name']
        
        # Manual case-insensitive comparison
        if compare_strings_case_insensitive(product_name_stored, product_name_input):
            product['quantity'] += quantity
            
            # Generate purchase invoice
            now = datetime.now()
            # Manual padding with zeros
            month_str = str(now.month)
            if len(month_str) == 1:
                month_str = "0" + month_str
                
            day_str = str(now.day)
            if len(day_str) == 1:
                day_str = "0" + day_str
                
            hour_str = str(now.hour)
            if len(hour_str) == 1:
                hour_str = "0" + hour_str
                
            minute_str = str(now.minute)
            if len(minute_str) == 1:
                minute_str = "0" + minute_str
                
            second_str = str(now.second)
            if len(second_str) == 1:
                second_str = "0" + second_str
                
            invoice_number = str(now.year) + month_str + day_str + hour_str + minute_str + second_str
            
            # Calculate costs with VAT
            subtotal = quantity * product['cost_price']
            vat_amount = subtotal * VAT_RATE
            total_amount = subtotal + vat_amount
            
            # Generate "random" supplier VAT number using microseconds from datetime
            micro_seconds = str(now.microsecond)
            # Manual padding to ensure 8 digits
            while len(micro_seconds) < 8:
                micro_seconds = "0" + micro_seconds
            if len(micro_seconds) > 8:
                micro_seconds = micro_seconds[:8]
            supplier_vat = "SUP" + micro_seconds
            
            invoice = "\n=== WeCare Skincare SYSTEM ===\n"
            invoice += "        PURCHASE INVOICE\n"
            invoice += "==============================\n\n"
            invoice += "Invoice No: " + invoice_number + "\n"
            
            # Format date manually
            date_str = str(now.year) + "-" + month_str + "-" + day_str
            time_str = hour_str + ":" + minute_str + ":" + second_str
            invoice += "Date: " + date_str + " " + time_str + "\n"
            invoice += "Supplier: " + supplier_name + "\n"
            invoice += "Supplier VAT No: " + supplier_vat + "\n\n"
            invoice += "Product Details:\n"
            invoice += "  Name: " + product['name'] + "\n"
            invoice += "  Brand: " + product['brand'] + "\n"
            invoice += "  Origin: " + product['origin'] + "\n"
            invoice += "  Quantity: " + str(quantity) + "\n"
            invoice += "  Cost per item: Rs. " + str(product['cost_price']) + "\n"
            invoice += "------------------------------\n"
            invoice += "Subtotal: Rs. " + str(subtotal) + "\n"
            invoice += "VAT (" + str(int(VAT_RATE * 100)) + "%): Rs. " + str(round(vat_amount, 2)) + "\n"
            invoice += "Total Amount: Rs. " + str(round(total_amount, 2)) + "\n\n"
            invoice += "==============================\n"

            try:
                # Try to create the directory by writing to a file
                try:
                    with open("purchase_invoices/test_dir.txt", 'w') as f:
                        f.write("Test directory creation")
                except:
                    print("\nWarning: Could not create purchase_invoices directory.")
                    
                invoice_file = "purchase_invoices/purchase_invoice_" + invoice_number + ".txt"
                with open(invoice_file, 'w') as f:
                    f.write(invoice)
                print("\nPurchase invoice generated successfully!")
                print(invoice)
            except:
                print("\nWarning: Could not save purchase invoice to file.")
                print("\nPurchase Invoice details:")
                print(invoice)
            
            return True, products
    
    print("\nError: Product not found in inventory.")
    return False, products

def add_new_product(products, product_name, brand, quantity, cost_price, origin, supplier_name):
    """
    Add a completely new product to inventory and generate purchase invoice with VAT.
    
    Args:
        products (list): List of dictionaries containing product information
        product_name (str): Name of the new product
        brand (str): Brand of the new product
        quantity (int): Initial quantity to add
        cost_price (int): Cost price per unit
        origin (str): Country of origin
        supplier_name (str): Name of the supplier
        
    Returns:
        tuple: (bool, list) - Success status and updated products list
    """
    # Check if product already exists
    for product in products:
        # Manual case-insensitive comparison
        if compare_strings_case_insensitive(product['name'], product_name):
            print("\nError: Product already exists. Use restock option instead.")
            return False, products

    # Create new product with selling price as 2x of cost price
    new_product = {
        'name': product_name,
        'brand': brand,
        'quantity': quantity,
        'cost_price': cost_price,
        'selling_price': cost_price * 2,  # 2x markup
        'origin': origin
    }
    products.append(new_product)

    # Generate purchase invoice
    now = datetime.now()
    # Manual padding with zeros
    month_str = str(now.month)
    if len(month_str) == 1:
        month_str = "0" + month_str
        
    day_str = str(now.day)
    if len(day_str) == 1:
        day_str = "0" + day_str
        
    hour_str = str(now.hour)
    if len(hour_str) == 1:
        hour_str = "0" + hour_str
        
    minute_str = str(now.minute)
    if len(minute_str) == 1:
        minute_str = "0" + minute_str
        
    second_str = str(now.second)
    if len(second_str) == 1:
        second_str = "0" + second_str
        
    invoice_number = str(now.year) + month_str + day_str + hour_str + minute_str + second_str
    
    # Calculate costs with VAT
    subtotal = quantity * cost_price
    vat_amount = subtotal * VAT_RATE
    total_amount = subtotal + vat_amount
    
    # Generate "random" supplier VAT number using microseconds from datetime
    micro_seconds = str(now.microsecond)
    # Manual padding to ensure 8 digits
    while len(micro_seconds) < 8:
        micro_seconds = "0" + micro_seconds
    if len(micro_seconds) > 8:
        micro_seconds = micro_seconds[:8]
    supplier_vat = "SUP" + micro_seconds
    
    invoice = "\n=== WeCare Skincare SYSTEM ===\n"
    invoice += "        PURCHASE INVOICE\n"
    invoice += "==============================\n\n"
    invoice += "Invoice No: " + invoice_number + "\n"
    
    # Format date manually
    date_str = str(now.year) + "-" + month_str + "-" + day_str
    time_str = hour_str + ":" + minute_str + ":" + second_str
    invoice += "Date: " + date_str + " " + time_str + "\n"
    invoice += "Supplier: " + supplier_name + "\n"
    invoice += "Supplier VAT No: " + supplier_vat + "\n\n"
    invoice += "Product Details:\n"
    invoice += "  Name: " + product_name + "\n"
    invoice += "  Brand: " + brand + "\n"
    invoice += "  Origin: " + origin + "\n"
    invoice += "  Quantity: " + str(quantity) + "\n"
    invoice += "  Cost per item: Rs. " + str(cost_price) + "\n"
    invoice += "------------------------------\n"
    invoice += "Subtotal: Rs. " + str(subtotal) + "\n"
    invoice += "VAT (" + str(int(VAT_RATE * 100)) + "%): Rs. " + str(round(vat_amount, 2)) + "\n"
    invoice += "Total Amount: Rs. " + str(round(total_amount, 2)) + "\n\n"
    invoice += "==============================\n"

    try:
        # Try to create the directory by writing to a file
        try:
            with open("purchase_invoices/test_dir.txt", 'w') as f:
                f.write("Test directory creation")
        except:
            print("\nWarning: Could not create purchase_invoices directory.")
            
        invoice_file = "purchase_invoices/purchase_invoice_" + invoice_number + ".txt"
        with open(invoice_file, 'w') as f:
            f.write(invoice)
        print("\nPurchase invoice generated successfully!")
        print(invoice)
    except:
        print("\nWarning: Could not save purchase invoice to file.")
        print("\nPurchase Invoice details:")
        print(invoice)

    return True, products

def generate_purchase_invoice(items, supplier_name):
    """
    Generate and save a purchase invoice for restocking.

    Arguments:
        items (list): List of dictionaries containing product and purchase details
        supplier_name (str): Name of the supplier

    Returns:
        None
    """
    # Generate invoice number manually
    now = datetime.now()
    # Manual padding with zeros
    year_str = str(now.year)
    month_str = str(now.month)
    if len(month_str) == 1:
        month_str = "0" + month_str
        
    day_str = str(now.day)
    if len(day_str) == 1:
        day_str = "0" + day_str
        
    hour_str = str(now.hour)
    if len(hour_str) == 1:
        hour_str = "0" + hour_str
        
    minute_str = str(now.minute)
    if len(minute_str) == 1:
        minute_str = "0" + minute_str
        
    second_str = str(now.second)
    if len(second_str) == 1:
        second_str = "0" + second_str
        
    invoice_number = year_str + month_str + day_str + hour_str + minute_str + second_str
    
    # Calculate total amount
    total_amount = 0
    for item in items:
        item_total = item['quantity'] * item['cost_price']
        total_amount += item_total
    
    # Format date manually
    date_str = year_str + "-" + month_str + "-" + day_str
    time_str = hour_str + ":" + minute_str + ":" + second_str
    datetime_str = date_str + " " + time_str
    
    invoice = "\n=== WeCare Skin Care Products ===\n"
    invoice += "        PURCHASE INVOICE\n"
    invoice += "==============================\n\n"
    invoice += "Invoice No: " + invoice_number + "\n"
    invoice += "Date: " + datetime_str + "\n"
    invoice += "Supplier: " + supplier_name + "\n\n"
    invoice += "Product Details:\n"
    
    # Add each product to the invoice
    for item in items:
        product = item['product']
        invoice += "  Product: " + product['name'] + "\n"
        invoice += "  Brand: " + product['brand'] + "\n"
        invoice += "  Origin: " + product['origin'] + "\n"
        invoice += "  Quantity: " + str(item['quantity']) + "\n"
        invoice += "  Rate per item: Rs. " + str(item['cost_price']) + "\n"
        invoice += "  Subtotal: Rs. " + str(item['quantity'] * item['cost_price']) + "\n"
        invoice += "-" * 50 + "\n"

    invoice += "Total Amount: Rs. " + str(total_amount) + "\n\n"
    invoice += "==============================\n"

    # Try to create the directory by writing to a file
    try:
        with open("purchase_invoices/test_dir.txt", 'w') as f:
            f.write("Test directory creation")
    except:
        print("\nWarning: Could not create purchase_invoices directory.")
        
    invoice_file = "purchase_invoices/purchase_invoice_" + invoice_number + ".txt"
    
    try:
        with open(invoice_file, 'w') as f:
            f.write(invoice)
        
        print("\nPurchase invoice generated successfully!")
        print(invoice)
        print("Invoice saved as: " + invoice_file)
    except:
        print("\nWarning: Could not save purchase invoice to file.")
        print("\nPurchase Invoice details:")
        print(invoice)

def compare_strings_case_insensitive(str1, str2):
    """
    Compare two strings in a case-insensitive manner without using .lower() or .upper()
    
    Args:
        str1 (str): First string to compare
        str2 (str): Second string to compare
        
    Returns:
        bool: True if strings are equal ignoring case, False otherwise
    """
    if len(str1) != len(str2):
        return False
        
    for i in range(len(str1)):
        char1 = str1[i]
        char2 = str2[i]
        
        # Convert to ASCII values
        ascii1 = ord(char1)
        ascii2 = ord(char2)
        
        # If both are letters, convert to same case for comparison
        is_char1_upper = 65 <= ascii1 <= 90  # A-Z
        is_char1_lower = 97 <= ascii1 <= 122  # a-z
        is_char2_upper = 65 <= ascii2 <= 90  # A-Z
        is_char2_lower = 97 <= ascii2 <= 122  # a-z
        
        # If one is uppercase and one is lowercase of the same letter
        if (is_char1_upper and is_char2_lower and ascii1 + 32 == ascii2) or \
           (is_char1_lower and is_char2_upper and ascii1 - 32 == ascii2):
            continue
            
        # If both are uppercase or both are lowercase, direct comparison
        elif ascii1 == ascii2:
            continue
            
        # If characters don't match (accounting for case)
        else:
            return False
            
    return True
