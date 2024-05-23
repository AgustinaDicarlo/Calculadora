from Funciones import*

print("Calculadora iniciada \n")
print("1. Ingresar 1er operando")
print("2. Ingresar 2do operando")
print("3. Calcular todas las operaciones")
print("4. Informar resultados")
print("5. Salir")

opcion = input("Elija una opción:\n ")

rta = "s"
while rta == "s":
    match opcion:
        case "1":
            primerValor = input("Ingrese el primer valor")
        case "2":
            segundoValor = input("Ingrese el segundo valor")
        case "3":
            resultadoSumar = sumar()
            resultadoRestar = restar()
            resultadoMultiplicar = multiplicar()
            resultadoDividir = dividir()
            resultadoFactoreo = factorial()

        case "4":
            pass
        case "5":
            break