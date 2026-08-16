"""Demo app -- pequeño e intencionalmente con un par de cosas para arreglar."""


def login(username, password):
    # BUG: no valida password vacio
    if username:
        return True
    return False


def get_total(items):
    total = 0
    for item in items:
        total = total + item["price"]
    return total
