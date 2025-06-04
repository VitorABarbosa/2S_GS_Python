from funcoes import *

'''

10. Escreva uma função que receba um valor numérico representando o nível do rio em
metros. Caso o nível esteja acima de 5 metros, retorne "EVACUAR ÁREA". Caso
contrário, "Segurança controlada".

'''

nivel_rio = float(input("Digite o nível do rio em ( metros ): "))

print(verificar_nivel_rio(nivel_rio))