print("Calculadora")

def suma(num1, num2):
    return num1 + num2


def resta(num1, num2):
    return num1 - num2


def multiplicacion(num1, num2):
    return num1 * num2


def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        raise ZeroDivisionError("No se puede dividir entre cero.")


while True:
    print("Seleccione la operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = int(input("Opción: "))

    if opcion == 1:
        num1 = float(input("Introduzca el primer número: "))
        num2 = float(input("Introduzca el segundo número: "))
        resultado = suma(num1, num2)

    elif opcion == 2:
        num1 = float(input("Introduzca el primer número: "))
        num2 = float(input("Introduzca el segundo número: "))
        resultado = resta(num1, num2)

    elif opcion == 3:
        num1 = float(input("Introduzca el primer número: "))
        num2 = float(input("Introduzca el segundo número: "))
        resultado = multiplicacion(num1, num2)

    elif opcion == 4:
        num1 = float(input("Introduzca el primer número: "))
        num2 = float(input("Introduzca el segundo número: "))
        try:
            resultado = division(num1, num2)
            print(f"El resultado es: {resultado}")
        except ZeroDivisionError:
            print("Error: No se puede dividir entre cero.")

    elif opcion == 5:
        print("Gracias por usar la calculadora")
        break

    else:
        print("Opción incorrecta")

    print("")