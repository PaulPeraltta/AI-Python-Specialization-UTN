# •Realizar un programa que solicite la carga por teclado de dos números, si el
# primero es mayor al segundo informar su suma y diferencia, en caso contrario
# informar el producto y la división del primero respecto al segundo.

# num1 = input("Ingresar primer numero: ")
# num2 = input("Ingresar segundo numero: ")

# if num1 > num2:
#     suma = int(num1) + int(num2)
#     diferencia = int(num1) - int(num2)
#     print("La suma es: " + str(suma))
#     print("La diferencia es: " + str(diferencia))


# •Se ingresan tres notas de un alumno, si el promedio es mayor o igual a siete
# mostrar un mensaje "Promocionado".

# nota1 = input("Ingresar primer nota: ")
# nota2 = input("Ingresar segunda nota: ")
# nota3 = input("Ingresar tercer nota: ")

# promedio = (int(nota1) + int(nota2) + int(nota3)) / 3

# if promedio >= 7:
#     print("Promocionado")
# else:
#     print("No promocionado")

# •Se ingresa por teclado un número positivo de uno o dos dígitos (1..99) mostrar
# un mensaje indicando si el número tiene uno o dos dígitos.
# (Tener en cuenta que condición debe cumplirse para tener dos dígitos un número entero)

# def evaluar_cifras(number):
#     # number = int(input("Ingresa un numero entero: "))
#     if number >= 0 and number <= 9:
#         print("Tu numero solo tiene un digito")
#     else: 
#         if number >= 10 and number <= 99:
#             print("Tu numero tiene dos digitos") 
#         else: 
#             if number >= 100:
#                 print("Tu numero tiene tres digitos")


# •Se cargan por teclado tres números distintos. Mostrar por pantalla el mayor
# de ellos.

# print("Prueba de mayor numero")
# num1 = int(input("ingresar primer numero: "))
# num2 = int(input("ingresar segundo numero: "))
# num3 = int(input("ingresar tercer numero: "))

# if num1 > num2 and num1 > num3:
#     print("El numero mas grande es: ", num1)
# else:
#     if num2 > num3:
#         print("El numero mas alto es el: ", num2)
#     else: print("El numero mas grandisimo es el:", num3)


# •Se ingresa por teclado un valor entero, mostrar una leyenda que indique si el
# número es positivo, negativo o nulo (es decir cero)

# numero = int(input("Ingresar numero: "))

# if numero < 0:
#     print("Es numero negativo")
# if numero == 0:
#     print("Es numero nulo")
# if numero > 0:
#     print("Es numero positivo")


# •Confeccionar un programa que permita cargar un número entero positivo de
# hasta tres cifras y muestre un mensaje indicando si tiene 1, 2, o 3 cifras.
# Mostrar un mensaje de error si el número de cifras es mayor.

# numero = int(input("Ingresar numero: "))

# if numero > 0 and numero <= 999:
#     evaluar_cifras(numero) # linea 33
# else:
#     print("Numero no compatible")


# •Un postulante a un empleo, realiza un test de capacitación, se obtuvo la
# siguiente información: cantidad total de preguntas que se le realizaron y la
# cantidad de preguntas que contestó correctamente. Se pide confeccionar un
# programa que ingrese los dos datos por teclado e informe el nivel del mismo
# según el porcentaje de respuestas correctas que ha obtenido, y sabiendo que:
# Nivel máximo: Porcentaje>=90%.
# Nivel medio: Porcentaje>=75% y <90%.
# Nivel regular: Porcentaje>=50% y <75%.
# Fuera de nivel: Porcentaje<50%.

# questions = int(input("Ingresar cantidad total de preguntas: "))
# answered = int(input("Ingresar cantidad total de respuestas correctas: "))

# percent = int((questions * answered) / 100)

# if percent >= 90:
#     print("Nivel maximo")
# elif percent >= 75:
#     print("Nivel medio")
# elif percent >= 50:
#     print("Nivel regular")
# elif percent < 50:
#     print("Fuera de nivel")


# •Realizar un programa que pida cargar una fecha cualquiera, luego verificar si
# dicha fecha corresponde a Navidad.
# •Se ingresan por teclado tres números, si todos los valores ingresados son
# menores a 10, imprimir en pantalla la leyenda "Todos los números son
# menores a diez".
# •Se ingresan por teclado tres números, si al menos uno de los valores
# ingresados es menor a 10, imprimir en pantalla la leyenda "Alguno de los
# números es menor a diez".
# •Se ingresan tres valores por teclado, si todos son iguales se imprime la suma
# del primero con el segundo y a este resultado se lo multiplica por el tercero.
# •Escribir un programa que pida ingresar la coordenada de un punto en el
# plano, es decir dos valores enteros x e y (distintos a cero).
# Posteriormente imprimir en pantalla en que cuadrante se ubica dicho punto.
# (1º Cuadrante si x > 0 Y y > 0 , 2º Cuadrante: x < 0 Y y > 0, etc.)
# •De un operario se conoce su sueldo y los años de antigüedad. Se pide
# confeccionar un programa que lea los datos de entrada e informe:
# a) Si el sueldo es inferior a 500 y su antigüedad es igual o superior a 10 años,
# otorgarle un aumento del 20 %, mostrar el sueldo a pagar.
# b)Si el sueldo es inferior a 500 pero su antigüedad es menor a 10 años,
# otorgarle un aumento de 5 %.
# c) Si el sueldo es mayor o igual a 500 mostrar el sueldo en pantalla sin
# cambios.
# •Escribir un programa en el cual: dada una lista de tres valores numéricos
# distintos se calcule e informe su rango de variación (debe mostrar el mayor y el
# menor de ellos)
