from menu import products


def get_product_by_id(id):
    for dicionario in products:
        if id in dicionario.values():
            return dicionario
    return {}


def get_products_by_type(type):

    response = []

    for dicionario in products:
        if type in dicionario.values():
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
