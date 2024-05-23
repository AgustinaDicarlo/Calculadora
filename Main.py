from Funciones import*

primerValor = 0
segundoValor = 0
seguir = True

while seguir == True:
    match menu(primerValor,segundoValor):

        case "1":
            primerValor = input("Ingrese el primer valor: ")
            if (primerValor.isdigit()):
                primerValor = int(primerValor)
            else:
                print("Eso no es un número entero positivo")

        case "2":
            segundoValor = input("Ingrese el segundo valor: ")
            if (segundoValor.isdigit()):
                segundoValor = int(segundoValor)
            else:
                print("Eso no es un número entero positivo")

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

            mostrar_mensaje_resultados(resultadoSumar,resultadoRestar,resultadoMultiplicar,resultadoDividir,
                                       resultadoFactoreoA,resultadoFactoreoB)

        case "5":
            respuesta = input(print("Desea salir?")).lower
            if respuesta == "s":
                seguir = False
            else:
                seguir = True
    pausar()
print("Fin del programa...")