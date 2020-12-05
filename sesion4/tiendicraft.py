def product_id(product):
    return product["id"]

def product_name(product):
    return product["name"]

def product_price(product):
    return product["price"]

def stock_add_product(stock, product, n = 1):
    for i in range(n):
        stock.append(product)

def stock_count_product(stock, product):
    count = 0
    for stock_product in stock:
        if stock_product["id"] == product["id"]:
            count += 1
    return count

def stock_count_product_by_id(stock, product_id):
    count = 0
    for stock_product in stock:
        if stock_product["id"] == product_id:
            count += 1
    return count
    
def stock_has_product(stock, product):
    for stock_product in stock:
        if stock_product["id"] == product["id"]:
            return True
    return False

def stock_has_product_by_id(stock, product_id):
    for stock_product in stock:
        if stock_product["id"] == product_id:
            return True
    return False

def stock_get_product_by_id(stock, product_id):
    for stock_product in stock:
        if stock_product["id"] == product_id:
            return stock_product
    return None

def stock_remove_product(stock, product, n = 1):
    # El número de productos en el stock
    N = stock_count_product(stock, product)
    
    # La diferencia de los productos que querían en el nuevo stock
    D = N - n
    
    # Nuevo stock sin los productos que se quieren quitar
    new_stock = [stock_product for stock_product in stock if stock_product["id"] != product["id"]]
    
    # Agregar los productos al nuevo stock de diferencia
    if D > 0:
        stock_add_product(new_stock, product, D)
            
    return new_stock

def stock_remove_product_by_id(stock, product_id, n = 1):
    product = stock_get_product_by_id(stock, product_id)
    
    # El número de productos en el stock
    N = stock_count_product_by_id(stock, product_id)
    
    # La diferencia de los productos que querían en el nuevo stock
    D = N - n
    
    # Nuevo stock sin los productos que se quieren quitar
    new_stock = [stock_product for stock_product in stock if stock_product["id"] != product_id]
    
    # Agregar los productos al nuevo stock de diferencia
    if D > 0:
        stock_add_product(new_stock, product, D)
            
    return new_stock

import pandas as pd

def stock_load(filename):
    data = pd.read_csv(filename)
    stock = []
    
    for index, row in data.iterrows():
        product = {
            "id": row["ID"],
            "name": row["NAME"],
            "price": row["PRICE"]
        }
        n = row["EXISTANCE"]
        #print(product, n)
        stock_add_product(stock, product, n)
    
    return stock
        