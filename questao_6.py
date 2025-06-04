from funcoes import *

'''

6. Faça um programa que calcule a média de chuvas em 7 dias. Se a média for maior
que 90 mm, exiba "Semana crítica! Monitoramento intensivo necessário".

'''

chuvas_diarias = []

for i in range(7):
    chuva = float(input(f"Digite a quantidade de chuva do dia {i+1} em ( mm ): "))
    chuvas_diarias.append(chuva)

media_critica, msg_critica = calcular_media_chuva_semanal_e_alertar(chuvas_diarias)
print(f"Média de chuva (crítica): {media_critica:.2f}mm.\nMensagem: '{msg_critica}'")