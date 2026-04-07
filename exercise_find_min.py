# Ejercicio 6: Encontrar el mínimo en una lista
from re import search


def find_min(lista):
    """
    Encuentra y retorna el valor mínimo en una lista de números.
    Si la lista está vacía, retorna None.

    Args:
        lista: Una lista de números

    Returns:
        El valor mínimo de la lista o None si está vacía
    """

    if not lista:
        return None

    minimo = min(lista)
    return(minimo)
