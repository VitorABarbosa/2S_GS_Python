from funcoes import *


'''

1. Crie um programa que pergunte a quantidade de milímetros de chuva prevista para
uma cidade. Se for maior que 100 mm, exiba a mensagem: "ALERTA: Risco alto de
inundação". Caso contrário, exiba "Nível de risco normal".

'''

perguntar_mm = float(input("Digite a quantidade de milímetros de chuva prevista para uma cidade: "))

print(verificar_risco_inundacao_por_chuva(perguntar_mm))
