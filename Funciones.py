import os

def limpiar_pantalla():
    os.system("cls")

def pausar():
    os.system("pause")

def menu():
    """Muestra el menú de opciones a elegir

    Returns:
        str: Devuelve la opción elegida
    """
    limpiar_pantalla()
    print("Calculadora iniciada \n")
    print("1. Ingresar 1er operando (A)")
    print("2. Ingresar 2do operando (B)")
    print("3. Calcular todas las operaciones")
    print("4. Informar resultados")
    print("5. Salir")
    return input("Elija una opción:\n ")


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

#def calcular_operaciones(primerValor:any,segundoValor:any)->any:
    """Llama y junta funciones para realizar las siguientes operaciones:
    -suma
    -resta
    -multiplicación
    -división
    -factoreo

    Args:
        primerValor (any): El primer valor para realizar el cálculo
        segundoValor (any): El segundo valor para realizar el cálculo

    
    """
    sumar(primerValor,segundoValor)
    restar(primerValor,segundoValor)
    multiplicar(primerValor,segundoValor)
    dividir(primerValor,segundoValor)
    factorial(primerValor)
    factorial(segundoValor)