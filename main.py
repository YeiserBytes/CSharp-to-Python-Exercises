#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Yeiser Jimenez - github.com/yeiserdeveloper

import os
from time import sleep


def clear() -> None:
    """
    Clears the console screen on different operating systems.
    """
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")
    else:
        return None


def main() -> None:
    print('Menu de opciones \n')
    print('1. Ejercicio 1')
    print('2. Ejercicio 4')
    print('3. Ejercicio 5')
    print('4. Ejercicio 7')
    print('5. Ejercicio 9')
    print('6. Ejercicio 14')
    print('7. Ejercicio 15')
    print('8. Ejercicio 23')
    print('9. Ejercicio 25')
    print('10. Ejercicio 30')
    print('11. Salir \n')
    opcion = int(input('Ingrese una opcion: '))
    if opcion <= 11:
        if opcion == 1:
            salary()
        elif opcion == 2:
            timeSeconds()
        elif opcion == 3:
            timeMinute()
        elif opcion == 4:
            sumSalary()
        elif opcion == 5:
            studentNotes()
        elif opcion == 6:
            meanHundred()
        elif opcion == 7:
            carculate_sum_product()
        elif opcion == 8:
            carculate_division_product()
        elif opcion == 9:
            hypotenuse()
        elif opcion == 10:
            average()
        else:
            print('Gracias por usar el programa!')
            sleep(2)
    else:
        print('Opcion no valida!')

# ejercicio 1
# A un trabajador le pagan según sus horas y una tarifa de pago por Horas. Si la cantidad de horas trabajadas es mayor a 40 horas. La Tarifa se incrementa en un 50% para las horas extras. Calcular el Salario del trabajador dadas las horas trabajadas y la tarifa.


def salary() -> None:
    clear()
    print('Ejercicio 1 \n')
    workHour = float(input("Ingrese horas trabajadas: "))
    fee = float(input("Ingrese la tarifa: "))
    if (workHour <= 40):
        salary = workHour * fee
        print(f'El salario es: {salary}')
    elif (workHour > 40):
        extraHour = workHour - 40
        extraFee = fee + 0.5 * fee
        salary = extraHour * extraFee + 40 * fee
        print(f'El salario es: {salary}')
    else:
        print('Las horas trabajadas no pueden ser negativas')

# ejercicio 4
# Dado un tiempo en segundos, calcular los segundos restantes que le Correspondan para convertirse exactamente en minutos


def timeSeconds() -> None:
    clear()
    print('Ejercicio 4 \n')
    second = int(input('Ingrese el tiempo en segundos: '))
    if (second < 60 and second > 0):
        secondsRemain = 60 - second
        print(f'Le falta {secondsRemain} segundos para covertirse en minuto')
    elif (second >= 60):
        minute = (second - (second % 60)) / 60
        secondsRemain = second % 60
        print(
            f'Equivale a {minute} minutos y le faltan {secondsRemain} segundos para convertirse en minuto')
    else:
        print('La cantidad de segundos debe ser un numero positivo')

# ejercicio 5
# Dado un tiempo en minutos, calcular los días, horas y minutos que Le corresponden.


def timeMinute() -> None:
    clear()
    print('Ejercicio 5 \n')
    minute = int(input('Ingrese un tiempo en minutos: '))
    if (minute >= 0):
        days = (minute - (minute % 60)) / 1440
        x = minute % 1440
        hours = (x - (x % 60)) / 60
        minute = x % 60
        print(f'Equivale a {days} dias con {hours} horas y {minute} minutos')
    else:
        print('El tiempo no puede ser negativo')

# ejercicio 7
# Modificar el ejercicio 1 para obtener la suma de los salarios de todos los trabajadores.


def sumSalary() -> None:
    clear()
    print('Ejercicio 7 \n')
    count = int(input('Ingrese la cantidad de trabajadores: '))
    for i in range(count):
        print(f'Trabajador {i + 1}: ')
        workHour = float(input("Ingrese horas trabajadas: "))
        fee = float(input("Ingrese la tarifa: "))
        salary = workHour * fee
        total += salary
    print(f'La suma de los salarios es: {total}')

# ejercicio 9
# Dado N notas de un estudiante calcular:
# a) Cuantas notas tiene desaprobados.
# b) Cuantos aprobados.
# c) El promedio de notas.
# d) El promedio de notas aprobadas y desaprobadas.


