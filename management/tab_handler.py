from menu import products
from management.product_handler import get_product_by_id


def calculate_tab(comanda):
    valor_final = 0

    for produto in comanda:
        item = get_product_by_id(produto["_id"])
        valor = item['price'] * produto["amount"]
        valor_final += valor

    valor_final = round(valor_final, 2)

    return {"subtotal": f'${valor_final}'}
