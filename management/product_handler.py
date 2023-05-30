from menu import products


def get_product_by_id(id):
    if type(id) != int:
        raise TypeError("product id must be an int")

    for dicionario in products:
        if dicionario.get("_id") == id:
            return dicionario
    return {}



def get_products_by_type(type_Product):
    if type(type_Product) != str:
        raise TypeError("product type must be a str")
    response = []

    for dicionario in products:
        if type_Product in dicionario.values():
            response.append(dicionario)
    return response


def add_product(products, **menu):
    ids = []
    for product in products:
        ids.append(product['_id'])

    novo_id = max(ids) + 1 if ids else 1

    menu['_id'] = novo_id

    products.append(menu)

    return menu


def menu_report():
    product_count = len(products)
    average_price = 0
    type_product = {}
    for product in products:
        average_price += product['price']
        if product['type'] not in type_product:
            type_product[product['type']] = 1
        else:
            type_product[product['type']] += 1

    average_price = round(average_price / product_count, 2)

    most_common_type = ''
    cont = 0
    for key, value in type_product.items():
        if value > cont:
            most_common_type = key
            cont = value

    return f"Products Count: {product_count} - Average Price: ${average_price} - Most Common Type: {most_common_type}"
