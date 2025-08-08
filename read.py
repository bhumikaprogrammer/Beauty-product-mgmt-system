"""
Read.py is for reading the text file.
Handles all file reading operations for the WeCare management system
"""

def read_products_file(filename):
    """
    Reads product data from a file and creates a list of product dictionaries.

    Arguments:
        filename (str): Name of the file containing product data

    Returns:
        list: List of dictionaries containing product information
    """
    products = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                if not line.strip():
                    continue

                data = [item.strip() for item in line.strip().split(',')]
                if len(data) != 5:  # Ensure we have all required fields
                    continue
                    
                try:
                    product = {
                        'name': data[0],
                        'brand': data[1],
                        'quantity': int(data[2]),
                        'cost_price': int(data[3]),
                        'origin': data[4],
                        'selling_price': int(data[3]) * 2  # 2x markup
                    }
                    products.append(product)
                except (ValueError, IndexError):
                    print(f"Warning: Skipping invalid line: {line.strip()}")
                    continue
                    
        return products
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []
 