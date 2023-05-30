from menu import products
from management.product_handler import get_product_by_id



def calculate_tab(comanda):

    valor_final = 0

    for produto in comanda:
        iten = get_product_by_id(produto["_id"])
        if produto["amount"] > 0:
            valor = iten['price'] * produto["amount"]
            valor_final += valor
        valor_final += iten['price']

    return valor_final
