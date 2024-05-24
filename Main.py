from Funciones import*

primerValor = 0
segundoValor = 0
seguir = True

while seguir == True:
    match menu(primerValor,segundoValor):

        case "1":
            primerValor = pedir_validar_int(primerValor, "primer valor")

        case "2":
            segundoValor = pedir_validar_int(primerValor, "segundo valor")

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