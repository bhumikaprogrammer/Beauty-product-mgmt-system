"""
File Writing Module
Handles all file writing operations for the product system.
"""

def update_product_file(products, filename):
    """
    Update the product file with current product information.
    
    Args:
        products (list): List of dictionaries containing product information
        filename (str): Name of the file to update
        
    Returns:
        bool: True if update was successful, False otherwise
    """
    try:
        with open(filename, 'w') as file:
            for product in products:
                line = f"{product['name']},{product['brand']},{product['quantity']},{product['cost_price']},{product['origin']}\n"
                file.write(line)
        return True
    except Exception as e:
        print(f"Error updating file: {e}")
        return False
