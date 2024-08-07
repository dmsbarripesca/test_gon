import asyncio
import os


#ABRIMOS Y LEEMOS EL TXT
with open('carpeta/numero.txt', 'r') as file:
    numero_leido = file.read()

#SUMAMOS 1 AL NÚMERO LEIDO
numero_leido = int(numero_leido)
numero_a_escribir = numero_leido + 1
numero_a_escribir = str(numero_a_escribir)

#SOBRESCRIBIMOS EL TXT CON EL NÚMEOR QUE LEIMOS + 1
with open('carpeta/numero.txt', 'w') as file:
    numero_leido = file.write(numero_a_escribir)

