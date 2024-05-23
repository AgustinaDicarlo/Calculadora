from Funciones import*

rta = "s"
while rta == "s":
    match menu():
        case "1":
            primerValor = input("Ingrese el primer valor: ")

            if (primerValor.isdigit()):
                primerValor = int(primerValor)
            else:
                print("Eso no es un número")

        case "2":
            segundoValor = input("Ingrese el segundo valor: ")
            if (segundoValor.isdigit()):
                segundoValor = int(segundoValor)
            else:
                print("Eso no es un número")

        case "3":
            resultadoSumar = sumar(primerValor,segundoValor)
            resultadoRestar = restar(primerValor,segundoValor)
            resultadoMultiplicar = multiplicar(primerValor,segundoValor)
            resultadoDividir = dividir(primerValor,segundoValor)
            resultadoFactoreoA = factorial(primerValor)
            resultadoFactoreoB = factorial(segundoValor)
            
            print("Los cálculos se realizaron exitosamente")

        case "4":
            print(f"Dados los números {primerValor} y {segundoValor}...\n")
            print(f"El resultado de A + B es: {resultadoSumar}")
            print(f"El resultado de A - B es: {resultadoRestar}")
            print(f"El resultado de A * B es: {resultadoMultiplicar}")
            print(f"El resultado de A / B es: {resultadoDividir}")
            print(f"El resultado de A! es {resultadoFactoreoA} y el resultado de B! es {resultadoFactoreoB}")

        case "5":
            rta = input(print("Desea salir?"))
            if rta == "s":
                rta = "n"
            break
    pausar()
print("Fin del programa...")