def studentNotes() -> None:
    clear()
    print('Ejercicio 9 \n')
    prom, ca, cd, x, note, accumulate, accumulPass, accumulFail, promFail, promPass = 0, 0, 0, 1, 0, 0, 0, 0, 0, 0
    resp = "si"
    while resp == "si":
        note = float(input('Introduce la nota: '))
        resp = input('¿Desea ingresar otra nota?: ')
        if note <= 10 and note >= 0:
            cd += 1;
            accumulFail += note
        elif note > 10.5 and note < 20:
            ca += 1;
            accumulPass += note
        accumulate += note
        x = cd + ca;
        promPass = round(accumulPass / ca, 1) if ca > 0 else 0
        promFail = round(accumulFail / cd, 1) if cd > 0 else 0
        prom = round(accumulate / x, 1)
    print("La cantidad de notas desaprobadas es:", cd)
    print("La cantidad de notas aprobadas es:", ca)
    print("El promedio de las notas aprobadas es:", promPass)
    print("El promedio de las notas desaprobadas es:", promFail)
    print("El promedio final es:", prom)

# ejercicio 14
# Calcular la media de 100 números e imprimir su resultado.


def meanHundred() -> None:
    clear()
    print('Ejercicio 14 \n')
    total = 0
    for i in range(1, 101):
        num = float(input(f'Ingrese el {i} numero: '))
        total += num
    mean = round(total / 100, 2)
    print(f'\nLa media de los 100 numero ingresados es: {mean}')

# ejercicio 15
# Calcular y visualizar la suma y el producto de los Números pares comprendidos entre 20 y 400 ambos inclusive.


def carculate_sum_product() -> None:
    clear()
    print('Ejercicio 15 \n')
    total = 0
    product = 1
    for i in range(20, 31):
        total += i
        product = product * i
    print('Rango: numeros pares del 20 al 30 \n')
    print(f'La suma es: {total}')
    print(f'El producto es: {product}')

# ejercicio 23
# Hacer un programa en el que ingresados dos números por la pantalla se debe calcular la suma, diferencia, producto y división. El proceso debe finalizar al ingresar el primer número igual a cero


def carculate_division_product() -> None:
    clear()
    print('Ejercicio 23 \n')
    c = 0
    while num1 != 0:
        c += 1
        print(f'Progreso #{c}: ')
        num1 = float(input('Ingrese primer numero: '))
        if num1 != 0:
            num2 = float(input('Ingrese segundo numero: '))
            addition = num1 + num2
            subtraction = num1 - num2
            mutiplication = num1 * num2
            division = round(num1 / num2, 2)
            print(f'\nLa suma es: {addition}')
            print(f'La resta es: {subtraction}')
            print(f'La multiplicacion es: {mutiplication}')
            print(f'La division es: {division} \n')
    print('Fin del proceso')

# ejercicio 25
# Hacer un programa que calcule el valor de la hipotenusa de un triangulo rectángulo, ingresando por el teclado sus catetos (Teorema de Pitágoras)


def hypotenuse() -> None:
    clear()
    print('Ejercicio 25 \n')
    catetoA = float(input('Ingrese el cateto A: '))
    catetoB = float(input('Ingrese el cateto B: '))
    hypotenuse = round(pow(pow(catetoA, 2) + pow(catetoB, 2), 0.5), 2)
    print(f'\nLa hipotenusa es: {hypotenuse}')

# ejercicio 30
# Diseñar un formulario que permita ingresar dos notas malas y determine su promedio, debe mostrar un comentario si este está aprobado o desaprobado.


def average() -> None:
    clear()
    print('Ejercicio 30 \n')
    note1 = float(input('Ingrese la primera nota: '))
    note2 = float(input('Ingrese la segunda nota: '))
    average = (note1 + note2) / 2
    if note1 >= 0 and note1 <= 20 and note2 >= 0 and note2 <= 20:
        if average >= 10.5 and average <= 20:
            print(f'Promedio: {average}')
            print('Aprobado!')
        else:
            print(f'Promedio: {average}')
            print('Desaprobado!')
    else:
        print('Error, las notas ingresadas no se encuentran en la escala vigesimal (0-20)')


if __name__ == '__main__':
    main()
