from funcoes import *

'''

4. Escreva um programa que leia 5 temperaturas extremas (em graus Celsius) e diga
qual foi a mais alta e a mais baixa registrada.

'''

temperaturas = []

for i in range(5):
    temperatura = float(input(f"Digite a temperatura {i+1} em ( graus Celsius ): "))
    temperaturas.append(temperatura)

print(encontrar_temperaturas_extremas(temperaturas))

