import os

def limpiar_pantalla():
    os.system("cls")

def pausar():
    os.system("pause")

def menu(a:int,b:int):
    """Muestra el menú de opciones a elegir

    Returns:
        str: Devuelve la opción elegida
    """
    limpiar_pantalla()
    print("Calculadora iniciada \n")
    print(f"1. Ingresar 1er operando (A)\n» {a}")
    print(f"2. Ingresar 2do operando (B)\n» {b}")
    print("3. Calcular todas las operaciones")
    print("4. Informar resultados")
    print("5. Salir")
    return input("Elija una opción:\n ")


##########################################OPERACIONES##############################################
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
    
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Error. No se puede dividir por 0")
        resultado = "No se pudo dividir porque el divisor es 0"
    else:
        resultado

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
######################################################################################################


def mostrar_mensaje_resultados(resultadoSumar,resultadoRestar,resultadoMultiplicar,
                               resultadoDividir,resultadoFactoreoA,resultadoFactoreoB):
    """Junta los resultados de los calculos para mostrarlos en un mensaje

    Args:
        resultadoSumar (int): Resultado de la suma
        resultadoRestar (int): Resultado de la resta 
        resultadoMultiplicar (int): Resultado de la multiplicación
        resultadoDividir (float): Resultado de la división
        resultadoFactoreoA (int): Resultado de la factoreo de A
        resultadoFactoreoB (int): Resultado de la factoreo de B
    """
    
    print(f"El resultado de A + B es: {resultadoSumar}")
    print(f"El resultado de A - B es: {resultadoRestar}")
    print(f"El resultado de A * B es: {resultadoMultiplicar}")
    print(f"El resultado de A / B es: {resultadoDividir}")
    print(f"El resultado de A! es {resultadoFactoreoA} y el resultado de B! es {resultadoFactoreoB}")

def pedir_validar_int(validar,texto):
    """Pide y valida el valor para que sea un entero

    Args:
        validar (any): Valor a validar
        texto (str): mensaje

    Returns:
        int: El valor ya validado
    """
    while True:
        validar = input(f"Ingrese el {texto} valor: \n")
        if (validar.isdigit()):
            validar = int(validar)
            break
        else:
            print("Eso no es un número positivo\n")

    return validar