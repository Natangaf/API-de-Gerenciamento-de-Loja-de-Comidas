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
