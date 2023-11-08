t_base = float(input("Introduzca la base del triangulo:"))
t_height = float(input("Introduzca la altura del triangulo:"))
t_area = t_base * t_height / 2
print(f"el area del triangulo es de {t_area}")

numcheck = float(input("Introduzca el numero a comprobar:"))
pypar = numcheck % 2
if pypar == 0:
    print(f"{numcheck} es un numero par")
else:
    print(f"{numcheck} es un numero impar")
