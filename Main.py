# Definimos una función reutilizable que se repite hasta que
# se introduce un valor correcto en este caso un número "float"
def numcheck():
    while True:
        try:
            checked_number = float(input())
            return checked_number
        except ValueError:
            print("Valor no valido\nPor favor, introduzca un valor numérico valido")


# Definimos la función del cálculo del área del triángulo
def area_calcs():
    # creamos un bucle con un match que se repetirá hasta tener seleccionada
    # una unidad almacenada de las disponibles que usaremos luego
    while True:
        unit = input("Seleccione unidad de medida (m/cm/mm):").lower()
        match unit:
            case ("m"):
                unit = "m²"
                break
            case ("cm"):
                unit = "cm²"
                break
            case ("mm"):
                unit = "mm²"
                break
            case _:
                print("Unidad seleccionada no valida\nPor favor introduzca una unidad valida")
                continue
    print("Introduzca la base del triangulo:")
    triangle_base = numcheck()
    print("Introduzca la altura del triangulo:")
    triangle_height = numcheck()
    triangle_area = triangle_base * triangle_height / 2
    print(f"El área del triángulo es de: {triangle_area}{unit}")


# Definimos la función que mediante el operador módulo sabremos si el número es par
def par_impar():
    print("Introduzca el numero a comprobar:")
    number = numcheck()
    resto = number % 2
    if resto == 0:
        print(f"{number} es un numero par")
    else:
        print(f"{number} es un numero impar")


area_calcs()
par_impar()
