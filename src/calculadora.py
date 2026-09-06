"""Funções de apoio para somar valores de uma lista de compras."""


def somar_precos(precos):
    total = 0
    for p in precos:
        total = total + p
    return total


def somar_quantidades(quantidades):
    total = 0
    for q in quantidades:
        total = total + q
    return total


def calcular_media_precos(precos):
    total = 0
    for p in precos:
        total = total + p
    return total / len(precos)
