
def sumar(a:int, b:int)->int:
    """Hace una suma entre dos números

    Args:
        a (int): Primer valor de tipo entero
        b (int): Segundo valor de tipo entero

    Returns:
        int: Devuelve el valor de la suma
    """
    resultado = a + b
    return resultado


def restar(a:int, b:int)->int:
    """Hace una resta entre dos números

    Args:
        a (int): Primer valor de tipo entero
        b (int): Segundo valor de tipo entero

    Returns:
        int: Devuelve el valor de la resta
    """
    resultado = a - b
    return resultado


def multiplicar(a:int, b:int)->int:
    """Hace una multiplicación entre dos números

    Args:
        a (int): Primer valor de tipo entero
        b (int): Segundo valor de tipo entero

    Returns:
        int: Devuelve el valor de la mutiplicación
    """
    resultado = a * b
    return resultado


def dividir(a:int,b:int)->float:
    """Hace una división entre dos números

    Args:
        a (int): Primer valor de tipo entero
        b (int): Segundo valor de tipo entero

    Returns:
        float: Devuelve el valor de la división
    """
    resultado = a / b
    return resultado

def factorial(n:int)->int:
    """Hace el factoreo de los números positivos hasta "n"

    Args:
        n (int): Numero a sacar el factoreo

    Returns:
        int: Resultado total del factoreo
    """
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    
    return resultado

