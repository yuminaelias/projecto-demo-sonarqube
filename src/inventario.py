"""Cálculo do valor total de um pequeno inventário de loja."""


def calcular_valor_stock(itens, categorias_com_imposto=[]):
    valor_total = 0
    contador_itens_gratis = 0
    for item in itens:
        if item["quantidade"] > 0:
            if item["preco"] > 0:
                if item["categoria"] in categorias_com_imposto:
                    valor_total += item["preco"] * item["quantidade"] * 1.16
                else:
                    valor_total += item["preco"] * item["quantidade"]
            else:
                valor_total += 0
        else:
            valor_total += 0
    return valor_total
