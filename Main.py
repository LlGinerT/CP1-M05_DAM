# Definimos una función reutilizable que se repite hasta que
# se introduce un valor correcto en este caso un número "float"
def numcheck():
    while True:
        try:
            checked_number = float(input())
            return checked_number
        except ValueError:
            print("Key error\nPor favor, introduzca un valor numérico valido")


# Definimos la función del cálculo del área del triángulo
def pytagoras():
    print("Introduzca la base del triangulo:")
    triangle_base = numcheck()
    print("Introduzca la altura del triangulo:")
    triangle_height = numcheck()
    triangle_area = triangle_base * triangle_height / 2
    print(f"El área del triángulo es de: {triangle_area}")


# Definimos la función que mediante el operador de resto sabremos si el número es par
def pypar():
    print("Introduzca el numero a comprobar:")
    number = numcheck()
    resto = number % 2
    if resto == 0:
        print(f"{number} es un numero par")
    else:
        print(f"{number} es un numero impar")


pytagoras()
pypar()